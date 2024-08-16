def input_and_convert(prompt, conversion_fn):
    string = input(prompt)
    value = conversion_fn(string)
    return value

number1 = input_and_convert("First number: ", int)
number2 = input_and_convert("Second number: ", int)
operation1 = input("Operation [+, -, /, *]: ")
operation = str(operation1)

def output(text, combination):
    print(f"{text} {combination}")

if operation == "+":
    combination = number1 + number2
elif operation == "-":
    combination = number1 - number2
elif operation == "*":
    combination = number1 * number2
elif operation == "/":
    combination = number1 / number2
else:
    combination = "ERROR ... '" + operation + "' unrecognised"

output("Answer", combination)

