from random import randint

# input text: "Enter the minimum/maximum number: "
min_number = int(input("Enter the minimum number: "))
max_number = int(input("Enter the maximum number: "))

# image: (-it) to run the container in interactive mode with a terminal.
# docker run -it python-app-starting-setup:0.0.1
# container: attach (-a) to the container, but it's not working it properly, so we need to use this option with the interactive mode (-i).
# docker start -a -i gifted_edison
if (max_number < min_number):
    print("The maximum number must be greater than the minimum number.")
else:
    random_number = randint(min_number, max_number)
    print(f"The random number between {min_number} and {max_number} is: {random_number}")