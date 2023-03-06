import sys
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)

try :
    n = int(sys.argv[1])
except :
    n = 100
    print("running for default value of n = 100")

array_s = [1,3,5,10]

simulations = 10000

success_rates = np.zeros((len(array_s),n))

for s in array_s:
    for i in range(simulations):
        for m in range(1,n):
            #uniform sampling
            rank = np.random.uniform(0,1,n)
            
            #taking m samples
            m_samples = np.random.choice(rank, m, replace=False)
            rest = np.array([x for x in rank if x not in m_samples])
            
            #setting the criteria
            criteria = np.max(m_samples)

            #getting the best candidate
            selected_candidate = 0
            for j in range(len(rest)):
                selected_candidate = j
                if rest[j] >= criteria:
                    break
            
            #checking if strategy was successful
            descending_rank = np.sort(rank, axis=-1, kind='quicksort', order=None)[::-1]
            top_s = descending_rank[:s]

            if rest[selected_candidate] in top_s:
                success_rates[array_s.index(s)][m] += 1
    
    success_rates[array_s.index(s)] = success_rates[array_s.index(s)]/simulations

#plotting the success rates
plt.clf()
for s in array_s:
    plt.plot(range(1,n), success_rates[array_s.index(s)][1:])
    plt.legend(array_s, title = "s", loc = 'upper right')
plt.title("A Simulation of The Marriage Problem")
plt.xlabel('Size of Sample(m)')
plt.ylabel('Success Rate')
plt.show()
plt.savefig('success_rate.png')

                
        

