arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:

def sum_odds(sum):
    adder = 0
    for i in range(len(sum)):
        if sum[i]%2 != 0:
            adder+=sum[i]
    return adder

print(sum_odds(arr))
