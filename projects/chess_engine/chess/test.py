class Test():
    def __init__(self, file):
        self.file = file
        print (self.file)

test = Test('test')

def returning():
    return 10, 20

a, b = returning()
print (a, b)