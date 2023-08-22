#rock paper scissors
import random

def gamewin(comp, you):
    if comp == you:
        return None
    
    elif comp=='r':
        if you== 's':
            return False
        elif you== 'p':
            return True
    
    elif comp=='p':
        if you== 'r':
            return False
        elif you== 's':
            return True
    
    elif comp=='s':
        if you== 'p':
            return False
        elif you== 'r':
            return True
         
print("Computer's Turn: Rock(r) Paper(p) or Scissor(s)? ")
randno= random.randint(1, 3)
if randno== 1:
    comp='r'
elif randno== 2:
    comp='p'
elif randno== 3:
    comp='s'
    
you= input("Your Turn: Rock(r) Paper(p) or Scissor(s)? ")
a= gamewin(comp, you)      

print(f"Computer Chose {comp}")
print(f"You Chose {you}")

#any of this declaration works

# if a== None:
#     print("The game is a Tie!")
# elif a:
#     print("You Win!")
# else:
#     print("You Lose!")
if a== None:
    print("The game is a Tie!")
elif a== True:
    print("You Win!")
elif a== False:
    print("You Lose!")
    
