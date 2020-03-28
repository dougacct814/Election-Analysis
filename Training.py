

name = 'Jacob Deming'
country = 'United States'
age = 25
hourly_wage = 15
satisfied = True
daily_wage = ([hourly_wage * 8])

print("Hello, " + name + "!")
print("You live in " + country)
print("You are " + str(age) + " years old")
print(f"You make {daily_wage} per day")
print(f"Are you satisifed with your current wage? {satisfied}")



#* Create a Python list to store your grocery list as a list of strings. You need to buy:
 #   * Milk
  #  * Bread
  #  * Eggs
  #  * Peanut Butter
 #   * Jelly

grocerylist = ['Milk', 'Bread', 'Eggs', 'Peanut Butter', 'Jelly']

# Print out the list
print()
print(grocerylist)
# Wait! Your cousin is visiting next week, and they’re allergic to peanuts! Change “peanut butter” in the list to “almond butter”.
grocerylist[3] = 'Almond Butter'
print(grocerylist)
# You just remembered that you have homemade jam that your neighbor made for you. Remove “jelly” from the list.

grocerylist.remove('Jelly')
print(grocerylist)

# You just used up the last of your coffee. Add “coffee” to your grocery list.
grocerylist.append('Coffee')
# Print out the updated list.
print(grocerylist)

print()



# Create a dictionary that will store the following:
  # Your name
  # Your age
  # A list of a few of your hobbies
  # A dictionary of a few days and the time you wake up on those days


# Print out your name, how many hobbies you have and a time you get up during the week.

# Dictionary full of info
my_info = {"name": "Rex",
           "occupation": "dog",
           "age": 21,
           "hobbies": ["barking", "eating", "sleeping", "loving my owner"], #List
           "wake-up": {"Mon": 5, "Friday": 5, "Saturday": 10, "Sunday": 9}} #Nested Dictionary
#Print out results are stored in the dictionary

print(f'Hello I am {my_info["name"]} and I am a {my_info["occupation"]}')
print(f'I have {len(my_info["hobbies"])} hobbies!')
print(f'On the weekend I get up at {my_info["wake-up"]["Saturday"]}')


print()

#Prompt the user for what video they are looking for.
# Search through the netflix_ratings.csv to find the user’s video.
# If the CSV contains the user’s video then print out the title, what it is rated and the current user ratings.
# For example: 'Grease is rated PG with a rating of 86'

# Bonus:

#Insert a break statement into the for loop to stop the loop when the first movie is found to stop duplicated results. See the [documentation](https://docs.python.org/3.6/reference/simple_stmts.html#break) for additional info.
#If the CSV does not contain the user’s video then print out a message telling them that their video could not be found.
#_______________________________________SOLUTION_____________________________________
# Modules
import os
import csv

#Prompt user for video lookup
video = input("What show or movie are you looking for? ")
#Set path for file
#csvpath = os.path.join("..", "Resources", "netflix_ratings.csv")  #USE THIS TO GO UP A LEVEL
#csvpath = os.path.join("..", "Resources", "netflix_ratings.csv") ANOTHER EXAMPLE
csvpath = os.path.join("Resources", "netflix_ratings.csv") 
# Bonus
# ------------------------------------------
# Set variable to check if we found the video
found = False
# Open the CSV

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    # Loop through looking for the video
    for row in csvreader:
        if row[0] == video:
            print(row[0] + " is rated " + row[1] + " with a rating of " + row[5]) #FIRST - SECOND AND SIXTH COLUMNS

            # BONUS: Set variable to confirm we have found the video
            found = True

            # BONUS: Stop at first results to avoid duplicates
            break

    # If the video is never found, alert the user
    if found is False:
        print("Sorry about this, we don't seem to have what you are looking for!")



#___________________WRITE TO FILE___________________________________
# Dependencies
import os
import csv

# Specify the file to write to
output_path = os.path.join("output", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

    # Write the second row
    csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])


#_______________________LIST COMPREHENSIONS________________________________________


cats = ['Siamese', 'Abyssinian', 'Shorthair', 'Bengal']
illegal_in_hawaii = 'Bengal'

#transform cats to the subset of legal breeds with list comprehension

legal_cats = [cat for cat in cats if cat != illegal_in_hawaii]
print(legal_cats)



# ~ is used for home direcotry
# # mkdir output
# Make directory and it will go into it with mkdir &&




#__________________________________________________PYPOLL BACKUP

# Add Dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties in the election\n-----------------------\nArapahoe\nDenver\nJefferson")



# Total number of votes cast


# Get total number of votes


# List all candidates who got a vote


# Update percentage of each votes the candidates won


# Total number of votes for each candidate


# Winner of election


# Close the file

election_data.close()

