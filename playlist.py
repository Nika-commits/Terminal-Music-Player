import random

class PlaylistNode:
    def __init__(self, song):
        self.song = song
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, song):
        node = PlaylistNode(song)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def traverse(self):
        current = self.head
        idx = 1
        while current:
            print(f"{idx}. {current.song}")
            current = current.next
            idx += 1

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.song)
            current = current.next
        return result

    def shuffle_recursive(self):
        lst = self.to_list()
        random.shuffle(lst)
        self.head = None
        for song in lst:
            self.add_song(song)
