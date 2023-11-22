#Strings
#first_name = "Grace"
#last_name = "Hall"
#full_name = "Grace Hall"
#print("hello " + full_name)



#Integers
#age = 21
#age += 1
#print("Your age is: "  +str(age))

#float
#height = 250.5

#print("Your height is: "+str(height)+ "cm")
#print(type(height))

#bool
#human = True
#print("are you a human: "+str(human))
#print(type(human))



#multiple assignment = allows us to assign multiple variables at the same time in one line of code
# name = "Grace"
#age = 16
#attractive = True

#name, age, attractive = "Grace", 16, True

#print(name)
#print(age)
#print(attractive)

#Spongebob = Patrick = Sandy = Squidward = 30
#print(Spongebob, Patrick, Sandy, Squidward)


#name = "Grace"

#print(len(name))
#print(name.find("r"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isalpha())
#print(name.count("r"))
#print(name.replace("r", "a"))
#print(name*3)



#type casting = convert the date type of a value to another data type.

#x = 1 #int
#y = 2.0 #float
#z = "3" #string

#int(y)
#z = int(z)
#x = float(x)
#y = str("Y is: "+str(y))
#print(x)
#print(y)
#print(z*3)



#input = input is user created strings or variables to add to your program

#name = input("What is your name?: ")
#age = int(input("How old are you?: "))
#height = float(input("How tall are you?: "))

#age = age 

#print("Hello "+name)
#print("You are "+str(age)+" years old")
#print("You are "+str(height)+"cm tall")



#import math

#pi = 3.14
#x = 1
#y = 2
#z = 3


#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi, 2))
#print(round(pi))
#print(math.sqrt(pi))
#print(max(x, y, z))
#print(min(x, y, z))

  
#slicing = create a substring by extracting elements from another string
#                       indexing [] or slice()
#                        [start:stop:step]
#Python will assume if your start bracket is missing, the value is equal to 0. 
#If stop is missing, it will assume it is the end of the string
    
#name = "Grace Hall"

#first_name = name[:5]
#last_name = name[6:]
#funky_name = name[0:10:2]
#reversed_name = name[::-1]

#print(reversed_name)

#website = "http://google.com"
#website2 = "http://wikipedia.com"

#slice = slice(7, -4)

#print(website[slice])
#print(website2[slice])


# if statement = a block of code that will execute if it's condition is true

#age = int(input("How old are you?: "))

#if age == 100:
#    print("You are a century old!")
#elif age >= 18:
#    print("You are an Adult!")
#elif age < 0:
#    print("You haven't been born yet!")
#else:
#    print("You are a child!")



#logical operators (and, or, not) = used to check if two or more conditional statements is true
#in and statements, both conditions must be fufilled in order to be true

#temp = int(input("What is the tempature outside?: "))
#if temp >= 0 and temp <= 30:
#    print("The temparature is good today")
#    print("go outside")
#elif temp == 69:
#    print("Nice.")
#elif temp < 0 or temp > 30:
#    print("The temparture is bad today")
#    print("Stay inside")



#while loop = a statement that will execute it's block of code, as long as it's condition remains true



#name = ""

#while len(name) == 0:
#    name = input("Enter your name: ")

#print ("Hello "+name)


#import time
#for loop = a statement that will execute it's block of code a limited amount of times
# while loop = unlimited
# for loop = limited

#for i in range(10):
#    print(i+1)

#for i in range(50, 100+1,2):
#    print(i)

#for i in "Grace Hall":
#    print(i)

#for seconds in range(10, 0, -1):
#    print(seconds)
#    time.sleep(1)
#print("Happy new years!")



# nested loops = the "inner loop" will finsih all of it's iterations before finsihing one interation of the outer loop


#rows = int(input("How many rows?: "))
#columns = int(input("How many columns?: "))
#symbol = input("Enter a symbol to use: ")

#for i in range(rows):
#    for j in range(columns):
#        print(symbol, end="")
#    print()

