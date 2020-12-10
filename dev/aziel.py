def goodbye(target):
  print("goodbye " + target)

def hello(target):
  global hello
  print("hello " + target)
  hello = goodbye

hello("world")
hello("done")

print("aziel")