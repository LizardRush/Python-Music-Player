import os
import pygame
import time

# Initialize pygame mixer
pygame.mixer.init()

# Directory containing music files
music_dir = './Music'

# List all files in the music directory
if not os.path.exists("./Music"):
    os.mkdir("./Music")
music_files = [f for f in os.listdir(music_dir) if f.endswith(('.mp3', '.wav', '.ogg'))]
try:
    if not music_files:
        print("No music files found in the Music directory.")
    else:
        print("Music files found:")
        for i, file in enumerate(music_files, start=1):
            print(f"{i}. {file.removesuffix(".mp3").removesuffix(".wav").removesuffix(".ogg")}")

        while True:
            # Play music files one by one
            for file in music_files:
                print(f"Now playing: {file.removesuffix(".mp3").removesuffix(".wav").removesuffix(".ogg")}")
                pygame.mixer.music.load(os.path.join(music_dir, file))
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    continue  # Keep the program running while music is playing
                time.sleep(1)

            print("Finished playing all music files. Looping...")
except KeyboardInterrupt:
    print("\nStopping the music player.")
    pygame.mixer.music.stop()
