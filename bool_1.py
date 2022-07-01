def dislike(a):
  if (type(a) is int or type(a) is float) and a == 6.0:
    return 'just not 6!'
  return True

print(dislike(6))
print(dislike(5))
print(dislike(6.0))
print(dislike('6'))
print(dislike(True))
