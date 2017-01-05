def add(a, b):
    print ("Adding %d and %d" % (a,b))
    return a + b

def subtract(a, b):
    print ("subtracting %d and %d" % (a, b))
    return a - b

def mutiply(a, b):
    print ("mutiplying %d and %d" % (a,b))
    return a * b

def divide(a, b):
    print ("dividing %d and %d" % (a, b))
    return a / b


print ("Let us do some math use just functions!")

age = add(30,5)
height = subtract(190,15)
weight = mutiply(35,2)
iq = divide(500,2)

print ("Age:%d, Height:%d, Weight:%d, IQ:%d." %(age, height, weight, iq))


##################
print ("Here is a puzzle.")

what = add(age, subtract(height, mutiply(weight, divide(iq,2))))

print ("That becomes:", what, "\nCan you do it by hand?")
