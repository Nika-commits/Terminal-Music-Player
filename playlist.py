class Node:
    def __init__(self, song):
        self.song = song
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_song(self, song):
        new_node = Node(song)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def traverse(self):
        current = self.head
        idx = 1
        while current:
            print(f"{idx}. {current.song}")
            current = current.next
            idx += 1

    def shuffle_recursive(self):
        import random
        nodes = []
        current = self.head
        while current:
            nodes.append(current.song)
            current = current.next
        random.shuffle(nodes)
        self.head = self.tail = None
        for song in nodes:
            self.add_song(song)
