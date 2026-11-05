def calculate_team_goals(players):
    players_goals = {}

    for p in players:
        players_goals.setdefault(p["team"], 0)
        players_goals[p["team"]] += p["goals"]
  
    return players_goals

def total_players(players):
    team_counts = {}

    for p in players:
        team_counts.setdefault(p["team"], 0)
        team_counts[p["team"]] += 1
  
    return team_counts
    

def calculate_average_goals_per_team(players):
    team_goals = calculate_team_goals(players)
    team_counts = {}

    for p in players:
        team_counts.setdefault(p["team"], 0)
        team_counts[p["team"]] += 1
    
    return {team: team_goals[team] / count for team , count in team_counts.items()}


print(calculate_average_goals_per_team(teams))