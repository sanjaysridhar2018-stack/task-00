def is_prime(n):
    if n<2:
        return("False")
    for i in range(2,n):
        if n%i==0:
           return("False")
    else:
        return("True")
        

a= int(input("enter the number to be tested"))       
print(is_prime(a))