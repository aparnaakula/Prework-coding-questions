""" Question 1 
Write a function to print "hello_USERNAME!" USERNAME is the input of the 
function. The first line of the code has been defined as below.
"""
def hello_name(user_name):
    if user_name.casefold() == 'quit':
       print ("Thank you for registering")
    else:
       print("hello_"+ user_name +"!")
user_name = input("Please enter your name")
name = hello_name(user_name)

"""Question 2
Write a python function, first_odds that prints the odd numbers from 1-100 and 
returns nothing
"""
def first_odds(number):
        list_range =[]
        for i in number:
             if i%2!=0 & i<=100:
                 list_range.append(i)
        print (list_range)
number = range(1,101)
first_odds(number)
    
"""            
Question 3
Please write a Python function, max_num_in_list to return the max number of a given list. 
The first line of the code has been defined as below.
"""
def max_num_in_list(a_list):
   max = a_list[0]
   for i in a_list:
       if i > max:
           max = i
   return max
a_list =[20,50,90,100]
print("Largest Element is " , max_num_in_list(a_list))
                
"""         
Question 4
Write a function to return if the given year is a leap year. A leap year is divisible by 4, 
but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).  def is_leap_year(a_year):
 """       
def leap_year(year):
   return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
year = int(input("Enter a year: "))
print(leap_year(year))


"""Question 5
Write a function to check to see if all numbers in list are consecutive numbers. 
For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
The return should be boolean Type.
"""

def is_consecutive(a_list):
    sorted_list = sorted(a_list)
    range_list=list(range(min(a_list), max(a_list)+1))
    print(bool(sorted_list == range_list))
    
a_list=[8,5,2,3,6,4,7]
is_consecutive(a_list)
