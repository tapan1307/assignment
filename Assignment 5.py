
print('Task 1')

student_marks={"Alok":80,"Alice":85,"Bruce":95,"Catherene":75,"Deep":92,'Eric':90}
student=input('Enter the student\'s name :')
marks=student_marks.get(student)
if student in student_marks:
    print(student,"\'s marks is :",marks)
else:
    print('Student is not found')

print('Task 2')
original_list=[1,2,3,4,5,6,7,8,9,10]
nums=(original_list[:5])
print('Extracted Numbers:',nums)
reverssed_nums=nums[::-1]
print('Extracted Reversed Numbers:',reverssed_nums)