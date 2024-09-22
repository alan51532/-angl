
import pygame
import keyboard

pygame.mixer.init()

print('''спонсор разработки сайт Цифра и Аналог-
Профессиональные портативные рации https://stoptut.ru''')
print('''
        
        ||
        ||
        ||пп. 
        |   |
        |   |
        |___|''')

audio_playing = False

def play_wav_file(file_name):
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play(-1)  # Loop the audio file indefinitely

def stop_audio():
    pygame.mixer.music.stop()

def on_press(key):
    global audio_playing
    if keyboard.is_pressed('left shift') and keyboard.is_pressed('alt'):
        print("Left Shift + Alt pressed")
        if not audio_playing:
            play_wav_file('audio1.wav')
            audio_playing = True
        else:
            stop_audio()
            audio_playing = False

keyboard.on_press(on_press)

keyboard.wait('esc')

