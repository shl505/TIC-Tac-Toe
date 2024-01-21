class Game:
  def __init__(self):
    pass
  
class Player:
  def __init__(self, name, player_shape):
    self.name = name
    self.player_shape = player_shape

class Board:
  def __init__(self):
    self.board = [' '] * 9

  def to_string(self):
    return '{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}\n'.format(*self.board)

  def make_move(self, player, plase):
    if self.board[plase] == ' ':
      self.board[plase] = self.player_shape
