# Functions go here

def yes_no(question):

     # Checks user response to a question is yes/no (y/n); returns "yes" or "no"

     while True:

          response = input(question).lower()

          # check the user says yes or no
          if response == "yes" or response == "y":
               return "yes"
          elif response == "no" or response == "n":
               return "no"
          else:
               print("Please enter yes / no")

# Main Routine

want_instructions = yes_no("Do you want to see the instructions? ").lower()
want_coffee = yes_no("Do you want coffee? ").lower()

print("We done")