for i in range(1,100):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:       
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)




student_score = [78, 92, 45, 100, 67, 92, 34, 81, 56, 100]


student_count = 0
student_sum = 0

student_max = student_score[0]
student_min = student_score[0]



for i in student_score:

     student_sum+=i
     student_count+=1

     if i >= 90:
      print("A")
     elif i >= 70:
      print("B")  
     elif i >= 60:
      print("C")
     else:    
      print("D") 
      

      if i > student_max:
         student_max = i
         
            
      elif i < student_min:
         student_min = i  


       

      
      

average = student_sum/student_count
print(f"Studentlar soni {student_count}\nyigindi {student_sum}\nortacha {average}\nkatta {student_max}\nkichik {student_min}")

