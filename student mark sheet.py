marks = [] 

for i in range(5):
    num= int(input("Enter mark {}: ".format(i + 1)))
    marks.append(num)
print("marks for five subject", marks)
Totalmarks=0
for i in marks:
    Totalmarks += i
print("sum of five subject:",Totalmarks)
percentage=Totalmarks*100/500
print("percentage of student:",percentage)
if(percentage>90):
    print("Grade 0")
elif(percentage>70 and percentage<90):
    print("Grade A")
elif(percentage>50 and percentage<70):
    print("Grade B")
elif(percentage>35 and percentage<50):
    print("Grade C")
else:
    print("Fail")
    reappear_decision = input("Do you want to reappear for the exam? (yes/no): ").lower()
    if reappear_decision == "yes":
        print("You have opted to reappear for the exam.")
    else:
        print("You have chosen not to reappear for the exam.")



