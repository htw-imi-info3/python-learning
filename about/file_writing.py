def fileWriting(usertext):
    f = open("lab3filewriting.txt", "a")
    f.write(usertext)
    f.close()
    f = open("lab3filewriting.txt", "r")
    print(f.read())

userText = input("What would you like to add to the text file?")
fileWriting(userText)