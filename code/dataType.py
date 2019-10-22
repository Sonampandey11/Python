'''
data type in python
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview

'''

#working with numeric type
#long is deprecated in python 3.0
#float holds precising value up to 15 is correct
def numFunc() :
    num1 = 2
    num2 = 3.5
    num3 = 6j
    print("Value of num1",type(num1))
    print('convert int to string', str(num1))
    print('find the value of num1', type(num1))
    print('value of num2 ====float', type(num2))

numFunc();


#working with sequence type in python
#list ----list is similar to array to hold data types ['one','two','three'...]
#the main difference is that we can hold unsimilar data in list example

def seqFun() :
     a = [1, 2, 3, 'one','apple', 2.3]
     print (type(a),'Define type of a') #list
     print(a[1]) #index are 0 based. this will print a single character  == 2
     print ( type(a[5]), 'it will print float value for 2.3')

seqFun();

# working with touple datatype
# touple is similar to list the main difference is that we cannot change the value i.e. they are immutable
# also we use () instead of []

def toupleFun() :
    num1 = (1,2,3,4,0,'sonam')
    tup2 = (1, 2, 3, 4, 5, 6, 7 );
    print (tup2[1:5], "value between 1 to 5 is tup2[1:5]")
    print (num1)

    #Tuples are immutable which means you cannot update or change the values of tuple element
    
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print (tup3);
    

toupleFun()


