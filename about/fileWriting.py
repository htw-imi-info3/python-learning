
def fileWriting(usertext):
    f = open("fileWriting.txt", "a")
    f.write("What would you like to)
    f.close()
    f = open("fileWriting.txt", "r")
    print(f.read())

userText = input("What would you like to add to the text file?")
fileWriting(userText)