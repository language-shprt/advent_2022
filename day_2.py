"""
Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
What would your total score be if everything goes exactly according to your strategy guide?
"""

player_choice = {
    'A': 1, #rock
    'X': 1, #rock
    'B': 2, #paper
    'Y': 2, #paper
    'C': 3, #scissors
    'Z': 3, #scissors
}

game_rules = {
    'X': 'C', # Rock defeats Scissors
    'Y': 'A', # Paper defeats Rock
    'Z': 'B' # Scissors defeats Paper
}

round_score = {
    'lost': 0,
    'draw': 3,
    'won': 6
}

with  open('day_2_input.txt', encoding='utf-8') as input_data:
    game_pairs = input_data.readlines()

game_pairs = [pair.replace('\n','')  for pair in game_pairs]

# Part 1

game_score = 0
for i in range(len(game_pairs)):
    player_1_choice = game_pairs[i][0]
    player_2_choice = game_pairs[i][2]
    player_1_score = player_choice[game_pairs[i][0]]
    player_2_score = player_choice[game_pairs[i][2]]
    if player_1_score == player_2_score:
        score = player_2_score + round_score['draw']
        game_score = game_score + score
    elif game_rules[player_2_choice] == player_1_choice:
        score = player_2_score + round_score['won']
        game_score = game_score + score
    else:
        score = player_2_score
        game_score = game_score + score
print(game_score)

# Part 2
# new input re the rules

player_choice = {
    'A': 1, #rock
    'B': 2, #paper
    'C': 3, #scissors
}

game_rules = {
    'A': 'C', # Rock defeats Scissors
    'B': 'A', # Paper defeats Rock
    'C': 'B' # Scissors defeats Paper
}

game_rules_2 = {
    'X': 'lost',
    'Y': 'draw',
    'Z': 'won'
}

game_score = 0
for i in range(len(game_pairs)):
    player_1_choice = game_pairs[i][0]
    round_result = game_rules_2[game_pairs[i][2]]
    player_1_score = player_choice[player_1_choice]
    if round_result == 'draw':
        player_2_choice = player_1_choice
        player_2_score = player_1_score
        score = player_2_score + round_score['draw']
        game_score = score + game_score
    elif round_result == 'lost':
        player_2_choice = game_rules[player_1_choice]
        player_2_score = player_choice[player_2_choice]
        score = player_2_score + round_score['lost']
        game_score = score + game_score
    else:
        game_rules_reversed  = dict((value, key) for key, value in game_rules.items())
        player_2_choice = game_rules_reversed[player_1_choice]
        player_2_score = player_choice[player_2_choice]
        score = player_2_score + round_score['won']
        game_score = score + game_score

print(game_score)