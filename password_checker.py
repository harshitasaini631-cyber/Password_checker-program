import random
import string

def password_strength(password): #function defined. Takes one argument i.e, (password)
    score = 0 #starting point is 0 of the score
    suggestions = [] #empty list to store suggestions of how strong a assword should be.
    
    #To check length of the password
    if len(password) >= 12:
        score += 2 #if greater than 12 or equal then it will add +2 to the score
    elif len(password) >= 8:
        score += 1 #if greater than 9 or equal then it will add +1
    else:
        suggestions.append("Use at least 8 characters or more") #append -> to add an element to the end of a list. suggestions is an empty list. It will print else condition if the password is shorter than 8.
        
     
     # to check uppercase   
    has_upper = False

    if any(c.isupper() for c in password):
            score += 1 #checks if any character is uppercase, if yes then adds +1 to score and if not then it will execute else statement.
    else:
     suggestions.append("Add at least one uppercase letter.")
     
     
    #to check if password contains lowercase 
    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")
    
    
    #to check if password contains digit check
    if any(c.isdigit() for c in password):
            score += 1
    else:
        suggestions.append("Add at least one number.")
        
    #to check for any special character
        # Special character check
    if any(not c.isalnum() for c in password): #isalnum checks if a character is alphanumeric . (A-Z or digit 0-9)
        score += 2 #is alnum is true if c is a letter or number. not c isalnum true if it doesnt contain any letter or number. not is what makes it to check for special characters.
    else:
        suggestions.append("Add at least one special character (!, @, #, $, etc.).")
    
    
    #fnal score
    score = max(0,min(score,8)) #score will be b/w 0 and 8 only. wont be more as score itself starts from 0 , so its basically 0-8.
    #max 0 to make sure its not negative
    
    
    #To check the strength level
    if score <= 2:
        strength = "Very Weak"
    elif score <= 4:
        strength = "Weak"  
    elif score <=6:
        strength = "Moderate"      
    elif score == 7:
        strength = "Strong"    
    else:
        strength = "Very Strong"    
        
    return{
        "password" : password, #returns with original password
        "score" : score, #returns number score
        "strength" : strength, #returns thestrength
        "suggestions" : suggestions if suggestions else ["Strong Password"] #returns suggestions if password is weak , if not then returns strong passsword.
    }  

#program to generate strong password.
  
def password_generate(length=12):
    letters = string.ascii_letters #prints abc...ABC
    numbers = string.digits #prints 012345...    
    symbols = string.punctuation #prints !@#$%...

    all_char = letters + numbers + symbols
    password = "" #empty string to store the new genrated password

    for i in range(length):
        password = password + random.choice(all_char) #choose random choice od symbols, words and numbers to generate new password.
    return password    

password = input("Enter a password:")  #input by user
result = password_strength(password) # call the main function simple_password on user's password to execute.

#now it prints all the required callings
print("\nPassword:", result["password"])
print("Score:", result["score"], "/8")
print("Strength:", result["strength"])
print("Suggestions:")
for s in result["suggestions"]:
    print(" -", s)


if result ["strength"] in ["Very Weak","Weak","Moderate"]:
    print("\nSuggested strong password:")
    print(password_generate(14))


       

         


       

         

        

