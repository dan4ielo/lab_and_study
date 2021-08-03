class Test():
    def __init__(self, file):
        self.file = file
        print (self.file)

test = Test('test')

def returning():
    return 10, 20

a, b = returning()
print (a, b)

valid_moves = [('f', 3), ('h', 3), ('f', 0), ('h', 0), ('e', 2), ('e', 0), (0, 2), (0, 0)]
# [('f', 3), ('h', 3), ('h', 0), ('e', 2), (0, 2)]

# for move in valid_moves: 
#     if 0 in move: valid_moves.remove(move)

print (valid_moves)

cleaned_list = [move for move in valid_moves if 0 not in move]
print (cleaned_list)
