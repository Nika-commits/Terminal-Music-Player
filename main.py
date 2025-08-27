from song import Song
from playlist import Playlist
from queues import PlayQueue, PartyQueue
from stack import History
import pygame
import os

# --- Initialize Pygame Mixer ---
pygame.mixer.init()

# --- Load Songs from Folder ---
music_folder = "/home/pranish/Music"
songs = []
for file in os.listdir(music_folder):
    if file.endswith(".mp3"):
        title = os.path.splitext(file)[0]
        artist = "Unknown"
        path = os.path.join(music_folder, file)
        songs.append(Song(title, artist, path))

# --- Initialize Structures ---
playlist = Playlist()
play_queue = PlayQueue()
party_queue = PartyQueue()
history = History()

for song in songs:
    playlist.add_song(song)

# --- Track playback state ---
is_paused = False
current_song = None

# --- Menu ---
def menu():
    global is_paused, current_song
    while True:
        print("\nMenu: 1.Show Songs 2.Play Next 3.Play/Pause 4.History 5.Shuffle 6.Exit")
        choice = input("Choice: ")
        if choice == "1":
            playlist.traverse()
        elif choice == "2":
            next_song = play_queue.dequeue() or party_queue.play_next() or (playlist.head.song if playlist.head else None)
            if next_song:
                current_song = next_song
                print("Playing:", next_song)
                pygame.mixer.music.load(next_song.file_path)
                pygame.mixer.music.play()
                is_paused = False
                history.push(next_song)
            else:
                print("No songs to play!")
        elif choice == "3":
            if current_song:
                if is_paused:
                    pygame.mixer.music.unpause()
                    is_paused = False
                    print("Resumed:", current_song)
                else:
                    pygame.mixer.music.pause()
                    is_paused = True
                    print("Paused:", current_song)
            else:
                print("No song is currently playing!")
        elif choice == "4":
            history.show_history()
        elif choice == "5":
            playlist.shuffle_recursive()
            print("Playlist shuffled!")
        elif choice == "6":
            pygame.mixer.music.stop()
            break
        else:
            print("Invalid choice!")

menu()
