# pprint for pretty printing
from pprint import pprint

# creating a 'tic-tac-toe' board using list comprehension
board = [[num for num in range(1,4)] for _  in range(3)]
print(board)

# with conditionl logic
new_board = [['x' if num % 2 == 0 else 'o' for num in range(1,4)] for _ in range(3)]
print(new_board)

print("\n")
# other various examples

answer = [[num for num in range(0,3)] for _ in range(3)]
print(answer)

print("\n")

second_answer = [[num for num in range(10)]for _ in range(10)]
pprint(second_answer)
