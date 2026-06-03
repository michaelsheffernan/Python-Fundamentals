scores = [89, 50, 45, 67, 23, 41, 87, 90, 100, 92, 96, 56, 23, 30]

passing_scores = filter(lambda scores: scores >= 40, scores)

converted_grades = list(map(lambda score: "A" if score >= 90 else "B" if score >=
                        75 else "C" if score >= 60 else "D" if score >= 40 else "E", passing_scores))

print(converted_grades)
