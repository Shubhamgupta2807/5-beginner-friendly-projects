'''
use input funtion to input user chice
funtion method for organize and call service
conditional statement to decide
file handing to open, edit ,xlear and close file
loops for calculation
bsic maths
'''

HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE, "r")
    lines = file.readlines()
    if len(lines) == 0:
        print("No histroy found!")
    else:
        for line in lines:
            print(line.strip())
        file.close()


def clear_history():
    file = open(HISTORY_FILE,"w")
    file.close()
    print("History cleared!")


def save_history(equation, result):
    file = open(HISTORY_FILE, "a")
    file.write(equation + "=" + str(result) +"\n")
    file.close()


def calculator(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input!")
        return

    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot devide by zero!")
            return
        result = num1 / num2
    else:
        print("Invalid operators! Use valid Operator.")

    if int(result) == result:
        result = int(result)
    print(f"Result - {result}")
    save_history(user_input, result)

def main():
    print("--Simple calculators  (History , Exit , clear)--")
    while True:
        user_input = input("Enter calculation (+ - / *) or cammond (history , clear , exit) = ").lower()
        if user_input == "exit":
            print("Good Byee..")
            break
        elif user_input == "history":
            print("All history -\n")
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculator(user_input)

main()
