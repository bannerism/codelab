
import math 
import pandas as pd

def rpm(n1,n2):
    halving = [n1]

    while(min(halving) > 1):
        halving.append(math.floor(min(halving)/2))

    doubling =[n2]
    while(len(doubling)< len(halving)):
        doubling.append(max(doubling)* 2) 

    half_double = pd.DataFrame(zip(halving,doubling))
    half_double = half_double.loc[half_double[0]%2 == 1,:]
    return sum(half_double.loc[:,1])

if __name__ == "__main__":
    n1 = 89
    n2 = 18
    print(rpm(n1,n2))
    