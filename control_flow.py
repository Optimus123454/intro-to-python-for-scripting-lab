# Problem 1: Vowel or consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and 
#   determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user in the above
#   messages.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels. You may need to look up
#   how to use this online.
# - Ensure your code provides feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    #Create Lists of vowels an consonants to check against
    vowelsUp = ("A","E","I","O","U")
    vowelsLow = ("a","e","i","o","u")
    consUp = ("B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z")
    consLow = ("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z")
    #Grab user input as letter
    letter = input("Input a letter here: ")
    #Check the letter status and provide output based on status
    if letter in vowelsUp or letter in vowelsLow:
       print("The letter ", letter, "is a Vowel!")
    elif letter in consLow or letter in consUp:
        print("The letter ", letter , " is a Consonant!")
    else: 
         print("Sorry what you gave me isn't a letter :(")
# Call the function
check_letter()



# Problem 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a
# user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative 
#   numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting
#   age.
# - Print a message indicating whether the user is eligible to vote based on the
#   entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure that you handle any 
#   conversion errors gracefully. You may need to look up how to do this online.
# - Use a conditional statement to check if the age meets the minimum voting age
#   requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    #Set voting age as a var
    minAge = 18
    #Grab user age from input
    age = int(input("Please enter your age :"))
    #Check valid age
    while age < 0:
        age =int(input("Your age can't be negative, please enter your age :"))
    #Check if user can vote
    if age < minAge:
        print("Sorry but you can't quite vote yet!")
    else:
        print("Congrats, you can Vote! Be sure to use this power wisely!")
# Call the function
check_voting_eligibility()




# Problem 3: Calculate dog years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's
# age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the
#   dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    #Grab dog's age from input
    dogAge = int(input("How old is your dog?"))
    #Set instance a variable for dog years
    peopleAge = 0
    #Conditional logic for calculating dog years
    while dogAge > 2:
        peopleAge = peopleAge +7
        dogAge -= 1
    while dogAge > 0:
        peopleAge = peopleAge + 10
        dogAge -= 1
    #Output the dogs age in dog years
    print(peopleAge)

# Call the function
calculate_dog_years()



# Problem 4: Weather advice
#
# Write a Python script named `weather_advice` that provides clothing advice
# based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle
#   multiple conditions.

def weather_advice():
    # Your control flow logic goes here
    
    #Make valid answer list
    yesOrNo = ("Yes","YEs","YES","yes","yES","yeS","No","NO","no","nO")
    
    #Make Yes list
    yesses = ("Yes","YEs","YES","yes","yES","yeS")
    
    #Make rain and cold booleans
    rainStatus = True
    coldStatus = True
    
    #Store rain data via input from user
    rain = input("Is it raining? (yes/no)")
    
    #Check for yes/no
    while rain not in yesOrNo:
        rain = input("Plese enter yes or no")
   
    #Store cold data via input from user
    cold = input("Is it cold? (yes/no)")
    
    #Check for yes/no
    while cold not in yesOrNo:
        cold = input("Please enter yes or no")

    #Give booleans value based on input
    if rain in yesses:
        rainStatus = True
    else: rainStatus = False
    if cold in yesses:
        coldStatus = True
    else: coldStatus = False

    #Give clothing advice based on weather
    if coldStatus and rainStatus:
        print("Wear a waterproof coat.")
    elif coldStatus and not rainStatus:
        print("Wear a warm coat.")
    elif not coldStatus and rainStatus:
        print("Carry an umbrella.")
    else: print("Wear light clothing.")
    
# Call the function
weather_advice()



# Problem 5: What's the season?
#
# Write a Python function named `determine_season` that figures out the season
# based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three
#   characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month:
#   "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in
#   <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure you validate the user's input and handle unexpected inputs
#   gracefully.

def determine_season():
    # Your control flow logic goes here
    #Make list of valid months
    valMonths = ("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec")
    #Make lists for months with only 1 season
    winterMonths = ("jan", "feb")
    springMonths = ("apr", "may")
    summerMonths = ("jul", "aug")
    fallMonths = ("oct", "nov")
    #Grab the current month from user input
    month = input("Please enter the current month as the first 3 letters of the month (Jan - Dec)").lower()
    #Check for valid month
    while month not in valMonths:
        month = input("Please enter a valid month").lower()
    #Grab the day of the month from user input
    day = int(input("Please enter the day of the month as a number"))
    #Check for valid day
    while day < 1 or day > 31:
        day = int(input("Please enter a valid day"))
    if month == "feb":
        while day > 28:
          day = int(input("Please enter a valid day"))
    elif month == "apr":
        while day > 30:
            day = int(input("Please enter a valid day"))
    elif month == "jun":
        while day > 30:
            day = int(input("Please enter a valid day"))
    elif month == "sep":
        while day > 30:
            day = int(input("Please enter a valid day"))
    elif month == "nov":
        while day > 30:
            day = int(input("Please enter a valid day"))

    #Use logic to output current season
    if month in winterMonths:
        print(month, " ", day, " ", "is in Winter")
    elif month in springMonths:
        print(month, " ", day, " ", "is in Spring")
    elif month in summerMonths:
        print(month, " ", day, " ", "is in Summer")
    elif month in fallMonths:
        print(month, " ", day, " ", "is in Fall")

    if month == "dec" and day > 20:
        print(month, " ", day, " ", "is in Winter")
    elif month == "dec" and day <= 20:
        print(month, " ", day, " ", "is in Fall")
    elif month == "mar" and day > 19:
        print(month, " ", day, " ", "is in Spring")
    elif month == "mar" and day <= 19:
        print(month, " ", day, " ", "is in Winter")
    elif month == "jun" and day > 20:
        print(month, " ", day, " ", "is in Summer")
    elif month == "jun" and day <= 20:
        print(month, " ", day, " ", "is in Spring")
    elif month == "sep" and day > 21:
        print(month, " ", day, " ", "is in Fall")
    else:
        print(month, " ", day, " ", "is in Summer")
# Call the function
determine_season()
