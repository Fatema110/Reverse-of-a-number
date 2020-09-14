"""
REVERSE OF A GIVEN NUMBER
"""

n=int(input(" enter the number to be reversed "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number ",rev)

OUTPUT-
enter the number to be reversed 21
Reverse of the number  12
