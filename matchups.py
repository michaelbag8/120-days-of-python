def generate_matchups(teams):
    matchup = []
    for i in range(len(teams)):

        for j in range(i+1, len(teams)):

            matchup.append(f"{teams[i]} vs {teams[j]}")

    return matchup
