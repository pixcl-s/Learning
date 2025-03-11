
# There is a party at SoftUni.
# Many guests are invited, and there are two types of them:
# Regular and VIP.
# When a guest comes, check if they exist on any of the two reservation lists.
# On the first line, you will receive the number of guests – N.
# On the following N lines, you will be receiving their reservation codes.
# All reservation codes are 8 characters long,
# and all VIP numbers will start with a digit. Keep in mind that all reservation numbers must be unique.
# After that, you will be receiving guests who came to the party until you read the "END" command.
# In the end, print the number of guests who did not come to the party and their reservation numbers:
# ⦁	The VIP guests must be first.
# ⦁	Both the VIP and the Regular guests must be sorted in ascending order.

# list_of_guests = set()
#
# for _ in range(int(input())):
#     list_of_guests.add(input())
#
# while True:
#     arriving = input()
#     if arriving == "END":
#         break
#
#     if arriving in list_of_guests:
#         list_of_guests.remove(arriving)
#
# print(len(list_of_guests))
# print("\n".join(sorted(list_of_guests)))

vip = set()
guests = set()

for _ in range(int(input())):
    reservation = input()
    if reservation[0].isdigit():
        vip.add(reservation)
    else:
        guests.add(reservation)

while True:
    arriving = input()
    if arriving == "END":
        break

    if arriving in vip:
        vip.remove(arriving)
    elif arriving in guests:
        guests.remove(arriving)

print(len(vip) + len(guests))
print("\n".join(sorted(vip)))
print("\n".join(sorted(guests)))

# 100/100
