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


def traverse(player, world, room_graph):
	path = []  # Keep path here
	room_stack = []  # Rooms
	room_stack.append(player.current_room.id)
	print(player.current_room.id)
	visited_rooms = set()
	# Need loop to end when len(visited_rooms) == len(world.rooms)
	while len(visited_rooms) != len(world.rooms):
		current_room = room_stack[-1]
		visited_rooms.add(current_room)
		connecting_rooms = room_graph[current_room][1]
		connecting_rooms_queue = []

		for name, con_room in connecting_rooms.items():
			if con_room not in visited_rooms:
				connecting_rooms_queue.append(con_room)

		if len(connecting_rooms_queue) != 0:
			next_room = connecting_rooms_queue[0]
			# print('NR', next_room)
			room_stack.append(next_room)

		# If the queue is empty
		else:
			room_stack.pop()
			next_room = room_stack[-1]

		for name, con_room in connecting_rooms.items():
			if con_room == next_room:

				path.append(name)
		print('room queue', connecting_rooms_queue)
		print('room stack', room_stack)

	return path


traversal_path = traverse(player, world, room_graph)


# TRAVERSAL TEST
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
#
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
