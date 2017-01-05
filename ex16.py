from sys import argv

script, filename = argv

print ("We are going to erase %r." % filename)
print ("If you don't want to that, hit CTRL-C.")
print ("If you want do that, hit RETURN.")

input("?")

print ("Opening the file ...")
target = open(filename, 'w')

print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I am going to ask you 3 lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I am going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print('And finally, we close it.')
target.close()
