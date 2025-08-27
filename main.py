import os
import pygame
import time
from song import Song
from playlist import Playlist
from queues import PlayQueue, PartyQueue
from stack import History

# --- Initialize pygame mixer ---
pygame.mixer.init()

# --- Load Songs from Music Folder ---
music_folder = "/home/pranish/Music"
songs = []

for file in os.listdir(music_folder):
    if file.endswith(".mp3"):
        name_part = os.path.splitext(file)[0]  # remove .mp3
        if " - " in name_part:
            title, artist = name_part.split(" - ", 1)
        else:
            title = name_part
            artist = "Unknown"
        path = os.path.join(music_folder, file)
        songs.append(Song(title.strip(), artist.strip(), path))

# --- Initialize Structures ---
playlist = Playlist()
play_queue = PlayQueue()
party_queue = PartyQueue()
history = History()

for song in songs:
    playlist.add_song(song)

current_song = None
paused = False

# --- Functions ---
def play_song(song):
    global current_song, paused
    if not song:
        print("No song to play!")
        return
    if current_song != song:
        pygame.mixer.music.load(song.path)
        pygame.mixer.music.play()
        current_song = song
        paused = False
    print(f"Playing: {song}")

def toggle_pause():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
        print("Resumed")
    else:
        pygame.mixer.music.pause()
        paused = True
        print("Paused")

def play_by_number():
    playlist.traverse()
    try:
        choice = int(input("Enter song number to play: "))
        current = playlist.head
        idx = 1
        while current and idx < choice:
            current = current.next
            idx += 1
        if current:
            play_song(current.song)
            history.push(current.song)
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number!")

def menu():
    while True:
        print("\nMenu: 1.Show Songs 2.Play Next 3.Play by Number 4.History 5.Shuffle 6.Play/Pause 7.Exit")
        choice = input("Choice: ")

        if choice == "1":
            playlist.traverse()
        elif choice == "2":
            next_song = play_queue.dequeue() or party_queue.play_next() or playlist.head.song
            play_song(next_song)
            history.push(next_song)
        elif choice == "3":
            play_by_number()
        elif choice == "4":
            history.show_history()
        elif choice == "5":
            playlist.shuffle_recursive()
            print("Playlist shuffled!")
        elif choice == "6":
            toggle_pause()
        elif choice == "7":
            pygame.mixer.music.stop()
            break
        else:
            print("Invalid choice!")

menu()
