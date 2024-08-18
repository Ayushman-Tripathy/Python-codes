text = input("Enter a Text:\n")

if ("make a lot of money" in text):
    Spam = True
elif ("Buy now" in text):
    Spam = True
elif ("Click this" in text):
    Spam = True
elif ("Subscribe this" in text):
    Spam = True
elif ("Buy it" in text):
    Spam = True
elif ("Join us" in text):
    Spam = True
else:
    Spam = False

if (Spam is True):
    print("Spamming not allowed!\nYou can't use this here")
else:
    print("It is not a spam you can use it",text)
