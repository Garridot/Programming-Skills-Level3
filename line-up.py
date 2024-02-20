import re
import time
import random

tottenham_hotspur = """
Goalkeepers
Hugo Lloris 85 pts
Guglielmo Vicario 79 pts
Fraser Forster 79 pts
Brandon Austin 79 pts
Defenders
Eric Dier 80 pts
Cristian Romero 80 pts
Davinson Sánchez 74 pts
Japhet Tanganga 70 pts
Matt Doherty 70 pts
Djed Spence 70 pts
Sergio Reguilón 74 pts
Ben Davies 76 pts
Joe Rodon 70 pts
Mislav Orsic 71 pts
Midfielders
Oliver Skipp 70 pts
Pierre-Emile Højbjerg 70 pts
Yves Bissouma 72 pts
James Maddison 74 pts
Giovani Lo Celso 78 pts
Ryan Sessegnon 80 pts
Dejan Kulusevski 60 pts
Pape Sarr 65 pts
Rodrigo Bentancur 65 pts
Oliver Skipp 65 pts
Forwards
Son Heung-Min 78 pts
Richarlison 82 pts
Bryan Gil 80 pts
Timo Werner 82 pts
Brennan Johnson 70 pts
Manor Solomon 70 pts
Alejo Véliz 75 pts
Dane Scarlett 75 pts
"""

manchester_united = """
Goalkeepers
André Onana 80 pts
Tom Heaton 75 pts
Altay Bayindir 69 pts
Defenders
Victor Lindelöf 80 pts
Harry Maguire 82 pts
Lisandro Martínez 82 pts
Tyrell Malacia 67 pts
Raphaël Varane 80 pts
Diogo Dalot 89 pts
Luke Shaw 89 pts
Aaron Wan-Bissaka 70 pts
Midfielders
Sofyan Amrabat 76 pts
Scott McTominay 80 pts
Bruno Fernandes 88 pts
Christian Eriksen 67 pts
Mason Mount 77 pts
Kobbie Mainoo 65 pts
Daniel Gore 60 pts
Forwards
Anthony Martial 50 pts
Marcus Rashford 76 pts
Antony 75 pts
Rasmus Højlund 80 pts
Alejandro Garnacho 85 pts
Facundo Pellistri: 75 pts
"""

def get_list_player(string):   
    """Responsible for extracting player information from the provided string."""  
    
    players = string.strip().splitlines() # Split the string into a list of lines
    list_players = []
    positions = ""    

    for x in players:
        if not any(char.isdigit() for char in x):
            positions = x
        else:
            player = re.sub(r'\d+', '', x).replace("pts", "").strip()
            position = positions
            points = re.sub(r'\D', '', x)

            player_data = {"player": player, "position": position, "points": points}
            list_players.append(player_data)

    return list_players   

def filter_player_by_position(team):    
    """Filters players based on their positions."""

    goalkeepers = [player for player in team if player['position'] == 'Goalkeepers']
    defenders   = [player for player in team if player['position'] == 'Defenders']
    midfielders = [player for player in team if player['position'] == 'Midfielders']
    forwards    = [player for player in team if player['position'] == 'Forwards']

    return [goalkeepers,defenders,midfielders,forwards]

def random_line_up(team):
    """Generates a random lineup for the rival team."""

    line_up = []
    players_select = []

    # Random Formation
    line_defenders   = random.randint(3, 5)  # the first line (defenders) can not be lower than 3
    line_midfielders = random.randint(2, 4)
    line_forwards    = 10 - (line_defenders + line_midfielders)  # making sure that the line-up can only consist of 10 players.

    # select Players  
    players = filter_player_by_position(team)        
     
    players_select.append( random.sample(players[0], 1) ) # select a random goalkeeper     
    players_select.append( random.sample(players[1], line_defenders) ) # select random defenders by formation line    
    players_select.append( random.sample(players[2], line_midfielders) ) # select random midfielders by formation line     
    players_select.append( random.sample(players[3], line_forwards) ) # select random forwards by formation line    

   
    print("\nYour Rival: Tottenham Hotspur") 
    index = 0
    for i in players_select:
        for x in i:
            index += 1
            print(f"{index}. {x['player']}, GRL: {x['points']}")
            line_up.append(x)

    print(f"Formation: {line_defenders}-{line_midfielders}-{line_forwards}\n")          

    return line_up   

def show_options_players(players):  
    """Displays options for player selection to the user."""

    for index, player in enumerate(players):
        print(f"{index}. {player['player']}, GRL: {player['points']}")

class SetUserLineUp:
    """Manages the user's selected lineup and related operations."""

    def __init__(self,players):
        self.players = players
        self.line_up = []
   
    def select_player(self,position,select):
        """This function allows the user to add a selected player to their line-up."""
        players = self.players[position]

        if 0 <= select < len(players):
            player = players[select]
            self.line_up.append(player)
            print(f"{player['player']} has been selected!")
            return True

        print(f"\nError: The ID {select} has not been found. Try Again\n")
        return False

    def remove_player(self,position): 
        """In case of an error, the function will remove the most recently added player."""
        indices_to_remove = [index for index, player in enumerate(self.line_up) if player['position'] == position]

        for index in reversed(indices_to_remove):
            self.line_up.pop(index)
         

    def get_line_up(self):
        """Return the line-up"""
        return self.line_up                             

def select_goalkeepers(goalkeepers):
    """Handles the selection of goalkeepers by the user."""
    
    print(f"\nSelect the ID of a goalkeeper:")
    show_options_players(goalkeepers)
    goalkeeper_id = input()

    try:
        goalkeeper_id = int(goalkeeper_id)
    except ValueError:
        print("Error: Invalid Format. Try Again")
        return False

    # Adding the player to line-up
    return line_up.select_player(position=0, select=goalkeeper_id)

def select_players(formation,player,position_id,position):
    """Handles the selection of players (defenders, midfielders, forwards) by the user."""

    print(f'\nSelect the ID of {formation} {position.lower()}, in this format, "1,2,3,4..."')
    show_options_players(player) 
    players_select = input()

    try:
        list(map(int, players_select.split(',')))    
    except ValueError: 
        print(f'\nError: The selection of players must follow this format: "1,2,3,4...". Try Again')
        return False

    players_select = players_select.split(",")
    
    if len(players_select) != int(formation):
        print(f"\nError: Select {formation} {position.lower()}. Try Again")
        return False   
    
    continue_loop = True

    for i in players_select:            
        if not line_up.select_player(position=position_id, select=int(i)):                          
            line_up.remove_player(position)
            continue_loop = False  # Set the flag to False if select_player returns False
            break  # Break out of the for loop

    return continue_loop 

def select_formation():
    """Takes user input for selecting the formation."""

    formation_input = input('Enter Your Formation in this format, example "4-3-3": ')

    try: list(map(int, formation_input.split('-')))
    except ValueError:
        print(f'\nError: The selection of formation must follow this format: "4-3-3". Try Again')
        return False

    if len(formation_input.split('-')) != 3:
        print (f"\nError: You are only allowed to enter a line-up with three lines. Try Again")
        return False              

    formation = formation_input.replace("-", "")
    len_formation = sum(int(digit) for digit in formation)

    if len_formation != 10:
        print("Error: The team should have exactly 10 players in their lineup. Try Again")
        return False

    return True, formation  

def match_result(user_team,rival_team):
    """Computes and displays the match result between the user's team and the rival team."""
    
    user_grl  = sum([int(player["points"]) for player in user_team]) / len(user_team)
    rival_grl = sum([int(player["points"]) for player in rival_team]) / len(rival_team)

    user_grl  = str(user_grl) 
    rival_grl = str(rival_grl)

    user_goals  = random.randint(0, abs(int(user_grl[0])  - int(user_grl[1])))  # Ensure user_goals is non-negative
    rival_goals = random.randint(0, abs(int(rival_grl[0]) - int(rival_grl[1]))) # Ensure rival_goals is non-negative

    print("\nManchester United vs Tottenham Hotspur has kicked off!")
    time.sleep(1.5) # Sleep for 1.5 seconds
    print(f"\nHalf Time: Manchester United: {int(user_goals / 2)} - {int(rival_goals / 2)} Tottenham Hotspur.")  
    time.sleep(3) # Sleep for 1.5 seconds
    print(f"\nFull Time: Manchester United: {user_goals} - {rival_goals} Tottenham Hotspur.")


if __name__ == '__main__':
    # get the team's players
    tottenham_players  = get_list_player(tottenham_hotspur)
    manchester_players = get_list_player(manchester_united)

    # generate a random rival line-up
    rival_team = random_line_up(tottenham_players)

    print("Your Team: Manchester United")

    while True:
        formation = select_formation()
        if formation:
            break

    players = filter_player_by_position(manchester_players)
    line_up = SetUserLineUp(players)
    
    # Filter players by position
    goalkeepers = players[0]  
    defenders   = players[1]
    midfielders = players[2]
    forwards    = players[3]

    while True:
        goalkeeper = select_goalkeepers(goalkeepers)
        if goalkeeper: 
            break

    # Select defenders
    while True:
        defender = select_players(formation[1][0],defenders,1,"Defenders") 
        if defender: 
            break 

    # Select midfielders
    while True:
        midfielder = select_players(formation[1][1],midfielders,2,"Midfielders") 
        if midfielder: 
            break 

    # Select forwards
    while True:
        forwards = select_players(formation[1][2],forwards,3,"Forwards") 
        if forwards: 
            break 

    # View user Line-up     
    user_team  = line_up.get_line_up()  
    print("\nManchester United | Your Line-up:")        
    show_options_players(user_team)      

    print("\nTottenham Hotspur | Rival Line-up:") 
    show_options_players(rival_team)

    # Result of the game
    match_result(user_team,rival_team)