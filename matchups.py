def generate_matchups(teams):
    matchup = []
    for i in range(len(teams)):

        for j in range(i+1, len(teams)):

            matchup.append(f"{teams[i]} vs {teams[j]}")

    return matchup

def group_players_by_team(players):
    grouped_players = {}

    for player in players:
        team = player["team"]
        name = player["name"]

        if team not in grouped_players:
            grouped_players[team] = []

        grouped_players[team].append(name)

    return grouped_players


def total_goals(players):
    team_goals = {}

    for p in players:
        team_goals.setdefault(p["team"], 0)
        team_goals[p["team"]] += p["goals"]

    return team_goals


def top_scoring_team(players):
    goals = total_goals(players)
    if goals:
        return max(goals.items(), key=lambda item: item[1])
    return None

def top_scoring_teams(players):
    goals = total_goals(players)
    highest = max(goals.values(), default=0)
    return [
        (team, total)
        for team, total in goals.items()
        if total == highest
    ]
