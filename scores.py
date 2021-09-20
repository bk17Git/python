scores = []

for i in range(6):
    scores.append(int(input("Scores: ")))

average = sum(scores) / len(scores) 
print(f"The average is:  {average}")