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