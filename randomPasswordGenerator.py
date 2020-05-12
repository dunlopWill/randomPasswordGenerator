import random
import string

#Obtain password length
passwordLength = int(input("How many characters would like your password to be?\n"))
print("Okay, your password will be " + str(passwordLength) + " characters long!")

#Set characters to include in password
includeLower = True
includeUpper = True
includeNumbers = True
includePunct = True

def password(n):
    if includeLower and not includeUpper and not includeNumbers and not includePunct:
        print("".join(random.choice(string.ascii_lowercase) for i in range(n)))
    elif includeLower and includeUpper and not includeNumbers and not includePunct:
        print("".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(n)))
    elif includeLower and includeNumbers and not includeUpper and not includePunct:
        print("".join(random.choice(string.ascii_lowercase + string.digits) for i in range(n)))
    elif includeLower and includePunct and not includeUpper and not includeNumbers:
        print("".join(random.choice(string.ascii_lowercase + string.punctuation) for i in range(n)))
    elif includeLower and includeUpper and includeNumbers and not includePunct:
        print("".join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(n)))
    elif includeLower and includeUpper and includePunct and not includeNumbers:
        print("".join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.punctuation) for i in range(n)))
    elif includeLower and includeNumbers and includePunct and not includeUpper:
        print("".join(random.choice(string.ascii_lowercase + string.digits + string.punctuation) for i in range(n)))
    elif includeLower and includeUpper and includeNumbers and includePunct:
        print("".join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation) for i in range(n)))
    elif includeUpper and not includeLower and not includeNumbers and not includePunct:
        print("".join(random.choice(string.ascii_uppercase) for i in range(n)))
    elif includeUpper and includeNumbers and not includeLower and not includePunct:
        print("".join(random.choice(string.ascii_uppercase + string.digits) for i in range(n)))
    elif includeUpper and includePunct and not includeLower and not includeNumbers:
        print("".join(random.choice(string.ascii_uppercase + string.punctuation) for i in range(n)))
    elif includeUpper and includeNumbers and includePunct and not includeLower:
        print("".join(random.choice(string.ascii_uppercase + string.digits + string.punctuation) for i in range(n)))
    elif includeNumbers and not includeLower and not includeUpper and not includePunct:
        print("".join(random.choice(string.digits) for i in range(n)))
    elif includeNumbers and includePunct and not includeLower and not includeUpper:
        print("".join(random.choice(string.digits + string.punctuation) for i in range(n)))
    elif includePunct and not includeLower and not includeUpper and not includeNumbers:
        print("".join(random.choice(string.punctuation) for i in range(n)))

password(passwordLength)
