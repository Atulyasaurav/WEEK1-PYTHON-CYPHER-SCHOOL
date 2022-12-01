#################################print function######################################################################################
print("hello world")
print('hello world')

print("hello'world' world")
print('hello"world"world')

''' we can't print the string using same ('' or "")'''
''' print("hello "world" atulya")'''
'''print('hello'world'atulya')'''

####################################escape sequences#########################################################################################
''' using of  same double quotes in python'''
print("hello \"world\" world")
print('atulya\'saurav\' abhisanchit')

'''new line escape sequences '''
print("atulya\nsaurav\nabhisanchit")

''' tab escape sequences'''
print("name\t atulya")

''' backlash'''
print('this is backlash\\')
print('this is double backlash\\\\')

'''backlash B(this act as a backspace'''
print("hell\blo")

#################################comment####################################################################################################
''' single line comment - #'''
''' multi line comment - (this is a comment)'''
''' shorcut (ctrl+/ - for single line comment)'''

#################################escape sequence as normal text in python#####################################################################
print("linea \\n lineb") 
print("linr\\tlineb")
print("this is 4 backslash\\\\\\\\ ")
#output:- \" \'
print('\\\" \\\'')

##################################exercise1 chapter1 ##########################################################################################
print("this is a \\\\ double backlash")
print("these are /\\/\\/\\/\\/\\")
print("he is \t awesome")
print("\\\" \\n \\t \\'")

################################## raw string in python###############################################################################################
print(r"atulya\n sauav")
print(r"atulya\t saurav")

##################################variable in python####################################################################################################
number1=2
print(number1)
number1= 4
print(number1)
'''string,number'''
name="atulya"
print(name)
name=123
print(name)
"""some rule to create a name"""
#alpha,numeric and underscore should only use
#no special charater should used- @atulya(invalid)
#we cant assign name by assinging starting by numeric- (1atulya)

#to seperate the two letter we use underscore -(atulya_saurav)
#for assing a constant variable we use an alphabet always in captial letter-(SCHOOL_NAME)
