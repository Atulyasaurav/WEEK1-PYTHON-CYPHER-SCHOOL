#############################################string concatenation######################################################
#SSfirst_name ="ATULYA"
#SSlast_name="SAURAV"
#SSfull_name=first_name+" "+last_name
#sprint(full_name)
#print(full_name+3) ->  ERROR
#print(full_name+"3") -> NO ERROR
#print(full_name+str(3))-> NO ERROR
#SSprint(full_name*2)
##############################################input function####################################################################
#input function
#SSname=input("ENTER YOUR NAME ")
#SSprint("HELLO"+name)
#string 
#SSage = input("what is yout age")
#SSprint("your age is"+age)
#int function
#SSnum_one=int(input("enter your first num"))
#SSnum_two=int(input("enter your second num"))
#SStotal=num_one+num_two
#SSprint("total is",total)
#str
# 4 ---> "4"

#int
#"4" ---> 4.0
###############################################more about varibale#######################################
#SSname,age="atulya",str(34)
#SSprint("hello im "+name+"your age is"+age)

#SSx=y=z=1
#SSprint(x,y,z,"=",x+y+z)
###############################################two or more intup in one line#####################################
#split()
#SSname,age=input("enter your name and age").split(",")
#SSprint(name)
#SSprint(age)
#################################################string fornating#########################################################
#SSname = "atulya"
#SSage =34

#python3\
#print("hello{}your age is{}".format(name,age+2))

#python3.6
#SSprint(f"hello{name}your age is{age+2}")

##################################################exercise - 1 ##############################################################
#SSnum1 = int(input())
#SSnum2 = int(input())
#SSnum3 = int(input())
#SSaverage = (num1+num2+num3)/3
#SSprint(average)
####################################################string indexing############################################################
#SSname = "python"
#SSp = 0,-6
#SSy = 1,-5
#SSt = 2,-4
#SSh = 3 ,-3
#SSo = 4,-2
#SSn = 5,-1
#SSprint(name[4])
#######################################################slicing###############################################################
#[starting argument:stop argumrnts]
#SSname = 'ATULYASAURAVABHISANCHIT'
#SSprint(name[2:6])
#SSprint(name[1:8])
#SSprint(name[0:])
#SSprint(name[:23])
#SSprint(name[-8:-4])
#SSprint(name[::-1])
#################################################### EXERCISE - 2 ##############################################################
#SSNAME = input("enter your name ")
#SSprint(NAME[::-1])
#################################################string method part 1############################################################
#SSname = "atulya saurav abhisanchit"
# len() function
#SSprint(len(name))

#lower() method
#SSprint(name.lower())


#upper()method
# ssprint(name.upper())

#titteL() method
# ssprint(name.title())

# count() method
# ssprint(name.count("y"))
################################################### exercise = 3 ####################################################
#SSnaam,chr = input("enter your name and a chr ").split()
#SSprint(len(naam))
#SSprint(naam.lower().count(chr.lower()))
#################################################### strip method ##########################################
#left strip
name = "        atulya          "
dots = "............."
print(name.lstrip()+dots)
print(name.rstrip()+dots)
print(name.strip()+dots)
##############################################replace and find method ###############################################
#replace
string = "atulya saurav abhisanchit is a best "
print(string.replace(" ","_",1))

#find
print(string.find("is",18))
is_pos1 = string.find("is")
is_pos2 = string.find("is",is_pos1+1)

###################################################center method########################################################
name = "atulya"
print(name.center(8,"*"))
name = input("enter your name: ")
print(name.center(len(name)+8,"*"))

#######################################################string immutablel####################################################
string = "abhisanchit"
new_name = string.replace("i","A")
print(new_name)

####################################################assignment operator###############################################3
a = 5
b = 7
a += b
print(a)
a -= b
print(a)
a *= b
print(a)




