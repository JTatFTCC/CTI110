#Jonathon Thompson

#03/09/2024

#P2HW2

# This project will take the users grade and give the highest, lowest, sum, and average of the grades

inp = True
h_m = int(input('How many grades do you want to enter? '))
gr_list = []
txt = 'Grades'

while inp:
    grade = int(input('Enter your grade: '))
    if grade < 0 or grade > 100:
            print('Grade must be above 0-100.')
            inp = False
    else:
            gr_list.append(grade)
            h_m = h_m - 1
        
    if h_m == 0:
        inp = False

print(txt.center(20, "-"))

print('Highest Grade: ', end="")

print(max(gr_list))

print('Lowest Grade: ', end="")

print(min(gr_list))

print('Sum of Grades: ', end="")

print(sum(gr_list))

print('Average Grade: ', end="")

print(round(sum(gr_list)/len(gr_list), 2))
