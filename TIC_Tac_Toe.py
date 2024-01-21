class Game:
  def __init__(self, player1, player2):
    self.board = Board()
    self.players = [player1, player2]
    self.turn = False
  
  def play(self):
    while True:
      current_player = self.players[int(self.turn)]
      print(self.board.to_string())
      move = int(input(f'This is current board, {current_player.name}\n'))
      
      try:
        is_winner = self.make_move(current_player, move)
        break

      except ValueError:
        move = int(input('illegal move, please try again\n'))
      self.turn = not self.turn

      if is_winner:
        break
  
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
    if self.board[plase] != ' ':
      raise ValueError(f"Plase {plase} is already taken")
    self.board[plase] = player.player_shape
    return self.is_winner(player.player_shape)
  
  def is_winner(self, player_shape):
    winner_positions = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8]
    ]
    return any([all(self.board[x] == player_shape for x in pos) for pos in winner_positions])

Game(Player("Shloimy", 'o'), Player('haiim', 'x')).play()