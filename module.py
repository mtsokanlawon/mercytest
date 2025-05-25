# A title caser
def title_caser():
  user_text = input("Enter your text: ")
  title_case = user_text.upper()
  return title_case

# A simple calculator.
def calculator():
  operand1 = float(input("Enter your first operand: ")
  operand2 = float(input("Enter your second operand: ")
  operator = input("Enter your operator(+, -, /, *): ")

  if operator == '+':
    print(operand1 + operand2)
  elif operator == '-':
    print(operand1 - operand2)
  elif operator == '/':
    print(operand1 / operand2)
  elif operator == '*':
    print(operand1 * operand2)
  else:
    print("Invalid input!")
                   
    
