import os

desk = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
user1 = 'User1'
user2 = 'User2'
i = 4
game_over = False

#For clearing console:
def clear_cons():
    os.system('cls')


def print_desk():
    clear_cons()
    print(desk[:3])
    print(desk[3:6])
    print(desk[6:])

def if_user_win(symb):
    if desk[0] == symb and desk[1] == symb and desk[2] == symb:
        return True
    elif desk[3] == symb and desk[4] == symb and desk[5] == symb:
        return True
    elif desk[6] == symb and desk[7] == symb and desk[8] == symb:
        return True

    elif desk[0] == symb and desk[3] == symb and desk[6] == symb:
        return True
    elif desk[1] == symb and desk[4] == symb and desk[7] == symb:
        return True
    elif desk[2] == symb and desk[5] == symb and desk[8] == symb:
        return True
    
    elif desk[0] == symb and desk[4] == symb and desk[8] == symb:
        return True
    elif desk[2] == symb and desk[4] == symb and desk[6] == symb:
        return True

def if_user_pos_is_corect(pos):
    try:
        if desk[pos] == ' ':
            return True
    except:
        return False

def user1_make_pass(pos):
    desk[pos] = 'x'

def user2_make_pass(pos):
    desk[pos] = '0'

def table_full():
    count = 0
    for i in desk:
        if i == " ":
            count += 1
    if count <= 1:
        print("Table is full")
        game_over = True

print("Rules:")
print("Use index 1 to 9")
print("If you accidentaly write incorect index, you can't rewrite")
input()

while not game_over:
    print_desk()
    position = input(user1 + " make pass: ")
    position = int(position) -1
    if if_user_pos_is_corect(position):
        user1_make_pass(position)    
        if if_user_win('x'):
            print_desk()
            print(user1 + " win!")
            game_over = True
            break

    print_desk()
    position = input(user2 + " make pass: ")
    position = int(position) - 1
    if if_user_pos_is_corect(position):
        user2_make_pass(position)    
        if if_user_win('0'):
            print_desk()
            print(user2 + " win!")
            game_over = True
            break

    if table_full():
        game_over = True

print("Game Over")