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
room_graph=literal_eval(open(map_file, "r").read())
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
backwards_list = []

'''
My code [and comments] will start here
'''
print("Houston, you read me? We are starting without you.")
# I need a dictionary for my rooms
# I need a to create a set for my visited rooms
# And maybe someway to signal my truthy flag for a while loop that I visited all the rooms

# I need two helper functions
## One to add a room to my graphs dictionary
## And another to show me what are my current options for exits
## Both of these will be used in a while loop below as the loop progresses

# Helper function 1 - Add a visited room to my graph
# Take in the current rooms id, the directions you can go, the previous room ID number and direction, use KWARGS?
# Using the rooms id as the index, instantiate a dictionary
# Create a for loop that loops of the directions you can go
## And if the direction you can go is the same as the previous rooms direction
### Use the dictionary created above to set the value of the key of the previous rooms ID to the previous rooms ID
## Otherwise
### Use the dictionary created above to set the value of the key of the previous rooms ID to a "?" per spec





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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
