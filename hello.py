def goodbye(target):
    print("Goodbye " + target)

def hello(target):
    global hello
    print("Hello " + target)
    hello = goodbye

hello("Ryan")
hello("Ryan")
