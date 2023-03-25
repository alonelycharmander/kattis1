
def game():
  cin = input()
  played = []
  r = len(cin)-1
  l = len(cin)-4
  curr_board = []
  for i in range(3):
    played.append(str(bin(int(cin[r-i]))[2:].zfill(3)))
  
  index = 0
  while l >= 0:
    tmp = str(bin(int(cin[l]))[2:].zfill(3))
    curr_board.append(tmp)
    index += 1 
    if index > 2:
      break
    l -= 1

  #Checks for the row wins 
  for i in range(len(curr_board)):
    if played[i] == '111':
      if curr_board[i] == '111':
        return 1
      if curr_board[i] == '000':
        return 0
  
  #checks for the vertical wins 
  for i in range(len(curr_board)):
    if played[0][i] == '1' and played[1][i] == '1' and played[2][i] == '1':
        if curr_board[0][i] == '1' and curr_board[1][i] == '1' and curr_board[2][i] == '1':
            return 1
        if curr_board[0][i] == '0' and curr_board[1][i] == '0' and curr_board[2][i] == '0':
            return 0
  #checkes of the diagnal wins 
  if played [1][1] == '1' and played[0][0] == '1' and played[2][2] == '1':
      if curr_board[0][0] == '1' and curr_board[1][1] == '1' and curr_board[2][2] == '1':
          return 1
      if curr_board[0][0] == '0' and curr_board[1][1] == '0' and curr_board[2][2] == '0':
          return 0
  if played [1][1] == '1' and played[0][2] == '1' and played[2][0] == '1':
      if curr_board[0][2] == '1' and curr_board[1][1] == '1' and curr_board[2][0] == '1':
          return 1
      if curr_board[0][2] == '0' and curr_board[1][1] == '0' and curr_board[2][0] == '0':
          return 0
  if played[0] == '111' and played[1] == '111' and played[2] == '111':
        return 3
  else:
        return 2


rounds = int(input())

for i in range(rounds):
  winner = game()
  if winner == 3:
    print("Cat's")
  if winner == 2:
    print("In progress")
  if winner == 1:
    print("X wins")
  if winner == 0:
    print("O wins")
  