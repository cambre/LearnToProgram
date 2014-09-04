__author__ = 'Cambre'
scores =[]
highest_score = 0
results_f = open("results.txt")
for line in results_f:
    (name, score) = line.split()
    scores.append(float(score))
results_f.close()
scores.sort()
scores.reverse()
print("The top scores were:")
print(scores[0])
print(scores[1])
print(scores[2])