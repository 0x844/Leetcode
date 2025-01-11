def dailyTemperatures(temperatures):
  stack = []
  results = [0] * len(temperatures)

  for i in range(len(temperatures)):
    while len(stack) >= 1 and temperatures[i] > temperatures[stack[-1]]:
      prevIndex = stack.pop()
      results[prevIndex] = i - prevIndex
    stack.append(i)