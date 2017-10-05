row = [1,2,3,4]

# [] --> []
def computeNextRow(currentrow):
    factor = 2
    nextrow = [currentrow[0] + 1]
    for i in row[1:]:
        nextrow = nextrow + [(currentrow[0] + 1) * factor]
        factor = factor + 1

    return nextrow

currentrow = row
for i in row:
    print(currentrow)
    nextrow = computeNextRow(currentrow)
    currentrow = nextrow
