
#define first function
def first_function(msg):
    print(msg)

#define second function
def sum_two_integers(a, b):
    c = a + b
    return c 

# invoke first function
msg = "hello world"
first_function(msg.capitalize)


# invoke second function

number_1 = 13 
number_2 = 21 
sum = sum_two_integers(number_1, number_2)

print(f"{number_1} plus {number_2} is {sum}")
