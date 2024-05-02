



import random



def math_quiz(x, y, qt):
    
    global ans
    global count

    while qt != 2:
        y = random.randint(1, 1000)
        x = random.randint(1, 1000)
        print('Menu')
        print('1 for Addition')
        print('2 for Subtraction')
        print('3 to Stop')
        qt = int(input())

        
        if qt == 1:
            while (ans != x + y):
                print(y)
                print("+", x)

                ans = int(input('What is the solution? - '))
                if ans == x + y:
                    print('You are correct!')
                    print('Your guesses:', count + 1)
                    break

                else:
                    print('You are incorrect, try again')
                    count += 1
                    
        elif qt == 2:
            while (ans != y - x):
                print(y)
                print("-", x)

                ans = int(input('What is the solution? - '))
                if ans == y - x:
                    print('You are correct!')
                    print('Your guesses:', count + 1)
                    break

                else:
                    print('You are incorrect, try again')
                    count += 1

        else:
            print('Thanks for playing!')
            break
            

ans = 0
count = 0
x = 0
y = 0
qt = 0



math_quiz(y, x, qt)






