val1 = 'good'
def createFun() :
    val1 = 'fantastic'
    print('Python is' + val1)  #Python isfantastic

createFun()

print('Python is last updated ' + val1) #Python is last updated good
       
#working with python variable

def globalFunc() :
    global val2
    val2 = 'workdone'

globalFunc()

print ('To declare varibale we can work with global attribute' + val2) #To declare varibale we can work with global attributeworkdone


# working with string and integer

def addNumber() :
    num1 = 1
    num2 = '5'
    print("Add num1 and num2", str(num1) + num2) #convert as string 15

addNumber()



#working with subtract - keyword

def subNumber() :
    num1 = 8
    num2 = 5
   # print(str(num1) -num2, 'subtraction of two number'); #it will throw error in python as - is not suppoeted in string
    print((num1) -num2, 'subtraction of two number')
subNumber();
