import random

print("Welcome to rock papar scissors game!!");
print("Game loading......\n");
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

options = ["Rock","Paper","Scissors"];
option_list = [rock,paper,scissors];

# User_choice!
human_input = int(input("For 🪨 (Rock) press 1\nFor 📃(Paper) press 2\nFor ✂️ (Scissors) press 3\nEnter your choice: "))
human_choice = human_input - 1;
print("\n\nUser choosed:")
print(option_list[human_choice])
print("\n")


# Computer_Choice;
computer_choice = int(random.randint(0,2));
print(f"Computer choosed:\n{option_list[computer_choice]}");


#Logic
# options = ["Rock","Paper","Scissors"];

if (human_choice) == (computer_choice):
  print("It's a Draw")

elif (human_choice == 0) and (computer_choice == 2):
  print("User won!")

elif (human_choice == 0) and (computer_choice == 1):
  print("Computer won")

elif (human_choice == 1) and (computer_choice == 0):
  print("User won")

elif (human_choice == 1) and (computer_choice == 2):
  print("Computer won")

elif (human_choice == 2) and (computer_choice == 0):
  print("Computer won")

elif (human_choice == 2) and (computer_choice == 1):
  print("User won")

