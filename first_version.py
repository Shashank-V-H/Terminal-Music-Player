
import pygame
import os
import time

# Initialize pygame mixer
pygame.mixer.init()

# Function to play music
def play_music(music_file):
    if os.path.exists(music_file):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(loops=0, start=0.0)
        print(f"Playing {music_file}")
    else:
        print("File not found!")

# Function to pause music
def pause_music():
    pygame.mixer.music.pause()
    print("Music paused.")

# Function to unpause music
def unpause_music():
    pygame.mixer.music.unpause()
    print("Music resumed.")

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()
    print("Music stopped.")

def show_menu():
    print("\n===== Terminal Music Player =====")
    print("1. Play Music")
    print("2. Pause Music")
    print("3. Unpause Music")
    print("4. Stop Music")
    print("5. Exit")

# Main function
def music_player():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            music_file = input("Enter the path of the music file: ")
            play_music(music_file)
        elif choice == '2':
            pause_music()
        elif choice == '3':
            unpause_music()
        elif choice == '4':
            stop_music()
        elif choice == '5':
            stop_music()
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please choose again.")
        time.sleep(1)

# Run the music player
if __name__ == "__main__":
    music_player()
