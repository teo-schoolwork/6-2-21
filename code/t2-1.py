score = 0
over100 = 0

while score != -1:
    score = int(input("Enter your score, Enter -1 to exit\n : "))

    if score >= 100:
        over100 += 1

print(f"Exited. You had {over100} scores over 100.")
