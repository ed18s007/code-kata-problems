#A Simple Hello World
print("Hello World")

#Getting input via STDIN
userInput = input()
print("The Input Provided is: " + userInput)
a,b = map(int, userInput.split())
prod = 1
while a>b:
    prod *= a
    a-=1
print(prod)
