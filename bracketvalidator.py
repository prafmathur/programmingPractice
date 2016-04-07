# Code for validating whether a string of brackets has been closed properly

exampleRight = "{[]{()(())[()]}}"
exampleWrong = "{[]{()(()[()]}}"

pair = {"{":"}","[":"]","(":")"}


def validateIter(brackets):
  stack = []
  for b in brackets:
    if b in ["{", "[", "("]:
      stack.append(b)
    else:
      top = stack[-1]
      if pair[top] != b:
        return False
      stack.pop()
  return True

def validateRec(brackets):
  def helper(brackets, seen):
    if brackets == "":
      return True
    b = brackets[0]
    if b in ["{", "[", "("]:
      seen.append(b)
      return helper(brackets[1:], seen)
    else:
      top = seen[-1]
      seen.pop()
      return pair[top] == b and helper(brackets[1:], seen)
  return helper(brackets, [])


print validateIter(exampleRight)
print validateIter(exampleWrong)
print validateRec(exampleRight)
print validateRec(exampleWrong)
