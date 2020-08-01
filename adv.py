from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
'''
We will need a second list per spec, added that below
'''
reversed_list = []
'''
My code [and comments] will start here
'''
print("Houston, you read me? We are starting without you.")
# I need a dictionary for my rooms
bobs_room_graph = {}
# I need a to create a set for my visited rooms
visited_rooms = set()
# I need a dictionary that points to the opposite directions. This is used in conjunction with the reversed list.
reversed_directions = {
    "n": "s",
    "s": "n",
    "w": "e",
    "e": "w"
}
# And maybe someway to signal my truthy flag for a while loop that I visited all the rooms
all_rooms_visited = False


# I need two helper functions
## One to add a room to my graphs dictionary
## And another to show me what are my current options for exits
## Both of these will be used in a while loop below as the loop progresses

# Helper function 1 - Add a visited room to my graph
# Take in the current rooms id, the directions you can go, the previous room ID number and direction, use KWARGS?
def add_to_graph(players_current_room_id, directions, previous_room=None, previous_room_direction=None):
    # Using the rooms id as the index, instantiate a dictionary
    bobs_room_graph[players_current_room_id] = {}
    # Create a for loop that loops of the directions you can go
    for direction in directions:
        ## And if the direction you can go is the same as the previous rooms direction
        if direction == previous_room_direction:
            ### Use the dictionary created above to set the value of the key of the previous rooms ID to the previous rooms ID
            bobs_room_graph[players_current_room_id][direction] = previous_room
        ## Otherwise
        else:
            ### Use the dictionary created above to set the value of the key of the previous rooms ID to a "?" per spec
            bobs_room_graph[players_current_room_id][direction] = "?"


# Helper Function 2 - Getting the available moves inside a room
# Take in all the directions you can go that you know of
def get_directions(players_available_directions):
    # Instantiate a list
    directions = []
    # Create a loop that loops over the directions you can go that you know of
    for direction in players_available_directions:
        ## If the value of the key of the rooms index is "?"
        if bobs_room_graph[players_current_room_id][direction] == "?":
            ### Add the known directions to the instantiated list above
            directions.append(direction)
    # return the list of directions
    return directions


'''
Now time for our main event
'''


## Start off in our first room
add_to_graph(player.current_room.id, player.current_room.get_exits())

# Create a while loop that runs until all rooms are visited
while not all_rooms_visited:
    ## Using the imported player class, get the exits from the current room
    players_available_directions = player.current_room.get_exits()
    ## Get the current room id from the player class
    players_current_room_id = player.current_room.id
    ## Maybe print out the data in a user friendly way?
    print(f"Current room: {players_current_room_id} - {players_available_directions}")
    print("~" * 10+ "+" * 10+"~" * 10,)

    ## Find the players available moves
    available_moves = get_directions(players_available_directions)

    ## Loop through the available directions to go
    for direction in players_available_directions:
        ## If the value of the key of the current rooms available direction is "?"
        if bobs_room_graph[players_current_room_id][direction] == "?":
            ## Add that option to the available moves list
            available_moves.append(direction)
    ## If the length of the available moves list is 0
    if len(available_moves) == 0:
        ## Then check if the length of the reversed list is 0
        if len(reversed_list) == 0:
            ## if it is, then set all rooms are visited value to True
            all_rooms_visited = True
        ## Othersise
        else:
            ## Reduce the reversed list by 1
            movement = reversed_list.pop(-1)
            ## Add to the Traversal Path the room that was removed from the reversed list above
            traversal_path.append(movement)
            ## Move the player using the player class
            player.travel(movement)
            ## In case we get back to first room, reset return sequence by checking the
            ## players current room against the worlds starting room
            if player.current_room.id == world.starting_room:
                reversed_list = []
    ## Otherwise
    else:
        ## Grab the first available move and maybe print that out to be user friendly?
        movement = available_moves[0]
        ## Add the direction your heading to the traversal path list
        traversal_path.append(movement)
        ## Add the exact opposite direction your heading in to the reversed list
        reversed_list.append(reversed_directions[movement])
        ## Using the player class, move the player
        player.travel(movement)
        ## Grab the players current room using the players class
        players_new_room_id = player.current_room.id
        ## Set the value of the the key of the index of my rooms graph to the value of the room id above
        bobs_room_graph[players_current_room_id][movement] = players_new_room_id
        ## If the players room id does not exist in the players visited rooms set
        if players_new_room_id not in visited_rooms:
            ## Then we add the new room to the visited rooms list
            visited_rooms.add(players_new_room_id)
            ## And then add the players room id to the graph using the first helper function
            add_to_graph(players_new_room_id, player.current_room.get_exits(), players_current_room_id, reversed_directions[movement])


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
