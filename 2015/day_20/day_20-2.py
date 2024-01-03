import math

def find_factors(x):
   low_devisors = [i for i in range(1, int(math.sqrt(x))+1) if x%i == 0]
   high_devisors = [x / i for i in low_devisors if x != i *i]
   return low_devisors + high_devisors


puzzle = 34000000
_ = 460000
value = [0]
while 10* sum(value) < puzzle:
    value = find_factors(_)
    value = [i for i in value if _/i <= 50]
    if 11*sum(value) >=  puzzle:
        print(_, sum(value))
    _ += 1
    



