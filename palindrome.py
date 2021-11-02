num = int(input("Enter a value:"))
Temp = num
sum = 0
while(Temp > 0):
    dig = Temp % 10
    sum = sum * 10 + dig
    Temp = Temp // 10
if(num == sum):
    print("This value is a palindrome number!")
else:
    print("This value is not a palindrome number!")