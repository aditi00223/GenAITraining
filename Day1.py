# # a = int(input("Enter a number: "))
# # string = input("Enter a string: ")
# # float = float(input("Enter a float number: "))
# # d = a + float
# # print("The sum of the integer and float is:", d)

# # temp = a
# # a= float
# # float = temp
# # print("The value of a after swapping is:", a)
# # print("The value of float after swapping is:", float)

# # a = a + float
# # float = a - float
# # a = a - float
# # print("The value of a after swapping back is:", a)
# # print("The value of float after swapping back is:", float)

# # # write a program display grading sytem based on marks obtained by a student
# # # rule based grading system
# # maths = int(input("Enter marks obtained in Maths: "))
# # science = int(input("Enter marks obtained in Science: "))
# # english = int(input("Enter marks obtained in English: "))
# # hindi = int(input("Enter marks obtained in Hindi: "))
# # total_marks = (maths + science + english + hindi) / 4
# # if total_marks >= 90:
# #     print("Grade: A")
# # elif total_marks >= 80:
# #     print("Grade: B")
# # elif total_marks >= 70:
# #     print("Grade: C")
# # elif total_marks >= 60:
# #     print("Grade: D")
# # else:
# #     print("Grade: F")


# # # loops 

# # for i in range(5):
# #     print("This is iteration number:", i + 1)

# # for i in range(1, 11,2):
# #     print("This is odd number:", i)



# # zip function
# roll_numbers = [1, 2, 3, 4, 5] 
# name = ["Alice", "Bob", "Charlie", "David", "Eve"]
# courses = ("Maths", "Science", "English", "Hindi")
# for roll, n, course in zip(roll_numbers, name, courses):
#     print("Roll Number:", roll, "Name:", n, "Course:", course)

# # for loop 
# sum = 0
# product = 1
# for i in range(1,6):
#     sum += i
#     product *= i
# print(sum)
# print(product)

# # que
# for i in range(1,22):
#     if i % 2 == 0:
#         print(i, "is even")
#fibonacci series

n1 = 0
n2 = 1
n3 = n1 + n2
print(n1)
print(n2)
for i in range(2, 10):
    n1 = n2
    n2 = n3
    n3 = n1 + n2
    print(n3)

# reverse number using while loop
#armstrong number
# prime number
# palindrome number

