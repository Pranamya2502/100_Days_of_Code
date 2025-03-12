rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
import random
print("what do you choose,type 0 for rock, 1 for paper and 2 for scissors")
user=int(input())
random_no= random.randint(0,2)
if user>= 0 and user <= 2:
    print(game_images[user])
print("computer chooses rock, paper or scissors")
if random_no==0:
    print(game_images[random_no])
elif random_no==1:
    print(game_images[random_no])
elif random_no==2:
    print(game_images[random_no])

if user==0 and random_no==0:
    print("tie")
elif user==1 and random_no==0:
    print("user win")
elif user==2 and random_no==0:
    print("user lose")
elif user==0 and random_no==1:
    print("computer win")
elif user==1 and random_no==1:
    print("tie")
elif user==2 and random_no==1:
    print("computer lose")
elif user==0 and random_no==2:
    print("user win")
elif user==1 and random_no==2:
    print("computer win")
elif user==2 and random_no==2:
    print("tie")
else:
    print("invalid input")


