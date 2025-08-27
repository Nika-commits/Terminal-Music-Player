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
        name_part = os.path.splitext(file)[0]
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

current_node = playlist.head
paused = False

# --- Functions ---
def play_song(node):
    global current_node, paused
    if not node:
        print("No song to play!")
        return
    pygame.mixer.music.load(node.song.path)
    pygame.mixer.music.play()
    current_node = node
    paused = False
    print(f"Playing: {node.song}")
    history.push(node.song)

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

def play_next():
    global current_node
    if current_node.next:
        play_song(current_node.next)
    else:
        print("End of playlist reached!")

def play_previous():
    global current_node
    if current_node.prev:
        play_song(current_node.prev)
    else:
        print("Start of playlist reached!")

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
            play_song(current)
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number!")

def menu():
    while True:
        print("\nMenu: \n\n1.Show Songs \n2.Play Next \n3.Play Previous \n4.Play by Number \n5.History \n6.Shuffle \n7.Play/Pause \n8.Exit")
        choice = input("\n Enter your Choice: ")

        if choice == "1":
            playlist.traverse()
        elif choice == "2":
            play_next()
        elif choice == "3":
            play_previous()
        elif choice == "4":
            play_by_number()
        elif choice == "5":
            history.show_history()
        elif choice == "6":
            playlist.shuffle_recursive()
            print("Playlist shuffled!")
        elif choice == "7":
            toggle_pause()
        elif choice == "8":
            pygame.mixer.music.stop()
            break
        else:
            print("Invalid choice!")

menu()
