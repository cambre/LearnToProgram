__author__ = 'Cambre'

highest_score = 0
results_f = open("results.txt")
for line in results_f:
    (name, score) = line.split()
    if float(score) > highest_score:
        highest_score = float(score)
results_f.close()
print("The highest score was:")
print(highest_score)