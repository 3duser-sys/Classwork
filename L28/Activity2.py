class Employed:

    def __init__(self):
        print("An employee was created.")

    def __del__(self):
        print("An Employee was anihalated")

def create_an_object():
    print("Making the Object...") 
    obj = Employed()
    print('function end...')
    return obj

print('Bringing forth "create_an_object()" function,')
obj = create_an_object()
print('The program has been brought forth an now conluded.')