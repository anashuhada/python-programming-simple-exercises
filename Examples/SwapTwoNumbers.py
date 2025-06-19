# a = 10
# b = 20

a = input("Enter a value: ")
b = input("Enter b value: ")

print("Value of a before swapping:", a)
print("Value of b before swapping:", b)

# Approach 1
# temp = a # 10
# a = b # 20
# b = temp # 10

#Approach 2
a, b = b, a

print("Value of a after swapping:", a)
print("Value of b after swapping:", b)