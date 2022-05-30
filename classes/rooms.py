from classes.guests import Guests
from classes.songs import Songs


class Rooms:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.guests_list = []
        self.playlist = []

    def guests_in_room(self):
        return len(self.guests_list)

    def add_guest(self, guest):
        self.guests_list.append(guest)

    def remove_guest(self, guest):
        self.guests_list.remove(guest)

    def check_playlist(self):
        return len(self.playlist)

    # def check_playlist(self):
    #     if not self.playlist:
    #         return self.playlist

    # def add_song_to_playlist(self, song_to_add):
    #     self.playlist.append(song_to_add)
    #     return self.playlist
