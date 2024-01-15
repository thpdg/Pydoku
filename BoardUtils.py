from genperm import generate_all_permutations
import time


def create_block(starting_value,size):
    new_block = []
    for row in range(size):
        new_row = [starting_value]*size
        new_block.append(new_row)
    
    return new_block


def extract_block(board,block_x,block_y, block_size, scale_size=3):
    print("Extracting block " + str(block_x) + ":" + str(block_y))
    new_block = create_block(0,3)
    new_row = 0
    new_col = 0
    for row in range(block_x*scale_size,(block_x*scale_size)+block_size):
        new_col = 0
        # print("Moving through columns to " + str((block_x*scale_size)+block_size))
        for col in range(block_y*scale_size,(block_y*scale_size)+block_size):
            # print("Copying element from " + str(row) + ":" + str(col) + " to " + str(new_row) + ":" + str(new_col))
            new_block[new_row][new_col] = board[row][col]
            new_col += 1
        new_row += 1
    return new_block

def replace_block(board,block,block_x,block_y, scale_size=3)->list:
    board_x = block_x * scale_size
    for row in range(len(block)):
        board_y = block_y * scale_size
        for col in range(len(block[row])):
            board[board_x][board_y] = block[row][col]
            board_y+=1
        board_x+=1
    return board

def merge_block_if_compatible(board,block,block_x,block_y, scale_size=3)->list:
    out_board = [row[:] for row in board]
    board_x = block_x * scale_size
    for row in range(len(block)):
        board_y = block_y * scale_size
        for col in range(len(block[row])):
            if board[board_x][board_y] == 0:    # If this is blank in the board, fill it
                board[board_x][board_y] = block[row][col]
            else:
                if board[board_x][board_y] != block[row][col]:  # If these are not compatible
                    return board
            board_y+=1
        board_x+=1
    return out_board

# Checks to see if a block will fit into a board with spaces already filled in
def is_compatible_block(board,block,block_x,block_y, scale_size=3)->bool:
    board_x = block_x * scale_size
    for row in range(len(block)):
        board_y = block_y * scale_size
        for col in range(len(block[row])):
            if board[board_x][board_y] != 0:    # If this is blank in the board, fill it
                if board[board_x][board_y] != block[row][col]:  # If these are not compatible
                    return False
            board_y+=1
        board_x+=1
    return True

def print_board(board):
    for row in range(len(board)):
        print(board[row])

def return_test_board():
    return [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

def reduce_board_permutations(board,block_size=3):
    import genperm

    all_good_perms = []*9
    rough_block_number = 0
    for current_block_row in range(3):
        for current_block_col in range(3):
            these_good_perms = []
            perm_board_count = 1
            for perm in all_permutations:
                if is_compatible_block(this_board,perm,current_block_row,current_block_col):
                    # print(perm)
                    # print("board fits:" + str(perm_board_count))
                    these_good_perms.append(perm)
                perm_board_count+=1
            all_good_perms.append(these_good_perms)

            print("Block " + str(current_block_row) + ":" + str(current_block_col) + "->" + str(len(these_good_perms)))

            # for counter,perm in enumerate(all_good_perms[rough_block_number]):
            #     print("Block " + str(rough_block_number) + " Option " + str(counter))
            #     print_board(perm)


            rough_block_number+=1
    return all_good_perms


if __name__ == "__main__":
    # four_board = create_block(4,3)
    # five_board = create_block(5,3)
    # zero_board = create_block(0,9)

    # print_board(four_board)
    # print_board(zero_board)

    # print(is_compatible_block(zero_board,four_board,0,0))
    # new_board = replace_block(zero_board,four_board,0,0)
    # print_board(new_board)

    # print(is_compatible_block(zero_board,five_board,0,0))
    # new_board = merge_block_if_compatible(zero_board,five_board,0,0)
    # print_board(new_board)
    # print()
    start_time = time.time()
    
    this_board = return_test_board()
    print_board(this_board)

    all_permutations = generate_all_permutations('123456789')
    the_good_perms = reduce_board_permutations(this_board)
    
    for index,current_block in enumerate(the_good_perms):
        print("Block " + str(index) + "->" + str(len(current_block)))

    print("--- %s seconds ---" % (time.time() - start_time))

    # And now...recusrions!