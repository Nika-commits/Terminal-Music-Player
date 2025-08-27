class History:
    def __init__(self):
        self.stack = []

    def push(self, song):
        self.stack.append(song)

    def show_history(self):
        if not self.stack:
            print("No history yet!")
        for s in reversed(self.stack):
            print(s)
