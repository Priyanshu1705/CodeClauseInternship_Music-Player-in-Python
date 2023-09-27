import pygame

def initialize_music_player():
    pygame.init()
    pygame.mixer.init()

def play_music(file_path):
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    except pygame.error:
        print("Couldn't play the audio file.")

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def main():
    print("Simple Music Player")
    print("-------------------")
    
    file_path = input("Enter the path to the audio file: ")
    
    initialize_music_player()
    play_music(file_path)

    while True:
        action = input("Enter 'p' to pause, 'u' to unpause, 's' to stop, or 'q' to quit: ").lower()
        
        if action == 'p':
            pause_music()
        elif action == 'u':
            unpause_music()
        elif action == 's':
            stop_music()
            break
        elif action == 'q':
            stop_music()
            break

    pygame.mixer.quit()
    pygame.quit()

if __name__ == "__main__":
    main()