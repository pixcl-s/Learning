
# On the first line, you will be given an integer n representing the number of rooms in the business center.
# On the following n lines for each room, you will receive information about the chairs in the room
# and the number of visitors. Each chair will be presented with the char "X".
# Next, there will be a single space and the number of visitors at the end.
# For example: "XXXXX 4" (5 chairs and 4 visitors).
# Keep track of the free chairs:
# If there are not enough chairs in a specific room, print the following message:
# "{needed_chairs_in_room} more chairs needed in room {number_of_room}".
# The rooms start from 1.
# Otherwise, print:
# "Game On, {total_free_chairs} free chairs left".

rooms = int(input())

free_chairs = 0

room_needing_chairs = []
amount_of_chairs_needed = []


for x in range(1, rooms+1):
    chairs_guests = input().split()

    if len(chairs_guests[0]) >= int(chairs_guests[1]):
        free_chairs += len(chairs_guests[0]) - int(chairs_guests[1])
    elif len(chairs_guests[0]) < int(chairs_guests[1]):
        room_needing_chairs.append(x)
        amount_of_chairs_needed.append(int(chairs_guests[1]) - len(chairs_guests[0]))


if len(room_needing_chairs) == 0:
    print(f"Game On, {free_chairs} free chairs left")
else:
    for x in range(0, len(room_needing_chairs)):
        print(f"{amount_of_chairs_needed[x]} more chairs needed in room {room_needing_chairs[x]}")
