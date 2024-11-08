

#1 uzdevums


integer_variable = 10          
float_variable = 3.14         
string_variable = "1 uzdevums!"    
boolean_variable = True        

print("vesela skaitlis:", integer_variable)
print("Peldes komats:", float_variable)
print("Строка:", string_variable)
print("Loģiska vērtiba:", boolean_variable)



#2 uzdevums



num1 = float(input("Ievad pirmu skaitlis: "))
num2 = float(input("ievad otru skaitlis: "))

sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2

if num2 != 0:
    division_result = num1 / num2
else:
    division_result = "uz nuli dalit nevar!"

print("summa:", sum_result)
print("Разность:", difference_result)
print("Произведение:", product_result)
print("Частное:", division_result)




#3 uzdevums


number = float(input("ievad skaitļu: "))

if number > 0:
    print("Число положительное.")
elif number < 0:
    print("Число отрицательное.")
else:
    print("Skaitlis ir nulle.")




#4 uzdevums


x=int(input("x:"))
y=int(input("y:"))
result1=(4**(y*3))+15y
print(result1)

x=int(input("x:"))
y=int(input("y:"))
result2=5y**x-144x+2/(x+y)**2
print(result2)

x=int(input("x:"))
y=int(input("y:"))
result3=(2+x)-(2*x*y))/y/(x+y)
print(result3)



# 5 uzdevums

 ifgrade < 0 or grade > 10:

grade = int(input("Введите оценку (целое число от 1 до 10): "))

    print("Ошибка: Оценка должна быть целым числом от 0 до 10.")
else:
   
    if grade >= 9:
        level = 'A'
    elif grade >= 7:
        level = 'B'
    elif grade >= 5:
        level = 'C'
    elif grade >= 3:
        level = 'D'
    elif grade >= 1:
        level = 'E'
    else:
        level = 'F'
    
    
    print("Уровень:", level)


