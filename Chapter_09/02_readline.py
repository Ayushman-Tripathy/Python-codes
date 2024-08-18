with open('profile.txt', 'r') as profile:
    print(profile.readline())
#  it will read the first line of the text file

# After read any file the curser stays until we move that to anywhere
# to move the curser after read there is a command given below
    profile.seek(0)
# so by using seek we shifted the curser to the first place 
# seek needs atleast 1 argument , we can give 2 arguments too for different place
# where seek( places_to_move , from_where )
# there are 3 argu for specify the second argu like 0 and 1 and 2
# where 0 stands for start and 1 for the current position and 2 uses for last position 
# note if we need from last we have to specify the read mode to readboolean or 'rb'

    print(profile.read(5))


# with open('profile.txt', 'r') as f:
#     print(f.readline(5))
#     f.seek(0,1)
#     print(f.readline(5))
