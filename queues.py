class PlayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, song):
        self.queue.append(song)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None

class PartyQueue:
    def __init__(self):
        self.queue = []

    def play_next(self):
        if self.queue:
            self.queue.sort(key=lambda s: getattr(s, "votes", 0), reverse=True)
            return self.queue.pop(0)
        return None
