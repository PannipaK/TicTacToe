class TicTacToe():
  def __init__(self):
    self.boardState=[None]*9
    self.mark = 'X'
    self.finished = False

  def printBoard(self):
    for i in range(0, 9):
      print(self.boardState[i], end="\t")
      if not (i+1) % 3:
        print()
    print("-"*20)
    print()

  def placeMark(self, position, mark):
    self.boardState[position-1] = mark

  def isBoardFilled(self):
    if all(self.boardState):
      return True
    return False

  def isWinner(self):
    # if all row is same mark
    # or if all column is same mark
    # or if 1,5,9 is same mark
    # or if 3,5,7 is same mark
    # then there is a winner.
    # the winner is the one with the mark.
    for mark in ['X', 'O']:
      # if all row is same mark
      for i in [0, 3, 6]:
        if self.boardState[i:i+3].count(mark) == 3:
          return True
      # if all col is same mark
      for i in [0, 1, 2]:
        if [self.boardState[i], self.boardState[i+3], self.boardState[i+6]].count(mark) == 3:
          return True
      if [self.boardState[0], self.boardState[4], self.boardState[8]].count(mark) == 3:
          return True
      if [self.boardState[2], self.boardState[4], self.boardState[6]].count(mark) == 3:
          return True
    return False

  def nextMove(self):
    if self.isWinner() or self.isBoardFilled():
      if self.isWinner():
        print('Winner is', self.mark)
      else:
        print('A tie.')
      self.finished = True
      return
    if self.mark == 'O':
      self.mark = 'X'
    else:
      self.mark = 'O'
    move = int(input('place your {}: '.format(self.mark)))
    self.placeMark(move, self.mark)
    self.printBoard()


game = TicTacToe()
game.printBoard()
while not game.finished:
  game.nextMove()
