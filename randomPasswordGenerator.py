import random
import string

yes = {"Y", "Yes", "y", "yes", "Yeah", "yeah"}

no = {"N", "No", "n", "no", "Nope", "nope"}

print("Hello, I am a random password generator!")

passwordlength = int(input("How many characters would like your password to be?\n"))
print("Okay, your password will be " + str(passwordlength) + " characters long!")

includelower = str(input("Would you like to include LOWER case letters in your password? (Yes/No)"))
if includelower == yes:
    True
if includelower == no:
    False

includeupper = str(input("Would you like to include UPPER case letters in your password? (Yes/No)"))
if includeupper == yes:
    True
if includeupper == no:
    False

includenumbers = str(input("Would you like to include NUMBERS in your password? (Yes/No)"))
if includenumbers == yes:
    True
if includenumbers == no:
    False

includepunct = str(input("Would you like to include SPECIAL CHARACTERS (e.g. punctuation) in your password? (Yes/No)"))
if includepunct == yes:
    True
if includepunct == no:
    False

def poorpassword(passwordlength1=int(passwordlength)):
    lowerletters = string.ascii_lowercase
    return "".join(random.choice(lowerletters) for i in range(passwordlength1))

def weakpassword(passwordlength1=int(passwordlength)):
    lowerletters = string.ascii_lowercase
    upperletter = string.ascii_uppercase
    return "".join(random.choice(lowerletters + upperletter) for i in range(passwordlength1))

def moderatepassword(passwordlength1=int(passwordlength)):
    lowerletters = string.ascii_lowercase
    upperletter = string.ascii_uppercase
    includenumbers = string.digits
    return "".join(random.choice(lowerletters + upperletter + includenumbers) for i in range(passwordlength1))

def reasonablepassword(passwordlength1=int(passwordlength)):
    lowerletters = string.ascii_lowercase
    upperletter = string.ascii_uppercase
    includenumbers = string.digits
    includepunct = string.punctuation
    return "".join(random.choice(lowerletters + upperletter + includenumbers + includepunct) for i in range(passwordlength1))

if includelower and includeupper and includenumbers and includepunct:
    print("Your reasonably secure password is " + reasonablepassword()),
elif includelower and includeupper and includenumbers and not(includepunct):
    print("Your moderately secure password is " + moderatepassword()),
elif includelower and includeupper and not(includenumbers) and not(includepunct):
    print("Since your password is not complex, its security level is rated WEAK. It is " + weakpassword()),
elif includelower and not(includeupper) and not(includenumbers) and not(includepunct):
    print("Since your password is not complex, its security level is rated POOR. It is" + poorpassword())