number1 = int(input("Son 1 ni kiriting "))

number2 = int(input("Son 2 ni kiriting "))

operator = input("Operatorni ni kiriting ")


if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)    




student_score = [78, 92, 45, 100, 67, 92, 34, 81, 56, 100]


student_count = 0
student_sum = 0

student_max = student_score[0]
student_min = student_score[0]
studnet_max_count = 0

for i in student_score:

      if i > student_max:
         student_max = i
         studnet_max_count +=1   
            
      elif i < student_min:
         student_min = i  



      student_count+=1
      student_sum+=i

average = student_sum/student_count
print(f"Studentlar soni {student_count}\nyigindi {student_sum}\nortacha {average}katta {student_max}\neng katta sining soni {studnet_max_count}\nkichik {student_min}")

