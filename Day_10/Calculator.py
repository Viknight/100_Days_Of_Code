import art
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(art.logo)
  num1 = float(input("What's the first number?: "))
  for i in operations:
    print(i)
  end_of_calculation = False

  while not end_of_calculation:

    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))

    function = operations[operation_symbol]
    answer = function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit. :") == "n":
      end_of_calculation = True
      calculator()
    else:
      num1 = answer

calculator()