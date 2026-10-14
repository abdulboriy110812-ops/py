# number1 = int(input("Son 1 ni kiriting "))

# number2 = int(input("Son 2 ni kiriting "))

# operator = input("Operatorni ni kiriting ")


# if operator == "+":
#     print(number1 + number2)
# elif operator == "-":
#     print(number1 - number2)
# elif operator == "*":
#     print(number1 * number2)
# elif operator == "/":
#     print(number1 / number2)    




# student_score = [78, 92, 45, 100, 67, 92, 34, 81, 56, 100]


# student_count = 0
# student_sum = 0

# student_max = student_score[0]
# student_min = student_score[0]


# for i in student_score:

#       if i > student_max:
#          student_max = i
         
            
#       elif i < student_min:
#          student_min = i  



#       student_count+=1
#       student_sum+=i

# average = student_sum/student_count
# print(f"Studentlar soni {student_count}\nyigindi {student_sum}\nortacha {average}\nkatta {student_max}\nkichik {student_min}")



yosh = int(input("Yoshingizni kiriting:"))
ism = input("Ismingizni kiriting:")
vazn = float(input("Vazningizni kiriting:"))
dasturchi = input("Dasturchimisiz ha/yoq:")
loyihalar = []

while True:
    loyiha_nomi = input("Loyiha nomi yoki stop")

    if loyiha_nomi == "stop":
        break

    loyihalar.append(loyiha_nomi)

natija = f"Natija\n"
natija += f"Ism:{ism}\n"
natija += f"Yosh:{yosh}\n"
natija += f"Vazn:{vazn}\n"
natija += f"{True if dasturchi == "ha" else False}\n"
natija += f"Loyihalar{loyihalar}"

print(natija)
