quiz = {
    "Python kis year launch hua?": "1991",
    "Python ka founder?": "Guido",
}

score = 0
for q, a in quiz.items():
    ans = input(q + " ")
    if ans.lower() == a.lower():
        score += 1

print("Score:", score)
