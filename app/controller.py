from flask import render_template, request
from app import app
from app.models.player import *
from app.models.game import *


@app.route('/')
def index():
    return render_template('index.html', title = 'Home')


@app.route('/<player_1_choice>/<player_2_choice>')
def check_winner(player_1_choice, player_2_choice):
    player_1 = Player('Player 1', player_1_choice)
    player_2 = Player('Player 2', player_2_choice)
    game = Game()
    winner = game.check_winner(player_1, player_2)
    return render_template('result.html', player_1 = player_1, player_2 = player_2, winner = winner)