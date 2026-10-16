# for i in range(1,100):
#     if i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:       
#         print("Buzz")
#     elif i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     else:
#         print(i)




# student_score = [78, 92, 45, 100, 67, 92, 34, 81, 56, 100]


# student_count = 0
# student_sum = 0

# student_max = student_score[0]
# student_min = student_score[0]



# for i in student_score:

#      student_sum+=i
#      student_count+=1

#      if i >= 90:
#       print("A")
#      elif i >= 70:
#       print("B")  
#      elif i >= 60:
#       print("C")
#      else:    
#       print("D") 
      

#       if i > student_max:
#          student_max = i
         
            
#       elif i < student_min:
#          student_min = i  


       # average = student_sum/student_count
# print(f"Studentlar soni {student_count}\nyigindi {student_sum}\nortacha {average}\nkatta {student_max}\nkichik {student_min}")




student_ismlar = ["eldorbek","shukurjon","asadbek"]

student = input("ISm kiriting")

if student in student_ismlar:
    print("SIz kiritgn ism mavjud",student)
else:
    student_ismlar.append(student)
    print("List: ",student_ismlar)    



def studentlar_korsatish(student_ismlar):
     return student_ismlar   
   
def student_ochirish(user2,student_ismlar):
    student_ismlar.remove(user2)    

def student_qoshish(user3,student_ismlar):
    student_ismlar.append(user3)  

def student_indek_orqali_qoshishh(i,user4,student_ismlar):
    student_ismlar.insert(i,user4)    

student_ismlar = ["eldorbek","shukurjon","asadbek"]

while True:
    print("# 1. student ismlar ro'yhatini ko'rish \n2. ism olib tashlash \n3. yangi ism qo'shish(oxiriga) \n4. yangi ism qo'shish(aynan bir indexga) insert \n5. stop")   
    user1 = int(input("Kiriting:"))
    if user1 == 1:
     print("Student ismlar royxati",studentlar_korsatish(student_ismlar))
    elif user1 == 2:
      user2 = input("Qaysi ismni olib tashlamoqchisiz:")
      
      if user2 in student_ismlar:
         student_ochirish(user2,student_ismlar)
         print("SIz kiritgan ism olib tashlandi:",user2)
      else:
         print("Bunday ism arrayda mavjud emas")   

    elif user1 == 3:
      user3 = input("Qaysi ismni qoshmoqchisiz:")
      student_qoshish(user2,student_ismlar)
      print("SIz kiritgan ism arrayga qoshildi",student_ismlar)
    elif user1 == 4:
      user4 = input("Qaysi ismni qoshmoqchisiz:")
      i = int(input("Qaysi indexga qoshmoqchisiz:"))
      student_indek_orqali_qoshishh(i,user4,student_ismlar)
      print("SIz kiritgan ism arrayga qoshildi",student_ismlar)
    elif user1 == 5:  
         print(student_ismlar)
         print("Tizim tugadi")
         break
    else:
       print("siz notogri son kiritingiz")


