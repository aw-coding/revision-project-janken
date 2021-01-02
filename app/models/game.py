class Game():
    def __init__(self):
        self.win_lookup = {
            'rock' : 'scissors',
            'scissors' : 'paper',
            'paper' : 'rock'
        }


    def check_winner(self, player1, player2):
        winner = None

        if self.win_lookup.get(player1.choice) == player2.choice:
            winner = player1
        
        elif self.win_lookup.get(player2.choice) == player1.choice:
            winner = player2

        elif player1.choice == player2.choice:
            winner = 'draw'

        return winner