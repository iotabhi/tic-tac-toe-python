"""
Tic-Tac-Toe Game
----------------
A console-based implementation of Tic-Tac-Toe in Python.
Features specific AI logic for the computer player.
Author: [Abhilasha Manjeet]
Date: December 2025
"""
import random
import os
def clear_scr():
     os.system('cls' if os.name == 'nt' else 'clear')
def display_board(board):   
     print("+-------+-------+-------+")
     for row in board:
        print("|       |       |       |")
        print(f"|  {row[0]}    |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")
def enter_move(board):
    while True:
          try:
            move=int(input("Enter your move from (1-9!)"))
            if move <1 or move>9:
                print("Input out of Range!,Enter Number between 1-9")
                continue
            free_fields=list_of_free_fields(board)
            for(row,col) in free_fields:
                if board[row][col]==move:
                      board[row][col]='O'
                      return
            print("That spot is already taken!Try again.")
          except ValueError:
            print("Invalid move!Try Again")
def list_of_free_fields(board):
    free=[]
    for row in range(3):
         for col in range(3):
              if board[row][col] not in ['X','O']:
                   free.append((row,col))
    return free
def victory_for(board, sign):
     for row in board:
          if all(cell==sign for cell in row):
               return True
     for col in range(3):
          if all(board[row][col]==sign for row in range(3)):
               return True
     if all(board[i][i]==sign for i in range(3)):
          return True
     if all(board[i][2-i]==sign for i in range(3)):
          return True
     return False
def draw_move(board):
     free=list_of_free_fields(board)
     move=random.choice(free)
     board[move[0]][move[1]]='X'
def play():
 board=[[1,2,3],[4,'X',6],[7,8,9]]
 clear_scr()
 display_board(board)
 while True:
        enter_move(board)
        display_board(board)
        if victory_for(board, 'O'):
            print("You win!")
            break
        if not list_of_free_fields(board):
            print("It's a draw!")
            break
        draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print("Computer wins!")
            break
        if not list_of_free_fields(board):
            print("It's a draw!")
            break
while True:
     ch=input("Do you want to play Tic-Tac-Toe?Enter :(y/n)").lower()
     if ch=='y':
          play()

     else:
         break
print("Thanks for Playing!🥳")
