def patrol_bounds(positions):
    # rows = [row for row, col in positions]
    # cols = [col for row, col in positions]
    positions = positions[0]
    rows, cols = zip(*positions)
   
    return [min(rows),max(rows), min(cols), max(cols)]

Input=[[[1,3],[4,1],[2,5]]]
print(patrol_bounds(Input))

inputs=[[[2,2]]]
print(patrol_bounds(inputs))


def active_names(roster):
    words = []
    for empty_entry in roster:
        if len(empty_entry) != 0:
            words.append(empty_entry)
    return words


print(active_names(["Ada","","Tunde","","Halima"]))

#["Ada","Tunde","Halima"]


def long_names(roster, min_length):
    return [valid_names for valid_names in roster if len(valid_names) >= min_length ]

 def total_paces(n):
    total = 0
    if n == 0:
        return total

    for i in range(1,n+1):
        total += i
    return total

print(total_paces(2))


def count_sightings(report):
    count = 0
    for mark in report:
        if mark == "X":
            count += 1
    return count

def cadence_sum(n):
    total = 0
    for pace in range(3, n+1, 3):
        total += pace
    return total

print(cadence_sum(8))

def screen_visitor(name, pass_code, escort):
    if len(name) == 0:
        return "no name"
    if len(pass_code) == 0:
        return "no pass"
    if pass_code.startswith("X"):
        return "deny"
    if pass_code.startswith("R") and not escort:
        return "needs escort"
    return "admit"


def after_hours_admit(pass_color, hour):
    if pass_color == "red":
        return "deny"
    elif pass_color == "amber":
        return "hold"
    elif pass_color == "green" and  6 <= hour < 22:
        return "admit"
    elif pass_color == "green":
        return "admit with escort"
    else:
        return "verify"


def signal_report(callsign, strength):
    return f"{callsign:>8} | {strength * 100:.1f}%"

inc, a = ["HAWK",0.073]
ins, b = ["EAGLE",0.5]

print(signal_report(inc, a))
print(signal_report(ins, b))

def add_recruit(roster, name):
    roster.append(name)
    return roster
    

roster = ["A","B"]

print(add_recruit(roster, "C"))

def rotate_roster(roster):
    if len(roster) <=0:
        return roster.copy()
    new_roster = roster[1:] + roster[:1]
    return new_roster


print(rotate_roster(["Ada","Tunde","Halima"]))
#["Tunde","Halima","Ada"]
