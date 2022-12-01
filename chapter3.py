##################################if statement#######################################
#SSage = int(input("enter your age : "))
#SSif age > 18:
 #SS   print("you can start the game")

#################################### pass statement#############################################
#SSx = 50
#SSif x > 19:
#SS    pass

    #################################### else statement########################################
#SSage = int(input("enter your age : "))
#SSif age >= 18:
#SS    print("you can start the game")
#SSelse:
#SS    print("ypu can't play the game")
########################################### exercise = 3 #############################################3
# '''winning_number = 8
# guess_number = int(input("GUESS A NUMBER btw 1 TO 10 : "))
# a = guess_number
# if a == 8 :

#     print(" YOU WON !!")
# else:
#     if a>8:
#         print("to high!!")
#     else:
#         print("too low!!")
  
#   ######################################### and & or operation #########################################################
# # AND ---> if both are true

# name = "agent001"
# password = 143
# #SSif name == "agent001" and password == 143:
# #SS    print("welcome back major")
# #SSelse:
# #SS    print("get out of from here")

# # OR ---->  if one statement is true then true, if both false the false
# #SSif name == "agent001" or  password == 144:
# #SS    print("welcome back major")
# #SSelse:
# #SS    print("get out of from here")

# ######################################### exercise = 2 ####################################################################
# user_name = input("enter your name : ")
# age = int(input("enter your age : "))
# x= user_name
# y = age
# if y >= 10 and x[0] == "a" or x[0] == "A":
#     print("you can watch the movie")
# else:
#     print("you are under age")'''

############################################# if / else / elif ####################################################################
# age = int(input("ENTER YOUR AGE : "))
# if age <= 3 :
#     print("ticket price is free ")
# elif age <= 10 and age >= 4:
#     print("ticket price is 150")
# else:
#     print("ticket price is  250")

####################################################### python in keywords######################################################################
# name = "atulya"
# if "a" in name :
#     print("a is present")
# else:
#     print("a is not present")

# ######################################################### CHECK_EMPTY OR nOT ################################################################
# name = "atgl"
# if name:
#     print("name is",name)
# else:
#     print("name is empty")

################################################################# LOOP ####################################################################
# WHILE LOOP
# i = 1
# while i<=10:
#     print("hello major")
#     i += 1

####################################################### sum of numbers program using while loop ########################################################
# sum 1 to 10 :
# total = 0
# i = 1
# while i <= 10 :
#     total += i
#     i += 1
# print(total)

##############################################################EXERCIE - 3 ##################################################################################
# a = int(input("enter your numb : "))
# total = 0
# i = 1
# while i <= a:
#     total += i
#     i += 1
# print(total)

################################################################ EXERCISE - 4 #######################################################################
# numb = input("ENTER YOUR NUMBER : ")
# total = 0
# i = 0
# while i < len(numb):
#     total += int(numb[i])
#     i += 1
# print(total)
################################################################### EXERCISE - 5 ################################################################################
# name = input("enter your name : ")
# temp = ""
# i = 0  
# while i < len(name):
#     if name[i] not in temp :
#         print(name[i],':', name.count(name[i]))
#     i += 1
################################################################### INFINITE LOOP ########################################################################################
#while True:
  #  print("hi")

#####################################################################  FOR LOOP  ##############################################################################################
# for i in range(10):
#     print(i,":","hi")
 
for i in range(6,11):
    print(i,":","hi")