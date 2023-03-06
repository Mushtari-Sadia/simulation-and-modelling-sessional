import sys
import numpy as np
np.random.seed(2)

class MonteCarlo:

    def __init__(self,generations):
        self.n = generations
        self.count = np.zeros((self.n,5))
        self.set_probabilities()

    def p(self,n):
        if n<0:
            print("invalid n")
            return 0
        elif n==0:
            return 0.4825
        else:
            return (0.2126)*(0.5893)**(n-1)

    def set_probabilities(self):
        self.probabilities = [self.p(i) for i in range(5)]
        self.probabilities[0] = 1-sum(self.probabilities[1:4])

    def get_number_of_children(self):
        probabilities = self.probabilities
        r = np.random.uniform(0,1)
        for i in range(len(probabilities)):
            if r < probabilities[i]:
                return i
            r -= probabilities[i]
        return len(probabilities)-1

    def get_leaves(self,i):
        num_of_children = self.get_number_of_children()
        if i==0:
            return num_of_children
        
        leaves = 0
        for j in range(num_of_children):  
            leaves += self.get_leaves(i-1)
        return leaves

    def run_simulations(self,simulations):
        for i in range(simulations):
            for generation in range(self.n):
                leaves = self.get_leaves(generation)
                if leaves<5:
                    self.count[generation][leaves] += 1
    
    def print_result(self):
        for i in range(self.n):
            print("\n\nNumber of generations ",i+1,":")
            for j in range(5):
                print("Probability of ",j,"neutrons:",self.count[i][j]/sum(self.count[i]))

if __name__ == "__main__":
    try:
        generations = int(sys.argv[1])
    except:
        generations = 3
    monte_carlo = MonteCarlo(generations)
    monte_carlo.run_simulations(10000)
    monte_carlo.print_result()
