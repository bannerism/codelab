def halving(larger):
    halving = []
    while larger > 0:
        halving.append(larger)
        larger = larger // 2
    return halving

def double(smaller):
   return smaller * 2

def doubling(smaller, left):
    doubling = []
    for i in range(len(left)):
        doubling.append(smaller)
        smaller = double(smaller)

    return doubling

def sum_odd_halving(halvings, doublings):
    candidates = list(zip(halvings, doublings))
    to_sum = []
    for c in candidates:
        if c[0] % 2:
            to_sum.append(c[1])

    return to_sum

def rpm(n1:int, n2:int)-> int:
    """RPM, Russian Peasant Multiplication
    
    Multiply two numbers by halving the larger number and doubling the smaller

    Args:
        n1 (int): number to multiply
        n2 (int): second number to multiply

    Returns:
        int: the product of n1 * n2
    """
    values = [n1, n2]
    larger = max(values)
    smaller = min(values)
    left = halving(larger)
    right = doubling(smaller, left)
    return sum(sum_odd_halving(left, right))

if __name__ == "__main__":
    n1 = 89
    n2 = 17
    result = rpm(n1, n2)
    assert result == n1 * n2
    print(result)
