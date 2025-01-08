def evalRPN(self, tokens):
  stack = []
  ops = ['+','-','*','/']

  for i in range(len(tokens)):
    if tokens[i] in ops:
      second = int(stack.pop())
      first = int(stack.pop())

      if tokens[i] == '+':
        stack.append(first + second)
      if tokens[i] == '-':
        stack.append(first - second)
      if tokens[i] == '*':
        stack.append(first * second)
      if tokens[i] == '/':
        stack.append(first / second)
    else:
      stack.append(tokens[i])
  return stack.pop()