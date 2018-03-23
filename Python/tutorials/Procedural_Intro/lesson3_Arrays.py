###ARRAYS'''

#this program will store several values in an array,
#and then print each one to the screen

array = [4,5,6,7,8,9]

print("Print the items in order manually:")
print(array[0])
print(array[1])
print(array[2])
print(array[3])
print(array[4])
print(array[5])

print("Print the items in order using a loop:")
for i in array:
    print(i)


for i in range(0,11):
    print(i)

print("Print the items in order, a different way:")
for i in range(0, len(array)):  #i goes through 0, 1, 2, 3, 4, 5
    print(array[i])

print("Print the items backwards:")
for i in range(0, len(array)):
    print(array[len(array) - 1 - i])
