import random
import matplotlib.pyplot as plt

n = 5

# plot true distribution
def population():
    PDF = [0]
    PDF.append(1/n)
    for x in range(2, n+1):
        PDF.append(1/(x*(x-1)))

    CDF = [0]
    CDF.append(1/n)
    for x in range(2, n+1):
        CDF.append(1/n + 1 - 1/x)
    plt.plot(PDF)
    # plt.plot(CDF)
    

# plot sampled distribution
def sample():
    choices = list(range(1, n+1))
    print(choices)
    CDF = []
    CDF.append(1/n)
    for x in range(2, n+1):
        CDF.append(1/n + 1 - 1/x)
    print(CDF)
    PDF = [0]*(n+1)
    trials = 100
    for _ in range(trials):
        uni = random.random()
        point = choices[0]
        for i in range(n-1):
            if CDF[i] < uni < CDF[i+1]:
                point = choices[i+1]
        PDF[point] += 1/trials
    plt.plot(PDF)

population()
sample()
plt.show()
        


