from chess.custom_errors.errors import *
from chess.pieces.pieces import *
from nose.tools import *

def test_pieces():
    ''' Test the creation of pieces '''
    # Valid creations
    pawn = Pawn('a', 2, 'white')
    kght = Knight('b', 1, 'white')
    bish = Bishop('f', 8, 'black')
    rook = Rook('a', 1, 'white')
    dama = Queen('d', 8, 'black')
    king = King('e', 1, 'white')
    # Invalid creations
    pawn = assert_raises(InvalidColor, Pawn, 'a', 2, 'blue')
    kght = assert_raises(InvalidRank, Knight, 'b', 14, 'white')
    bish = assert_raises(InvalidFile, Bishop, 'n', 1, 'black')
    dama = assert_raises(InvalidFile, Queen, 'k', 10, 'green')
    
    
def test_pawn():
    ''' Test the pawn object '''
    p = Pawn('a', 2, 'white')
    assert_equal(p.file, 'a')
    assert_equal(p.rank, 2)
    assert_equal(p.COLOR, 'white')
    assert_equal(p.move(('a', 4)), ('a', 4))
    assert_equal(p.file, 'a')
    assert_equal(p.rank, 4)
    # Error handling 
    assert_raises(InvalidMove, p.move, ('c', 5))
        # Edge cases
    p = Pawn('a', 8, 'white')
    assert_raises(InvalidMove, p.move, ('a', 9))
    p = Pawn('a', 1, 'black')
    assert_raises(InvalidMove, p.move, ('a', 0))

def test_knight():
    ''' test the knight object '''
    k = Knight('b', 1, 'white')
    assert_equal(k.file, 'b')
    assert_equal(k.rank, 1)
    assert_equal(k.COLOR, 'white')
    assert_equal(k.move(('c', 3)), ('c', 3))
    # Error handling 
    assert_raises(InvalidMove, k.move, ('c', 4))
    assert_raises(InvalidMove, k.move, ('c', -2))

def test_bishop():
    '''test the bishop object '''
    b = Bishop('c', 1, 'white')
    assert_equal(b.file, 'c')
    assert_equal(b.rank, 1)
    assert_equal(b.COLOR, 'white')
    assert_equal(b.move(('a', 3)), ('a', 3))
    # Error handling 
    assert_raises(InvalidMove, b.move, ('b', 3))
    assert_raises(InvalidMove, b.move, ('c', 0))

def test_rook():
    '''test the rook object'''
    r = Rook('a', 1, 'white')
    assert_equal(r.file, 'a')
    assert_equal(r.rank, 1)
    assert_equal(r.COLOR, 'white')
    assert_equal(r.move(('a', 4)), ('a', 4))
    assert_equal(r.move(('d', 4)), ('d', 4))
    # Error handling 
    assert_raises(InvalidMove, r.move, ('b', 3))
    assert_raises(InvalidMove, r.move, ('d', 0))
    assert_raises(InvalidMove, r.move, ('j', 4))

def test_queen():
    q = Queen('d', 1, 'white')
    assert_equal(q.file, 'd')
    assert_equal(q.rank, 1)
    assert_equal(q.COLOR, 'white')
    assert_equal(q.move(('d', 4)), ('d', 4))
    assert_equal(q.move(('b', 6)), ('b', 6))
    assert_equal(q.move(('g', 6)), ('g', 6))
    assert_equal(q.move(('c', 2)), ('c', 2))
    # Error handling 
    assert_raises(InvalidMove, q.move, ('a', 8))
    assert_raises(InvalidMove, q.move, ('a', 0))
    assert_raises(InvalidMove, q.move, ('j', 8))

def test_king():
    k = King('e', 1, 'white')
    assert_equal(k.file, 'e')
    assert_equal(k.rank, 1)
    assert_equal(k.move(('d', 2)), ('d', 2))
    assert_equal(k.move(('d', 1)), ('d', 1))
    assert_equal(k.move(('e', 2)), ('e', 2))
    assert_equal(k.move(('f', 1)), ('f', 1))
    # Error handling 
    assert_raises(InvalidMove, k.move, ('f', 3))
    assert_raises(InvalidMove, k.move, ('f', 0))



