from snake_view import get_color 
from snake_main import is_legal_move


def run_all():
    ''' Run all tests for the snake program '''
    # As you add more test functions to this file, call them here
    test_get_color()


def test_get_color():
    print('Tester get_color...', end='')
    assert 'red' == get_color(-1)
    assert 'white' == get_color(0)
    assert 'green' == get_color(1)
    assert 'green' == get_color(42)
    print('OK')


if __name__ == '__main__':
    print('Starting snake_test.py')
    run_all()
    print('Finished snake_test.py')

def test_is_legal_move():
    print('Tester is_legal_move...', end='')
    board = [
        [0, 3, 4],
        [0, 2, 5],
        [0, 1, 0],
        [-1, 0, 0],
    ]
    assert is_legal_move((2, 2), board) is True
    assert is_legal_move((1, 3), board) is False # Utenfor brettet
    assert is_legal_move((1, 1), board) is False # Krasjer med seg selv
    assert is_legal_move((0, 2), board) is False # Krasjer med seg selv

    assert is_legal_move((0, 0), board) is True
    assert is_legal_move((3, 0), board) is True # Eplets posisjon er lovlig
    assert is_legal_move((3, 2), board) is True
    assert is_legal_move((-1, 0), board) is False # Utenfor brettet
    assert is_legal_move((0, -1), board) is False # Utenfor brettet
    assert is_legal_move((3, -1), board) is False # Utenfor brettet
    assert is_legal_move((3, 3), board) is False # Utenfor brettet
    assert is_legal_move((4, 2), board) is False # Utenfor brettet
    print('OK')
test_is_legal_move()