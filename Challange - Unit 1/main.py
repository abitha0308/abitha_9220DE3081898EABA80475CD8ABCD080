
def fact(n):
    if n==0 or n==1:
      return 1
    else:
        return n * fact(n-1)
num=int(input("Enter the Number: "))
result=fact(num)
print("The Factorial value {} is {}." . format(num,result))
