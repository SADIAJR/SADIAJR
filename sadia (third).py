import random

choices =('r','s','p')

while True:
 user_choice = input('Rock,paper or Scissors?(r/p/s):').lower()
 if user_choice not in choices:
   print ('invalid choice')


 computer_choice = random.choice(choices)


 print (f'you chose {user_choice}')
 print (f'computer chose {computer_choice}')

 if user_choice == computer_choice:
   print('Tie!')    
 elif (
   (user_choice == 'r' and computer_choice == 's')or
   (user_choice == 's' and computer_choice == 'p')or
   (user_choice == 'p' and computer_choice == 'r')):
   print('you win')
 else:
   print('you lose')


 should_continue = input('continue? (y/n):').lower()
 if should_continue == 'n':
   break



  






