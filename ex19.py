def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print ("You have %r cheesees!" % cheese_count)
    print ("you have %d boxes of crackers" % boxes_of_crackers)
    print ("Man that is enough for a party.")
    print ("get a blanket.\n")


print ("We can just give the function numbers directly:")
cheese_and_crackers(20,10)


print ("or, we can use the variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print ("We can even do math inside too:")
cheese_and_crackers(10+78, 39+72839)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese+8989, amount_of_crackers +383)
