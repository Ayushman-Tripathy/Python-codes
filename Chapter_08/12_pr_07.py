def remove_and_strip(string, value):
    newstring = string.replace(value,"")
    return newstring.strip()

sentence = "Hellow ayushman, how are you ? me"
p = remove_and_strip(sentence, "me")
print(p)