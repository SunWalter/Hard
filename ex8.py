formatter = "%r %r %r %r"

print (formatter % (1,2,3,4)) # put each number into the formatter
print (formatter % ("one", "two", "three", "four"))
print (formatter % (True, False, False, True))
print (formatter % (formatter, formatter,formatter,formatter)) #put each string into formatter
print (formatter % (
    "I had this thing.",
    "That you could type up right",
    "But it didn't sing",
    "So I said goodnight."
))
