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
      while True:
        try:
          is_winner = self.board.make_move(current_player, move)
          break

        except ValueError:
          move = int(input('illegal move, please try again\n'))
      self.turn = not self.turn
      if is_winner or self.board.is_draw():
        break
    print(self.board.to_string())
    if is_winner:
      print(f'Congratulations {current_player.name} you won!')
    else:
      print('It\'s a tie!')
      
  
class Player:
  def __init__(self, name, player_shape):
    self.name = name
    self.player_shape = player_shape

class Board:
  def __init__(self):
    self.board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

  def is_draw(self):
    return all(str(i) not in self.board for i in range(9))
    
  def to_string(self):
    return '{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}\n'.format(*self.board)

  def make_move(self, player, plase):
    if self.board[plase] != ' ':
      raise ValueError(f"Plase {plase} is already taken")
    self.board[plase] = player.player_shape
    return self.is_winner(player.player_shape)
  
  def is_winner(self, player_shape):
    winner_positions = [
      (0, 1, 2),
      (3, 4, 5),
      (6, 7, 8),
      (0, 3, 6),
      (1, 4, 7),
      (2, 5, 8),
      (0, 4, 8),
      (2, 4, 6)
    ]
    return any([all(self.board[x] == player_shape for x in pos) for pos in winner_positions])

Game(Player(input('Enter teh name of player 1:\n'), 'o'), Player(input('Enter teh name of player 2:\n'), 'x')).play()
