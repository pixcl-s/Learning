from typing import List
from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> None:
        for x in self.rooms:
            if x.number == room_number:
                if x.guests == 0:
                    x.take_room(people)
                    if x.is_taken:
                        self.guests += people
                return

    def free_room(self, room_number: int) -> None:
        for x in self.rooms:
            if x.number == room_number:
                humans = x.guests
                x.free_room()
                if not x.is_taken:
                    self.guests -= humans
                return

    def status(self) -> str:
        free_rooms = []
        taken_rooms = []
        for x in self.rooms:
            if x.is_taken:
                taken_rooms.append(x.number)
            else:
                free_rooms.append(x.number)
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(str(y) for y in free_rooms)}\n" \
               f"Taken rooms: {', '.join(str(y) for y in taken_rooms)}"
