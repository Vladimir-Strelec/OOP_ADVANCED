from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        possible_rooms = [x for x in self.rooms if x.number == room_number]
        room = possible_rooms[0]
        if room.capacity >= people and room.is_taken != True:
            self.guests += people
        return room.take_room(people)

    def free_room(self, room_number):
        not_possible_room = [x for x in self.rooms if x == room_number]
        if not_possible_room:
            room = not_possible_room[0]
            self.guests -= room.guests
            return room.free_room()

    def status(self):
        result = f"Hotel {self.name} has {self.guests} total guests\n"
        result += f"Free rooms: {', '.join([str(i.number) for i in self.rooms if i.is_taken is False])}\n"
        result += f"Taken rooms: {', '.join([str(i.number) for i in self.rooms if not i.is_taken is False])}"
        return result


