# name = input("enter your name:")
# print("wellcome",name)
# name =( input("enter your name:"))
# age = (input("enter your age:"))
# price =(input("enter youe price:"))
# print("well come", name)
# print("your age is",age)
# print("your price is",price)
# print(type(name))
# print(type(age))
# print(type(price))


# marks = int(input("enter your marks:"))
# if(marks >=90):
#     print("grade A")
# elif(marks >= 80 and marks < 90):
#     print("grade B")
# elif(marks >= 70 and marks < 80):
#     print("grade C")
# else:
#     print("grade D")
# student =["sohail",95.5, 56,"gp"]
# print(student[0])
# student[0]="ali"
# print (student)
# list = [34,45,67,89,89,45,34,35]
# (list.append(5))
# print(list)
# list =  [3,2,1]
# (list.sort())
# print (list)
# list = ['a','b','c','d']
# list. reverse()
# print (list)
# list = [1,2,3,4,5,6,]
# list.insert(4,4)
# list = [1,2,3,4,5,6,7,9]
# list.pop(3)
# print (list)
# tup = (1,2,3,4,5,6,7)
# print (type(tup))
# print (tup[0])
# print(tup[2])
# tup = (1,2,3,4,5,6,7,8,9,7)
# print (tup[1:3])
# tup = (1,2,3,4,5,2,7,2)
# print (tup.count(2))
# tup = (1,3,2,3,4,5,6,7,)
# print(tup.index())


# """1.....bill generator"""
# # product price 
# product = float(input("Enter your product price:"))
# # product quantity
# quantity = int(input("Enter product quantity:"))
# subtotal = product+quantity
# # Total Tax
# tax = subtotal*.10
# # Final Total bill
# Final_Total_Bill= subtotal+tax

# print("\n-------finalbill-------")
# print("Product Price:", product)
# print("Quantity of Product:", quantity)
# print("Tax:", tax)
# print("Final Bill:", Final_Total_Bill)


"""1..... 2nd method 
                        bill generator"""


# product = float(input("Enter your product price:"))
# quantity = int(input("Enter product quantity:"))
# total = product*quantity
# # discount = 0
# # discount rule
# if total >  10000 :
#     discount = total*0.20
# elif total < 2000:
#     discount = total*0.10
# subtotal = total - discount 
# tax = subtotal * 0.10
# totalbill = subtotal+tax
# print("\n-------final bill-------")
# print("total :", total)
# print("discount:", discount)
# print("amount after discount:", subtotal)
# print("tax:", tax)
# print("Final Payable Bill:", totalbill)

# print("Welcome to Shope Billing System")
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
total = price*quantity
# discount rule
if total > 10000: 
    discount = total*0.20
elif total < 2000:
    discount = total*0.10

subtotal = total - discount
# tax 12%
tax = subtotal * 0.12
final_bill = subtotal + tax
print("\n-------BILL RECEIPT-------")
print("Total amount:", total)
print("Discount:", discount)
print("Amount after discount:", subtotal)
print("Tax:", tax)
print("Final Payable Bill:", final_bill)
