def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
num_input = int(input("Enter a number: "))
global num
fact_num = factorial(num_input)
print(f"Factorial of {num_input} is: {fact_num}")