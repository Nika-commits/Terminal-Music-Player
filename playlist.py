import random

class Node:
    def __init__(self, song):
        self.song = song
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, song):
        node = Node(song)
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node

    def traverse(self):
        curr = self.head
        if not curr:
            print("Playlist empty!")
        while curr:
            print(curr.song)
            curr = curr.next

    def shuffle_recursive(self):
        def to_list(node):
            if not node: return []
            return [node.song] + to_list(node.next)
        def from_list(lst):
            pl = Playlist()
            for s in lst:
                pl.add_song(s)
            return pl
        songs = to_list(self.head)
        random.shuffle(songs)
        new_pl = from_list(songs)
        self.head = new_pl.head
