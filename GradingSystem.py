print("                 Grading System\n")
Eng = int(input("Enter English Marks :"))
Kis = int(input("Enter Kiswahili Marks :"))
Math = int(input("Enter Mathematics Marks :"))
Sci = int(input("Enter Science Marks :"))
Cre = int(input("Enter CRE Marks :"))
mean = (Eng + Kis + Math + Sci + Cre) / 5

if mean >= 80:
  print("Your Grade is A of Points", mean)
elif mean >= 70 and mean < 80:
  print("Your Grade is B+ of Points", mean)
elif mean >= 60 and mean < 70:
  print("Your Grade is B of Points", mean)
elif mean >= 50 and mean < 60:
  print("Your Grade is B- of Points", mean)
elif mean >= 40 and mean < 50:
  print("Your Grade is C+ of Points", mean)
elif mean >= 30 and mean < 40:
  print("Your Grade is D of Points", mean)
elif mean < 30:
  print("Your Grade is E of Points", mean)
else:
  print("Enter Valid Marks!")
