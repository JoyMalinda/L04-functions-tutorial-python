def input_and_convert(prompt, conversion_fn):
    string = input(prompt)
    value = conversion_fn(string)
    return value

def output(parameter1, parameter2):
    print(f"{parameter1} {parameter2}")


number1 = input_and_convert(" First number: ", int)

number2 = input_and_convert("Second number: ", int)

operation = input_and_convert("Operation [+, -]: ", str)

if operation == "+":
    combination = number1 + number2
elif operation == "-":
    combination = number1 - number2

output("Answer:", combination)

print()
input("Press return to continue ...")
