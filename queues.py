class PlayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, song):
        self.queue.append(song)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

class PartyQueue:
    def __init__(self):
        self.queue = []

    def add_song(self, song, priority=0):
        self.queue.append((priority, song))
        self.queue.sort(reverse=True)  # higher priority first

    def play_next(self):
        if self.queue:
            return self.queue.pop(0)[1]
        return None
