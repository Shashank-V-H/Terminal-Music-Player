
import pygame
import os
import random
import time

# Initialize pygame mixer
pygame.mixer.init()

# Supported audio file extensions
AUDIO_EXTENSIONS = ('.mp3', '.wav', '.ogg')

# Function to list all audio files in the current directory
def list_audio_files():
    return [f for f in os.listdir() if f.endswith(AUDIO_EXTENSIONS)]

# Function to play music
def play_music(music_file):
    if os.path.exists(music_file):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(loops=0, start=0.0)
        print(f"Now playing: {music_file}")
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

# Function to play the next song
def play_next(playlist, current_index):
    if current_index < len(playlist) - 1:
        return current_index + 1
    else:
        print("You're at the last song. Starting from the beginning.")
        return 0

# Function to play the previous song
def play_previous(playlist, current_index):
    if current_index > 0:
        return current_index - 1
    else:
        print("You're at the first song. Moving to the last song.")
        return len(playlist) - 1

# Function to shuffle the playlist
def shuffle_playlist(playlist):
    random.shuffle(playlist)
    print("Playlist shuffled.")

# Show the menu options
def show_menu():
    print("\n===== Terminal Music Player =====")
    print("1. Play Music")
    print("2. Pause Music")
    print("3. Unpause Music")
    print("4. Stop Music")
    print("5. Next Song")
    print("6. Previous Song")
    print("7. Shuffle Playlist")
    print("8. Exit")

# Main function for the music player
def music_player():
    playlist = list_audio_files()
    if not playlist:
        print("No audio files found in the current directory.")
        return

    current_index = 0
    auto_play = True  # Enable auto-play by default

    while True:
        print("\nAvailable Music Files:")
        for idx, file in enumerate(playlist, 1):
            marker = "->" if idx - 1 == current_index else "  "
            print(f"{marker} {idx}. {file}")

        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            play_music(playlist[current_index])
        elif choice == '2':
            pause_music()
        elif choice == '3':
            unpause_music()
        elif choice == '4':
            stop_music()
        elif choice == '5':
            current_index = play_next(playlist, current_index)
            play_music(playlist[current_index])
        elif choice == '6':
            current_index = play_previous(playlist, current_index)
            play_music(playlist[current_index])
        elif choice == '7':
            shuffle_playlist(playlist)
            current_index = 0  # Reset to the first song after shuffle
        elif choice == '8':
            stop_music()
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please choose again.")
        
        # Auto-play: Play the next song when the current song ends
        if auto_play and not pygame.mixer.music.get_busy():
            current_index = play_next(playlist, current_index)
            play_music(playlist[current_index])
        
        time.sleep(1)

# Run the music player
if __name__ == "__main__":
    music_player()
