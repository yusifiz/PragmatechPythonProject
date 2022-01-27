# Recursive Algorithm

## Factorial (non-tail)

def factorial(x):

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 3
print("The factorial of", num, "is", factorial(num))


## Fibonacci numbers

def recursive_fibonacci(n):
   if n <= 1:
       return n
   else:
       return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))
   
n_terms = 10
   
if n_terms <= 0:
   print("Invalid input ! Please input a positive value")
else:
   print("Fibonacci series:")
   for i in range(n_terms):
       print(recursive_fibonacci(i))

## Recursive function exapmle

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)