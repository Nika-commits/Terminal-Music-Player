class History:
    def __init__(self):
        self.stack = []

    def push(self, song):
        self.stack.append(song)

    def show_history(self):
        print("\nListening History:")
        for idx, song in enumerate(reversed(self.stack), 1):
            print(f"{idx}. {song}")
