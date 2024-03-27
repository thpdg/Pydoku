import sys
def generate_permutations(digits, current_permutation, all_permutations, file=None):
    if not digits:
        #all_permutations.append(current_permutation[:])
#         all_permutations.append(reshape_permutation(current_permutation,3))
        #print(current_permutation)
        print(".",end="")
        if not file==None:
            file.write('%s\n' %current_permutation)
        return

    for i in range(len(digits)):
        # Choose
        digit = digits[i]
        current_permutation.append(int(digit))
        remaining_digits = digits[:i] + digits[i + 1:]

        # Explore
        generate_permutations(remaining_digits, current_permutation, all_permutations,file)

        # Unchoose
        current_permutation.pop()

def generate_all_permutations(digits,file=None):
    all_permutations = []
    generate_permutations(digits, [], all_permutations, file)
    return all_permutations

# Shapes a 1-D list into the desired square
def reshape_permutation(incoming,square):
    # print("incoming is " + str(incoming))
    if len(incoming)<(square*square):
        print("Wrong size dummy")
        return []
    slot = 0
    board = []
    new = []
    for i in range (0, square):
        for j in range (0, square):
            new.append(incoming[slot])
            slot+=1
        board.append(new)
        new = []
    # print(board)
    return board

if __name__ == "__main__":
# # Example usage:
    digits = '123456789'
    f = open('all_perm.txt', 'w+')
    all_permutations = generate_all_permutations(digits,f)
    f.close()
    # print(all_permutations)
    board_count = 1
#     for perm in all_permutations:
#         print(perm)
#         print("board " + str(board_count))
#         board_count+=1
    print(len(all_permutations))

    
