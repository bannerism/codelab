## Euclid's Algorithm

def gcd(a:int,b:int)->int:
    """Use Euclid's Algorthim to find the GCD of two numbers

    Returns:
        int: the greatest commond divisor    
    """
    larger = max(a,b)
    smaller = min(a,b)
    remainder = larger % smaller
    
    if(remainder == 0):
        return(smaller)
    
    if(remainder != 0):
        return(gcd(smaller,remainder))

if __name__ == "__main__":
    a = 105
    b = 33
    print(gcd(a,b))

