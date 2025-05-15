# Functions go here

def yes_no(question):

     # Checks user response to a question is yes/no (y/n); returns "yes" or "no"

     while True:

          response = input(question).lower()

          # check the user says yes, no, y or n
          if response == "yes" or response == "y":
               return "yes"
          elif response == "no" or response == "n":
               return "no"
          else:
               print("Please enter yes / no")

def instructions():
     # Prints instructions

     print(""" 
*** Instructions ***

Roll the dice and try to win!      
      """)

def int_check():
    # Checks users enter an integer more than / equal to 13

    error = "Please enter an integer more than / equal to 13."

    while True:
        try:
            response = int(input("What is the game goal? "))

            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
           print(error)

# Main Routine

# testing loop...

want_instructions = yes_no("Do you want to see the instructions? ").lower()

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
     instructions()

print()
game_goal = int_check()
print(game_goal)