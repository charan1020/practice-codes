def sum_even_odd(arr):
    even_sum = 0
    odd_sum = 0
    for num in arr:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return even_sum, odd_sum
arr= list(map(int,input().split()))
even, odd = sum_even_odd(arr)
print("sum of even numbers:",even)
print("sum of odd numbers:",odd)