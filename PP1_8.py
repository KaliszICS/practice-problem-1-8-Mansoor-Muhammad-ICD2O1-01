'''
Lesson: Boolean Logic 
Author: Mansoor Muhammad 
Date Created: sept 26, 2024
'''
def q1():
  bool1 = True
  bool2 = False
  print(bool1 and bool2)


def q2():
  weed = input("Enter an integer: ")
  weed = int(weed)
  print(weed != 0)

   




def q3():
  education = input("Enter a number: ")
  print(education >= 0 and education <= 10)
  

def q4():
  food = input("Input food: ")
  drink = input("Input drink: ")
  print(not food == "pizza" or not drink == "pop")

def q5():
  integer = input("Enter an integer: ")
  print(f"The integer {integer} is {integer % 2 == 0}")

#Do not edit code after this
#Comment out the followwing code when running tests
'''
q1()
q2()
q3()
q4()
q5()
'''