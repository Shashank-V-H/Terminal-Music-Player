
import pygame
import os
import time

# Initialize pygame mixer
pygame.mixer.init()

# Supported audio file extensions
AUDIO_EXTENSIONS = ('.mp3', '.wav', '.ogg')

# Function to list all audio files in the current directory
def list_audio_files():
    files = [f for f in os.listdir() if f.endswith(AUDIO_EXTENSIONS)]
    return files

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

# Show the menu options
def show_menu():
    print("\n===== Terminal Music Player =====")
    print("1. Play Music")
    print("2. Pause Music")
    print("3. Unpause Music")
    print("4. Stop Music")
    print("5. Exit")

# Main function for the music player
def music_player():
    while True:
        # List available music files in the current directory
        music_files = list_audio_files()
        
        if not music_files:
            print("No audio files found in the current directory.")
            break

        print("\nAvailable Music Files:")
        for idx, file in enumerate(music_files, 1):
            print(f"{idx}. {file}")

        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Choose music file to play
            try:
                index = int(input(f"Enter the number of the music file (1-{len(music_files)}): "))
                if 1 <= index <= len(music_files):
                    play_music(music_files[index - 1])
                else:
                    print("Invalid selection!")
            except ValueError:
                print("Please enter a valid number.")
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
