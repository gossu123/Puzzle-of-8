"""Puzzle of 8"""
import os
import random
import pandas as pd
ARRAY = [[7, 5, 2, 1, 8, 3, 4, " ", 6],
         [5, 1, 3, 8, 6, " ", 2, 7, 4],
         [2, 3, 4, 5, " ", 1, 8, 6, 7]]
MATRIX = random.choice(ARRAY)
M2 = list(map(str, MATRIX))


def solvability():
    """To check solvability"""
    reversibility = 0
    for i, ele1 in enumerate(MATRIX, 0):
        if ele1 == " ":
            continue
        else:
            count = 0
            for j, ele2 in enumerate(MATRIX, 0):
                if i <= j and ele2 != " ":
                    if ele1 > ele2:
                        count = count+1
                else:
                    continue
            reversibility = reversibility+count
    return reversibility


def rightswipe():
    """For right swipe"""
    temp = 0
    for i in range(int(len(MATRIX))):
        if MATRIX[i] == " ":
            if i in (2, 5, 8):
                print("Invalid Move")
                return
            else:
                temp = MATRIX[i+1]
                MATRIX[i+1] = MATRIX[i]
                MATRIX[i] = temp
                break


def leftswipe():
    """For left swipe"""
    temp = 0
    for i in range(int(len(MATRIX))):
        if MATRIX[i] == " ":
            if i in (0, 3, 6):
                print("Invalid Move")
                return
            else:
                temp = MATRIX[i-1]
                MATRIX[i-1] = MATRIX[i]
                MATRIX[i] = temp
                break


def upswipe():
    """For up swipe"""
    temp = 0
    for i in range(int(len(MATRIX))):
        if MATRIX[i] == " ":
            if i in (0, 1, 2):
                print("Invalid Move")
                return
            else:
                temp = MATRIX[i-3]
                MATRIX[i-3] = MATRIX[i]
                MATRIX[i] = temp
                break


def downswipe():
    """For down swipe"""
    temp = 0
    for i in range(int(len(MATRIX))):
        if MATRIX[i] == " ":
            if i in (6, 7, 8):
                print("Invalid Move")
                return
            else:
                temp = MATRIX[i+3]
                MATRIX[i+3] = MATRIX[i]
                MATRIX[i] = temp
                break


def main(move_m):
    """For User"""
    while solvability() > 0 or MATRIX[8] != " ":
        if solvability() % 2 == 0:
            print("This puzzle is solvable \n")
            x_x = input("Enter A for left-Swipe ; D for Right-Swipe;"
                        "W for Up-Swipe; S for Down-Swipe: ")
            if x_x == "D":
                os.system('cls' if os.name == 'nt' else 'clear')
                rightswipe()
                move_m += 1
                for k in range(int(len(MATRIX))):
                    M2[k] = list(map(str, MATRIX))
                    a_a = (" ".join(M2[k][3*k:3*(k+1)]))
                    print(a_a)
            elif x_x == "A":
                os.system('cls' if os.name == 'nt' else 'clear')
                leftswipe()
                move_m += 1
                for k in range(int(len(MATRIX))):
                    M2[k] = list(map(str, MATRIX))
                    a_a = (" ".join(M2[k][3*k:3*(k+1)]))
                    print(a_a)
            elif x_x == "W":
                os.system('cls' if os.name == 'nt' else 'clear')
                upswipe()
                move_m += 1
                for k in range(int(len(MATRIX))):
                    M2[k] = list(map(str, MATRIX))
                    a_a = (" ".join(M2[k][3*k:3*(k+1)]))
                    print(a_a)
            elif x_x == "S":
                os.system('cls' if os.name == 'nt' else 'clear')
                downswipe()
                move_m += 1
                for k in range(int(len(MATRIX))):
                    M2[k] = list(map(str, MATRIX))
                    a_a = (" ".join(M2[k][3*k:3*(k+1)]))
                    print(a_a)
            else:
                print("Invalid Input")
        else:
            print("This puzzle is not solvable")
    return move_m


def user_verification():
    """user_verification Starting function"""
    move_m = 0
    userdata = pd.read_csv("Userdata.csv")
    userdata = userdata.set_index("username")
    count_1 = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    while count_1 == 0:
        username_1 = input("Please Enter Your Username: ")
        if username_1 in userdata.index:
            password_1 = input("Please Enter Your Password: ")
            if password_1 == userdata.at[username_1, "password"]:
                count_1 = 1
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You are logged in")
                userdata.at[username_1, "attempts"] \
                    = userdata.at[username_1, "attempts"]+1
                userdata.to_csv("Userdata.csv")
                for k in range(int(len(MATRIX))):
                    M2[k] = list(map(str, MATRIX))
                    a_a = (" ".join(M2[k][3*k:3*(k+1)]))
                    print(a_a)
                move_m = main(move_m)
            else:
                print("Please Enter correct password")
        else:
            print("Please insert correct Username")
    return move_m


MOVE_M = user_verification()
if solvability() == 0:
    print("YOU WON !!! \n")
    print("Number of Moves: ", MOVE_M)
