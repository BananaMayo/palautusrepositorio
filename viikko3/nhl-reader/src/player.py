import requests

class Player:
    def __init__(self, name, team, nationality, assists, goals, penalties):
        self. name = name
        self.team = team
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties


    def get_kansallisuus(self):
        return self.nationality

    def __str__(self):
        return f"{self.name:20} {self.team:2} {self.goals:2}+{self.assists:2} = {self.assists + self.goals:2}"


""" 

class Player:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name """