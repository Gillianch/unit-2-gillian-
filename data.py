# x = 3
# y = float(3)
# print(x,y)




# values = [1,2.23,5,7,2,30,15]
# print(values)
# for i in values:
#     print(i) 

# print (values[0])
# print (values[6])






# x = "this is a thing"
# y= x.split()
# z = y[0]
# print(y)
# print(z)





#print("what is your sentence:")
#user enters sentence
#find number of spaces 
#add 1 to that number to find amt of words

# x = str(input("Enter a Sentence:"))
# print(x)
# y = x.split()
# print(y)
# print(len(y))





# day_of_week = input("What day is it?")
# if day_of_week == "Friday": 
#     print("correct")
# else:
#     print("incorrect")





# x = "test"
# print(f"hello {x}")






# temp = 68
# if temp > 68:
#     print('warm')
# elif temp == 68:
#     print('perfect')
# else:
#     print('cold')





# number = int(input("What is your number?"))
# int 
# if number % 2 == 0:
#     print('even')
# if number % 2 == 1:
#     print('odd')





# bill = 45
# service = input("How was the service?")
# if service == "bad":
#     print (bill)
# if service == "okay":
#     print (bill * 1.15)
# if service == "good":
#     print (bill * 1.2)
# if service == "great":
#     print (bill * 1.25)





# x = int(input("Enter a number"))

# for i in range(1, x + 1):
#     if x % i == 0:
#         print(i)




x = int(input("Give me your first value"))
y = int(input("Give me your second value"))


for i in range(1, min(x,y) + 1):
    if x % i == 0 and y % i == 0:
        gcf = i

print(gcf)