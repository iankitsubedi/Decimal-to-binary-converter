num = []
a = int(input("Enter a number in decimal number system: "))

while a > 0:
    x = a % 2 
    num.append(x)
    a = a // 2

num.reverse()
print("The number in binary system is :")
for i in num:
    print(i,end = ' ')