# a = [1,2,3,4,5,6,7,8,9,9,]
# print(a)
# print(type(a))
# print(len(a))
# a[0]= 2
# print(a)
# marks = [2,3,5,4,6,7,8,9]
# print (marks)
# print(len(marks))
# print(type(marks))
# print(marks[1:4])
# marks.append(91)
# print(marks)
# marks.sort()
# print(marks)
# marks.remove(2)
# print(marks)
# marks.reverse()
# print(marks)
# marks.insert(2,55)
# print(marks)
# marks.pop(5)
# print(marks)
# tup = (1,2,3,4,5,6)
# print(type(tup))
# print(tup.index(2))
# print(tup.count(1))
# dict = {
#     "name" : "sohail",
#     "marks" : "34",
#     "city" : "lahore"
# }
# dict["name"] = "ali"
# print(dict)
# set1 = {1,2,2,3,4,5,6,7,8}
# set2 = {1,2,2,3,4,5,6,7,8}
# print(set)
# print(len(set))
# print(type(set))
# set.add(10)
# print(set)
# set.remove(4)
# print(set)
# set.clear()
# print(set)
# i = 1
# while i <= 100:
#     print(i)
#     i += 1 
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1 
# i = 1 
# while i <= 10:
#     print(10*i)
#     i += 1
# num = [1,4,9,16,25,36,49,64,81,100]
# indx =  0 
# while indx < len(num):
#     print(num [indx])
#     indx += 1
# i = 1
# while i <= 100 :
#     print("sohail",i)
#     i += 1
# i = 1 
# while i <= 100 :
#     print(i)
    # i += 1
# i 
# i = 1 
# while i <= 10:
#     print(i*10)
#     i += 1
# num = [1,5,6,4,9,6,3,8,]
# idx = 0 
# while idx < len(num):
#     print(num[idx])
# #     idx += 1
# hero = ("ali","sohail", "rashid")
# idx = 0 
# while idx < len(hero):
#     print(hero[idx])
#     idx += 1
# num = (1,9,4,9,3,9,8,9)
# x = 9                                                                                            
# i = 0   
                                                                                          
# while i < len(num):
#    if num[i] == x:
#     print("found at idx:",i)
#    else :  
#      print("finding")
#    i += 1    
  
'''.............'''
# heros = ("ali","sohail","azaz","muzmmil","saim",)
# # x = "saim"
# i = 0 
# while i < len(heros):
#     if heros[i]== x :
#         print("str found at :",i)
#     else :
#         print("not found")
#     i += 1
# while i < len(heros):
#     print(heros[i])
#     i  += 1

# list = [ 1,2,3,4,5]
# for el in list :
#     print(el)
# else :
#     print("end")


# list = ( 1,2,3,4,5,6,7,8,9,0)
# x = 9
# idx = 0
# for el in list :
#     if el == x :
#         print("found at the idx ",idx)
#     print(el)
#     idx += 1

# a = (1,2,3,4,5,6,7,8,9)
# for el in range (5) :
#     print(el)



# for el in range (2,10,2):
#     print(el)

# for el in range (100,0,-1):
#     print(el)
# a = int(input("enterthe number:"))
# for el in range (1,11):
    
#     print(a * el)


# for el in range(10):
#     pass


# n = 10 
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print("total sum =",sum)

# def print_hello ():
#     print_hello = ()
#     print("hello")

# a = print_hello ()
# a = print_hello ()
# a = print_hello ()
# a = print_hello ()
# a = print_hello ()
# a = print_hello ()


# a = (1,2,3,4,5,6,78,9)

# def print_len(list):
#    print_len (list)

# def print_len(list ):
#   for item in list:
#       print(item, end ="")
# print_len (a)



# def calu_fact (n):
#     fact = 1
#     for i in range (1, n+1):
#      fact *= i 
#     print(fact)
# print(calu_fact (5))   



# print(calu_fact (10)) 
  
# def converter(usd_valu):
#     inr_valu = usd_valu * 83
#     print(usd_valu, "USD =", inr_valu, "INR" )
# converter(100)


# def show(n):
#   if(n == 0):
#     return
#   print(n)
#   show(n-1) 

# print(show(10))


# def show (n):
#     if (n == 0):
#       return
#     print(n)
#     show (n -1)
# (show(10))


# def fact(n):
#  if(n == 0 or n == 1):
#   return 1 
#  else:
#   return n * fact (n-1)

# print(fact(5))

# def clac_sum (n):
#   if(n == 0):
#      return 0 
#   return clac_sum (n-1) + n

# print(clac_sum(5))



# def print_list (list,indx= 0):
#     if (indx == len(list)) :
#         return
#     print(list[indx])
#     print_list( list,indx + 1)
# a = [1,3,4,5,6,7,8,9]
# (print_list(a))

# f = open("text.py" , "w") 
# f.close () 

class Student:
    def __init__(self,fullname):
        self.name = fullname
        print("creating new students in data bases")
s1 = Student("sohail")
print(s1.name)
# print(s1.name)
# s2 = Student()
# print(s2.name)
# class car:
#     colour = "belu"
#     modle = "sounta"
# car1 = car()
# print(car1.colour)
# print(car1.modle)






















