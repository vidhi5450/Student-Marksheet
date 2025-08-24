sub1 = int(input("Enter subject 1 mark="))
sub2 = int(input("ENter subject 2 mark="))
sub3 + int(input("ENter subject 3 mark="))

total = sub1+sub2+sub3
per = total/3

if(sub>=40 and sub2>=40 and sub3>=40)
  if(per>=80):
    grade = "distinction"
  elif(per>=60):
       grade = "first"
  elif(per>40):
       grade = "second"
else:
  grade = "fail"
print("subject 1 marks =",sub1)
print("subject 2 marks =",sub2)
print("subject 3 marks =",sub3)
print("total =",total)
print("percentage =",per)
print("Grade =",grade)
