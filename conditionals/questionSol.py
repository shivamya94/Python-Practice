#Write a program to take input from user his age ,name , marks and show output 
#1. name in opposite direction (reversed)
#2. age as how many years are left in turning 100
#3. marks as how much are they out of 100(percentage)

a = int(input("enter age"))
b = input("enter name")
c = int (input("enter marks"))
l = []

a1 = a[::-1]
b1 = 100-a
c1 = c/100
l.append[a1,b1,c1]
print (l)
