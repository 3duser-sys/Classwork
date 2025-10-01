class IOstring:

    def __init__(self):
        self.strm = ""

    def string_input(self):
        self.strm = input("Enter String:")

    def printthestring(self):
        print("Result: ", self.strm.upper())


strm = IOstring()
strm.string_input()
strm.printthestring()