__author__ = 'Cambre'
scores =[]
names =[]
results_f = open("results.txt")
for line in results_f:
    (name, score) = line.split()
    scores.append(float(score))
    names.append(name)
results_f.close()
scores.sort()
scores.reverse()
names.sort()
names.reverse()
print("The top scores were:")
print(names[0] + ' with ' + str(scores[0]))
print(names[1] + ' with ' + str(scores[1]))
print(names[2] + ' with ' + str(scores[2]))
