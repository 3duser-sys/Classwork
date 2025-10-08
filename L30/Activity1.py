class myClass:

    __privateVar = 27;

    def __privatemeth(self):
        print("I am inside class myClass")

    
    def hello(self):
        print("Private Variable value: ", myClass.__privateVar)

foo = myClass()
foo.hello
foo.__privatemeth