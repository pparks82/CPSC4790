import csv
from competition import Competition
from league import League
from team import Team
from team_member import TeamMember
from singleton import Singleton
import pickle


@Singleton
class LeagueDatabase:
    _sole_instance = None
    _last_oid = 0

    def __init__(self):
        self._sole_instance = Singleton(LeagueDatabase)
        self._leagues = []

    @classmethod
    def load(cls, file_name):
        try:
            file = open(file_name, 'rb')
            cls._sole_instance = pickle.load(file)
            file.close()
        except FileNotFoundError:
            file = open(file_name+".backup", 'rb')
            cls._sole_instance = pickle.load(file)
            file.close()

    @property
    def leagues(self):
        return self._leagues

    def add_league(self, league):
        self._leagues.append(league)
        return None

    def remove_league(self, league):
        if league in self._leagues:
            self._leagues.remove(league)
        else:
            return

    def league_named(self, name):
        for league in self._leagues:
            if league.name == name:
                return league
            else:
                return None

    def next_oid(self):
        self._last_oid += 1
        return self._last_oid

    def save(self, file_name):
        try:
            file = open(file_name, 'wb')
            pickle.dump(self._sole_instance, file)
            file.close()
        except FileNotFoundError:
            file = open(file_name+".backup", 'wb')
            pickle.dump(self._sole_instance, file)
            file.close()

    def import_league_teams(self, league, file_name):
        reader = csv.reader(open(file_name, 'r'))
        next(reader, None)
        for row in reader:
            team = Team(self.next_oid(), row[0])
            team.add_member(TeamMember(self.next_oid(), row[1], row[2]))
            league.add_team(team)
        self._leagues.append(league)

    def export_league_teams(self, file_name):
        file = open(file_name, 'w')
        writer = csv.writer(file)
        writer.writerow(['Team name', 'Member name', 'Member email'])
        for league in self._leagues:
            for team in league.teams:
                for member in team.members:
                    writer.writerow([team.name, member.name, member.email])
