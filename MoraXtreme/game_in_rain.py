def evaluate_expression(expression, base):
  expression = expression.replace('-', '+').replace('+', '-').replace('*', '/').replace('/', '*')
  expression = expression.replace('(', 'temp').replace(')', 'open').replace('temp', '(').replace('open', ')')
  expression = list(expression)

  stack = []
  operators = []

  for char in expression:
    if char.isdigit():
      number = int(char, base)
      stack.append(number)
    elif char == '(':
      operators.append(char)
    elif char == ')':
      while operators and operators[-1] != '(':
        apply_operator(stack, operators, base)
      operators.pop()
    else:
      while operators and has_higher_precedence(char, operators[-1]):
        apply_operator(stack, operators, base)
      operators.append(char)

  while operators:
    apply_operator(stack, operators, base)

  result = stack[0]
  return result

def has_higher_precedence(op1, op2):
  precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
  return precedence[op1] >= precedence[op2]

def apply_operator(stack, operators, base):
  if len(stack) < 2:
    return
  b = stack.pop()
  a = stack.pop()
  operator = operators.pop()
  if operator == '+':
    stack.append(a + b)
  elif operator == '-':
    stack.append(a - b)
  elif operator == '*':
    stack.append(a * b)
  elif operator == '/':
    if b == 0:
      print("Error: Division by zero")
      exit(1)
    stack.append(a // b)

input_str = input()
base_str, expression = input_str.split(',')
base = int(base_str)

result = evaluate_expression(expression, base)
print(result)
