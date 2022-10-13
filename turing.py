from turtle import xcor


x = 123456
reversedNum = 0


print("**********************")
print('x-->', x)
print('reversedNum-->', reversedNum)
print("**********************")


#########################################
reversedNum = reversedNum * 10 + x % 10
x = x // 10

print('--------------')
print('x-->', x)
print('reversedNum-->', reversedNum)
print('--------------')



#########################################
reversedNum = reversedNum * 10 + x % 10
x = x // 10

print('--------------')
print('x-->', x)
print('reversedNum-->', reversedNum)
print('--------------')
