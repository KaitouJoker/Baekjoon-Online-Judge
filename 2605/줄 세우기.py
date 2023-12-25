input()
line   :list[int] = []
tickets:list[int] = [*map(int, input().split())]
for student, ticket in enumerate(tickets): line.insert(len(line) - ticket, student + 1)
print(*line)