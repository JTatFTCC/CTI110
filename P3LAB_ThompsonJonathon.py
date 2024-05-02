#Jonathon Thompson

#3/17/2024

#P3LAB1

#This project will determine if the year you input is a leap year


year = input('Input your year:')

if (int(year) % 4 == 0 and int(year) % 100 != 0) or (int(year) % 400 == 0 ): 
    print (f"{year} is a leap year.") 
    
else : 
    print(f"{year} is not a leap year.")
