from os import linesep as NEW_LINE
from typing import Dict, List, Tuple
import re
import copy


class Board:
    def __init__(self) -> None:
        # [row][column]
        self.board: Dict[Tuple[int,int],int] = {}
        self.lookup: Dict[int,Tuple[int,int]] = {}
        self.num_rows = 0
        self.num_cols = 0


class Input:
    def __init__(self, input: str) -> None:
        self.selections: List[int] = []
        self.boards: List[Board] = []

        input_lines = input.splitlines(False)
        # First line is selections that will be made 
        self.selections = [int(i) for i in input_lines[0].split(',')]

        # Following lines are bingo boards delimited by empty lines
        current_board: Board = None
        current_row = 0
        # Start from 1: as the first line is selections
        for line in input_lines[1:]:
            # Handle a new board being defined
            if (line == '' or line == NEW_LINE):
                if current_board is not None:
                    current_board.num_rows = current_row
                    self.boards.append(current_board)
                current_board = Board()
                current_row = 0
                continue

            current_column = 0
            row_contents = re.findall('\d+', line)
            for value in row_contents:
                current_board.board[(current_row,current_column)] = int(value)
                current_board.lookup[int(value)] = (current_row,current_column)
                current_column += 1

            current_row += 1
            current_board.num_cols = current_column
        
        if len(current_board.board) > 0:
            current_board.num_rows = current_row
            self.boards.append(current_board)


def search_for_bingo(board: Board, current_coords: Tuple[int,int], direction: str) -> bool:
    if direction == 'H':
        bingo = True
        for col in range(board.num_cols):
            if board.board[(current_coords[0], col)] is not None:
                bingo = False
                break
        
        return bingo
    
    if direction == 'V':
        bingo = True
        for row in range(board.num_rows):
            if board.board[(row,current_coords[1])] is not None:
                bingo = False
                break
        
        return bingo


def sum_board(board: Board):
    # k is the key in the lookup table which is the value
    # of the square. By iterating over this we can sum
    # the value of the board
    return sum([k for (k,_) in board.lookup.items()])


with open('input.txt', 'r') as input_file:
    input = input_file.read()

game = Input(input)

# Part 1
# bingo subsystem
part_1_boards = copy.deepcopy(game.boards)
game_won = False

for selection in game.selections:
    if game_won:
        break

    for board in part_1_boards:
        if selection in board.lookup:
            coords = board.lookup[selection]
            # Set to None to mark this square as a match
            board.board[coords] = None
            del board.lookup[selection]
            if search_for_bingo(board, coords, 'H') or search_for_bingo(board, coords, 'V'):
                print(sum_board(board) * selection)
                game_won = True
                break
                
# Part 2
# figure out which board will win last
part_2_boards = copy.deepcopy(game.boards)

for selection in game.selections:
    winning_boards = []
    
    for board in part_2_boards:
        if selection in board.lookup:
            coords = board.lookup[selection]
            # Set to None to mark this square as a match
            board.board[coords] = None
            # Remove from lookup to make summing the board contents easier if we win
            del board.lookup[selection]
            if search_for_bingo(board, coords, 'H') or search_for_bingo(board, coords, 'V'):
                if len(part_2_boards) == 1:
                    print(sum_board(board) * selection)
                    exit(0)
                
                winning_boards.append(board)
    
    for board in winning_boards:
        part_2_boards.remove(board)
