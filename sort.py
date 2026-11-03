teams = [
    ("Arsenal", 70, 25, 65),
    ("Liverpool", 70, 25, 60),
    ("Chelsea", 70, 20, 55)
]

def get_ranking(team):
    return (team[1], 
            team[2],
            team[3]
            )

result = sorted(
    teams,
    key=get_ranking,
    reverse=True
)

print(result)
