print("(dealing with is vs == )".center(45,'*').capitalize())

print(True ==1)
print(True=='1')
print(True==' ')
print(True==True)

print('True is True ',True is True)
print('True == True ',True == True)
print('True is False ',True is False)
print('False is False ',False is False)

print(1==1.0)    # true 
print(' '=='\0')  # false
print([]==()) #  false 
print('1'==1) # false
print((1,2,3)==[1,2,3]) # false
print((1,2,3)==(1,2,3)) # true
print([1,2,3]==[1,2,3]) # true
print([1,2,3]==(1,2,3)) # false  

print('next secton \n\n')
print([1,2,3] is [1,2,3]) # false because stored on different loacations

a=[1,2,3]
b=[1,2,3]
c=(1,2,3)
print('a is b ',a is b)    # false
print('a == b ',a == b) # true 
print('a is a ',a is a)   # true
print('a ==c ',a == c)   # false different data types (list and tuple)



