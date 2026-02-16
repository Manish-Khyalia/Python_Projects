from art import  logo
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2) :
    return n1 - n2
def multiply(n1, n2) :
    return n1 * n2
def division(n1, n2) :
    return n1/n2
operators = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : division
}
def calculator() :
    print(logo)
    calculation_done = False
    num1 = float(input("Enter the first number: "))
    while not calculation_done :
        for operator in operators :
            print(operator)
        operator = input("Choose the operator from the above operators: ")
        num2 = float(input("Enter the second number : "))
        answer = operators[operator](num1,num2)
        print(f"The answer of {num1} and {num2} is: {answer}")
        again = input("Enter 'yes' to continue the calculation and 'no' to start again.").lower()
        if again == "yes" :
            num1 = answer
        else :
            calculation_done = True
            print("\n"*30)
            calculator()
calculator()
c