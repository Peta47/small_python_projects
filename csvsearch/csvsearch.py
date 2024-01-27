search = str(input("zadej znacku co hledas:"))
word = ""

file = open("text.csv")
newfile = open("newtext.csv", "w")
line = file.readline()
while line != "":
    for letter in line:
        if letter != ",":
            word = word + letter
            if word == search:
                newfile.write(line)
                print(line)
        elif letter == ",":
            word = ""
    word = ""
    line = file.readline()
file.close()
newfile.close()
