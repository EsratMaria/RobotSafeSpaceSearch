import warnings
warnings.filterwarnings('ignore')


# Agent's action can be stated -> POSSIBLE_ACTIONS = ('U', 'D', 'L', 'R')

print("------------- Detection of Safe Search Space of Robot ------------------")


threshold = 23


def conversion(current_point):
    return str(current_point[0]) + "," + str(current_point[1])

# to keep track of the coordinates that have been visited by the robot already


def visited_before(current_point):
    if(conversion(current_point) in check_state):
        return False
    else:
        return True

# here I am counting the total sum of coodinates. for example: (22,30) -> 2+2+3+0 =7


def mine_safe_space_checking(current_point):
    a = str(abs(current_point[0]))
    b = str(abs(current_point[1]))
    values = a + b
    sum = 0
    for value in str(values):
        sum = sum + int(value)
    return sum

# checking the coordinate sum to see if they satisfy the given threshold = 23


def mine_safe_space(current_point):
    if(mine_safe_space_checking(current_point) <= threshold):
        return True
    else:
        return False


# ====================================  Main Code Body ====================================

current_point = [0, 0]  # this is the starting point
check_state = set([])
safe_block = 0
stack = []
stack.append(current_point)

while(len(stack)):
    coordinate = stack.pop()
    if(mine_safe_space(coordinate) and visited_before(coordinate)):
        check_state.add(conversion(coordinate))
        safe_block += 1
        stack.append([coordinate[0], coordinate[1] - 1])
        stack.append([coordinate[0], coordinate[1] + 1])
        stack.append([coordinate[0] - 1, coordinate[1]])
        stack.append([coordinate[0] + 1, coordinate[1]])

print('Total safe area for the robot after training is: ', +safe_block)
