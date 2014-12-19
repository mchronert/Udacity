
#!/usr/bin/env python

example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."


def breakout(string_input, phrase, sub_cat, dictionary):
    """Takes a string_input, a phrase, a new category name and an 
    existing dictionary. The phrase in this case is either 'is connected 
    to' or 'likes to play'.  Based on which phrase is used, find the associated
    games or people in each sentence and assign them to a sub category in that 
    user's sub-dictionary"""
    sentences = string_input.split(".") #break into sentences
    for line in sentences:
        if line.find(phrase) != -1: # phrase determines whether we are looking for names or games
            name = line.split()[0] # name is always the first word in the sentence
            start = line.find(phrase) + len(phrase) # find where names/games start
            connections = line[start:].split(',') # breakout games or names by comma
            if name not in dictionary: # create sub dictionary for each name if not in dictionary
                dictionary[name] = {}
            clean = [] # new loop to remove space from beginning of name or game
            for c in connections:
                clean.append(c[1:]) # remove spaces from the beginning of each name/game
            dictionary[name][sub_cat] = clean # add name/game to sub category within each name
            
            """could use strip function, or split on comma + space"""

def create_data_structure(string_input):
    names = {} #create the main dictionary which will contain user names
    breakout(string_input, "is connected to", 'connections', names) # add connections
    breakout(string_input, "likes to play", 'games', names) # add games
    return names
            
def get_connections(network, user):
    if user in network:
        return network[user]['connections'] #look up used and connections in dictionary
    return None

def get_games_liked(network,user):
    if user in network:
        return network[user]['games'] # look up user and games in dictionary
    return None

def add_connection(network, user_A, user_B):
    if user_A in network and user_B in network: #determine if A and B in network
         if user_B not in network[user_A]['connections']:
            network[user_A]['connections'].append(user_B) #add user B to user A's connection list
         return network    
    return False

def add_new_user(network, user, games):
    if user not in network:
        network[user] = {'connections': [], 'games':games} #new user with unique dictionary of connections and games
    return network

def get_secondary_connections(network, user):
    if user in network:
        secondary = []
        for person in network[user]['connections']: # each connection user has
            for each in network[person]['connections']: # each connection that connection has
                secondary.append(each) # add 2nd degree connections to list
        return secondary
    return None

def connections_in_common(network, user_A, user_B):
    if user_A in network and user_B in network:
        count = 0
        for person in network[user_A]['connections']:
            # search connections in user_B's connections and add 1 if they match
            if person in network[user_B]['connections']:
                count += 1
        return count        
    return False


def path_to_friend(network, user_A, user_B, ath = None):
    if path is None:
        path = []
    if user_A not in network or user_B not in network:
        return None
    
    # Base Case
    # if connection is made, add B to path and end loop
    if user_B in network[user_A]['connections']:
        path = [user_A, user_B]
        return path  

    # General Case
    # for each person user_A connected with, run path function only 
    # if that person isn't already in the path AND only if they have connections
    path.append(user_A) # add user_A to path if not complete
    for person in network[user_A]['connections']:
        if person: # only run function if the person has connections
            if person not in path: #only search people who aren't in the path already
                if path_to_friend(network, person, user_B, path) != None: # make sure path not a dead end   
                    return [user_A].append(path_to_friend(network, person, user_B, path))
        
    

def get_game_recs(network, user):
    if user in network:
        games = []
        connections = get_connections(network, user)
        for person in connections:
            for game in network[person]['games']:
                if game not in network[user]['games'] and game not in games:
                    games.append(game)
        return games
    return None
        
net = create_data_structure(example_input)
#print net
#print get_game_recs(net, "Mercedes")
print path_to_friend(net, "John", "Jennie")





