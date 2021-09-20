def announce(f):
    def wrapper():
        print("About to run the program...")
        f()
        print("Program run successfully!")
    return wrapper

@announce
def hello():
    print("Hello World!")

hello()