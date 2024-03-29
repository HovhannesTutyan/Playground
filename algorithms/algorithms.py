# def gridTraveler(m, n, memo = {}):
#     key = (m, n)
#     if key in memo:
#         return memo[key]
#     if m == 1 and n == 1:
#         return 1
#     if m == 0 or n == 0:
#         return 0
#     memo[key] = gridTraveler(m - 1, n, memo) + gridTraveler(m, n - 1, memo)
#     return memo[key]

# print(gridTraveler(18,15))


# def fib(n, memo={}):
#     key = n
#     if key in memo:
#         return memo[key]
#     if n <= 2:
#         return 1
#     memo[key] = fib(n-1, memo) + fib(n-2, memo)
#     return memo[key]

# print(fib(10))

# def canSum(targetSum, numbers, memo={}):
#     if(targetSum in memo):
#         return memo[targetSum]
#     if(targetSum == 0):
#         return "true"
#     if(targetSum < 0):
#         return "false"
#     for num in numbers:
#         reminder = targetSum - num
#         if canSum(reminder, numbers, memo) == "true":
#             memo[targetSum] = "true"
#             return "true"
#     memo[targetSum] = "false"
#     return "false"
   
# print(canSum(7, [2,4]))

# def howSum(targetSum, numbers):
    
# ////////////////////////////////// Power of a number /////////////////////////////////////
def power (base, exp):
    if (exp == 1):
        return (base)
    if (exp != 1):
        return (base * power(base, exp - 1))
    
base = int(input ("Enter the base"))
exp = int (input ("Enter the exponent"))
print ("The result is: ", power(base, exp))

