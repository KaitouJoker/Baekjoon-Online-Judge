line, _, tickets = [], input(), list(map(int, input().split()))
for student, ticket in enumerate(tickets):
    line.insert(len(line) - ticket, student + 1)
print(*line)