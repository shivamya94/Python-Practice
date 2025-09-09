Lis1= [ "yes" if i%2==0 else "no" for i in range(10) ]
print(Lis1)
Lis2= [i for i in range(10)]
print(Lis2)

#Write a  Python program to sum all the items in a list. 
List = [ 1,2,3,4,5,6]
sum = 0

for i in List:
  sum = sum + i 

print(sum)

# Write a Python program to get the largest number from a list.

def largest_num (numbers):
  return max(numbers)


my_List = [23,12,56,78,90]
print("The largest number is:", largest_num(my_List))

#Write a Python program to clone or copy item in a list.

My_List = [2,3,4,6,7,5]
My_List2 = My_List.clear()

print(My_List2)

#Write a Python program to access the index of an element present in a list.

Listt3 = [4,5,2,6,7,8,9,12]

