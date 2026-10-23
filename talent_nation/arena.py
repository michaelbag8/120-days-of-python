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