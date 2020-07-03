import random

# import hashlib
# import os

# ------------------------------------------------------------------------------
# PasswordGenerator.py
# by: Steven Johnson
# Last Modified: 11/29/2018
#
# Ran the Python code style checker
# From terminal run "pycodestyle --first PasswordGenerator.py"
# 1 error from pycodestyle for line 29, worth mentioning below
#   PasswordGenerator.py:29:28: W605 invalid escape sequence '\]'
#  Solved this by using a raw string foo = r"\"   - see line 41
#
# This is now solved and no errors returned from pycodestyle
# ------------------------------------------------------------------------------


def gen_pwd(pwd_len=8):

    # password lengths under 8 get changed back to 8, under 8 is weak sauce
    if pwd_len < 8:
        pwd_len = 8
        # print ("Passwords under 8 characters are very weak
        # , defaulted to length to 8.")

    myrandom = []
    randomoutput = random.SystemRandom()

    # variables to keep track of the current random character and the last one
    # don't want characters to repeat, start off different on purpose
    mytemp = 'a'
    mytemp2 = 'z'

    # keep track of the last special character used
    mytemp3 = '!'
    mynewval = 0

    # define characters to use in password
    normalchars = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ" \
                  "0123456789"
    specialchars = r"!#$%&'()*+,-./\:|;<=>?@[]^_`{}~"

    # keep track of special chars
    # don't want more than the max dynamically decided below
    specialchar_count = 0

    # define a min/max range to be used to determine randomly
    # how many special chars are in password
    minrange = pwd_len // 8
    maxrange = pwd_len // 4 + 1

    # Debug
    # print (str(minrange) + " " + str(maxrange))

    maxspecialchars = random.randint(int(minrange), int(maxrange))
    # debug
    #  random.randint(2,6)
    mybool = 1

    # Debug
    # print("Max: " + str(maxspecialchars))
    # chances = [mynewval for mynewval in range(1,257)]
    # for mynewval in range(1,21):

    # --------------------------------------------------------------------------
    # Using the while loop allows me to move the index backwards to fight
    # repeated characters, for loops don't allow index manipulations
    # --------------------------------------------------------------------------

    while mynewval < pwd_len:

        # print(mytemp2)
        mytemp2 = mytemp

        # test for zero in the while loop, 1 for a for loop
        if mynewval == 0 or mynewval == pwd_len - 1 \
                or specialchar_count == maxspecialchars or mybool == 1:
            # 5 times to help with randomness
            mytemp = randomoutput.choice(normalchars * 5)
            myrandom.append(mytemp)
            mybool = 0

        # if the counter variable mynewval is great than or equal to half
        # the password length then give the password a special character,
        # basically trying ot increase the randomness and uniqueness
        # or (specialchar_count < maxspecialchars
        # and mynewval == pwd_len-maxspecialchars): # mynewval >= pwd_len/2 and
        elif (mynewval >= pwd_len-minrange - maxrange
              and specialchar_count < maxspecialchars and mybool == 0):

            # simply trying to increase randomness of the special characters
            # in the final password, 3 times for special chars
            mytemp = randomoutput.choice(specialchars * 7)
            myrandom.append(mytemp)

        else:
            # 4 times for both again, changing it up to help with randomness
            mytemp = randomoutput.choice((normalchars + specialchars) * 10)
            myrandom.append(mytemp)
            mybool = 0

        # if the value from last pass equals this pass then throw it out.
        # Pop it off, iterate again
        if mytemp2 == mytemp or mytemp3 == mytemp:
            mytemp = "a"
            mytemp2 = "z"
            myrandom.pop()
            mynewval -= 1

        # look for any of the characters and if it exists
        # then increment the counter
        if any(char in specialchars for char in mytemp):
            specialchar_count += 1
            mybool = 1

            # remove the special character so it won't be reused,
            # experiment to see how it helps with randomness
            specialchars = specialchars.replace(mytemp, "")

            # keep track of which special character was assigned
            mytemp3 = mytemp

        # increment the loop counter
        mynewval = mynewval + 1

    mypwd = ''.join(str(i) for i in myrandom)

    # # debug and playing
    # print(mypwd + " Len = " + str(len(myrandom)) + " Special Char Count = "
    # + str(specialchar_count) + " MD5 Hash (Hex)= "
    # + hashlib.md5(mypwd.encode('utf-8')).hexdigest() )

    # print (mypwd)

    # ----------------------------
    # return the random password
    # ----------------------------

    return mypwd


def main():

    # Variable to control how long of a password you want
    PasswordLength = 24

    for i in range(10):
        temp = gen_pwd(PasswordLength)
        print(temp)
        temp = ""


if __name__ == '__main__':
    main()
