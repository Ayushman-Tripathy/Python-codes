# from os import curdir
# print(curdir)


# use open() function to open and read a file and the syntax is below 
profile = open('profile.txt', 'r') # By default the mode is "r"


print(profile.read())
# data = profile.read(19)
# data = profile.read(19) we can specify the caracter to be read like read(10 or 15 or 5)

# MODES OF OPENING A FILE

# r -> open for reading
# w -> open for writing
# a -> open for appending
# + -> open for updating ( read + write )

# "rb" will open for read in binary mode
# "rt" will open for read in text mode