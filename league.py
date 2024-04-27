# league.py #
# Patrick Parks #
# Auburn University #
# CPSC 4790 #
# 3/24/24 #

from identified_object import IdentifiedObject
from exceptions import DuplicateEmail, DuplicateOid
from team_member import TeamMember
from team import Team
from competition import Competition
import datetime

class League(IdentifiedObject):
    
    @property
    def teams(self):
        return self._teams
    
    @property
    def competitions(self):
        return self._competitions
    
    def __init__(self, oid, name):
        super().__init__(oid)
        self.name = name
        self._teams = []
        self._competitions = []
    
    def add_team(self, team):
        if team not in self.teams:
            self.teams.append(team)
        else:
            return None

    def remove_team(self, team):
        if team in self.teams and team not in self.competitions:
            self.teams.remove(team)
        else:
            raise ValueError
        
    def team_named(self, team_name):
        for team in self.teams:
            if team.name == team_name:
                return team
        else:
            return None
    
    def add_competition(self, competition):
        if competition not in self.competitions:
            self.competitions.append(competition)
        else:
            raise ValueError

    def teams_for_member(self, member):
        member_teams = []
        for team in self.teams:
            if member in team.members:
                member_teams.append(team)
        return member_teams
    
    def competitions_for_team(self, team):
        team_competitions = []
        for competition in self.competitions:
            if team in competition.teams_competing:
                team_competitions.append(competition)
        return team_competitions
    
    def competitions_for_member(self, member):
        member_competitions = []
        for competition in self.competitions:
            for team in competition.teams_competing:
                if member in team.members:
                    member_competitions.append(competition)
        return member_competitions
    
    def __str__(self):
        print(f"{self.name}: {len(self.teams)} teams, {len(self.competitions)} competitions")
    

    