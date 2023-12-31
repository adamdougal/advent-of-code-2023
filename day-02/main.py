import re

def strip_game_prefx(line):
    m = re.search(r'Game [0-9]+: (.*)', line)
    return m.group(1)


def parse_reveal(reveal):
    parsed_reveal = {}
    colours_count = reveal.split(', ')
    
    for colour_count in colours_count:
        m = re.search(r'([0-9]+) ([a-z]+)', colour_count)
        count = int(m.group(1))
        colour = m.group(2)
        parsed_reveal[colour] = count
        
    return parsed_reveal
    
    
def parse_game(game):
    reveals = strip_game_prefx(game).split('; ')
    parsed_game = []
    
    for reveal in reveals:
        parsed_game.append(parse_reveal(reveal))
                
    return parsed_game
    

def parse_input(filePath):
    games = []
    
    with open(filePath) as f:
        lines = f.readlines()
        for line in lines:
            game = parse_game(line)
            games.append(game)
        
    return games


def game_possible(game, max_colours):
    for reveal in game:
        for colour in max_colours:
            if colour not in reveal:
                continue

            if reveal[colour] > max_colours[colour]:
                return False
        
    return True


def id_sum_of_games_possible(file_path, max_colours):
    games = parse_input(file_path)
    possible_games = 0
    i = 0
    for game in games:
        i += 1
        if game_possible(game, max_colours):
            possible_games += i
            
    return possible_games

def power(colours):
    result = 1
    for colour in colours:
        result *= colours[colour]
        
    return result

def minimum_required_for_game(game):
    min_required = {
        'red': 0,
        'blue': 0,
        'green': 0
    }
    
    for reveal in game:
        for colour in reveal:
            if reveal[colour] > min_required[colour]:
                min_required[colour] = reveal[colour]
        
    return min_required

def sum_of_minimum_powers(file_path):
    games = parse_input(file_path)
    sum_of_powers = 0
    
    for game in games:
        min_required = minimum_required_for_game(game)
        sum_of_powers += power(min_required)
        
    return sum_of_powers

if __name__ == "__main__":
    max_colours = {'red': 12, 'blue': 14, 'green': 13}
    file_path = 'input.txt'
    print(id_sum_of_games_possible(file_path, max_colours))
    print(sum_of_minimum_powers(file_path))