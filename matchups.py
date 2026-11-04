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
