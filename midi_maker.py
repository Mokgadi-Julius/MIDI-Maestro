import random
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from music21 import note, chord, stream, instrument
import datetime
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Define scales
scales = {
    "major": ["C", "D", "E", "F", "G", "A", "B"],
    "minor": ["C", "D", "Eb", "F", "G", "Ab", "Bb"]
}

# Define keys
keys = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "G#", "A", "Bb", "B"]

# Define moods/genres
moods = {
    "happy": {"scale": "major", "rhythms": [1.0, 0.5], "dynamics": ['mf', 'f', 'ff']},
    "sad": {"scale": "minor", "rhythms": [2.0, 1.0], "dynamics": ['pp', 'p', 'mf']}
}

# Define complexities
complexities = {
    "low": {"chords": 4, "notes": 8, "rhythms": [1.0, 2.0]},
    "medium": {"chords": 6, "notes": 12, "rhythms": [1.0, 0.5, 2.0]},
    "high": {"chords": 8, "notes": 16, "rhythms": [0.5, 1.0, 2.0, 4.0]}
}

def generate_rhythm_sequence(total_beats, rhythms):
    rhythm_sequence = []
    total_length = 0.0

    # Basic rhythm pattern
    basic_pattern = [1.0, 0.5, 0.5] * total_beats

    while total_length < total_beats:
        beat = random.choice(basic_pattern)

        # Check if adding this beat will exceed the total beats
        if total_length + beat > total_beats:
            continue

        rhythm_sequence.append(beat)
        total_length += beat

    return rhythm_sequence

def generate_music(key, mood, music_type, complexity, bars, beats_per_bar):
    bars = int(bars)
    beats_per_bar = int(beats_per_bar)

    # Get the appropriate scale and modify it according to the key
    scale_type = moods[mood]["scale"]
    scale = [n if not n.startswith("C") else key for n in scales[scale_type]]

    # Get the mood-specific rhythms and dynamics
    dynamics = moods[mood]["dynamics"]

    # Get the complexity-specific chords, notes, and rhythms
    num_chords = min(complexities[complexity]["chords"], len(scale))
    num_notes = complexities[complexity]["notes"]
    rhythms = complexities[complexity]["rhythms"]

    # Generate a music21 stream and add a piano instrument
    music_stream = stream.Stream()
    music_stream.append(instrument.Piano())

    for _ in range(bars):
        if music_type != "melody":
            # Generate chord progression
            num_chords = beats_per_bar  # Number of chords is now set by the "beats_per_bar" setting
            chords = random.choices(scale, k=num_chords)  # Randomly select chords in the chosen scale
            rhythm_sequence = generate_rhythm_sequence(beats_per_bar, rhythms)  # Generate rhythm sequence

            for i, c in enumerate(chords):
                dyn = random.choice(dynamics)
                ch = chord.Chord([c, scale[(scale.index(c) + 2) % len(scale)], scale[(scale.index(c) + 4) % len(scale)]], quarterLength=rhythm_sequence[i % len(rhythm_sequence)])
                ch.lyric = dyn
                music_stream.append(ch)

        if music_type != "chords":
            # Generate melody
            num_notes = beats_per_bar  # Number of melody notes is now set by the "beats_per_bar" setting
            melody_notes = random.choices(scale, k=num_notes)  # Randomly select a sequence of notes in the scale for the melody
            rhythm_sequence = generate_rhythm_sequence(beats_per_bar, rhythms)  # Generate rhythm sequence

            for i, m in enumerate(melody_notes):
                dyn = random.choice(dynamics)
                nt = note.Note(m, quarterLength=rhythm_sequence[i % len(rhythm_sequence)])
                nt.lyric = dyn
                music_stream.append(nt)

    return music_stream

def play_music(music_stream):
    if music_stream:
        # Generate the timestamp and append it to the filename
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f'temp_{timestamp}.mid'

        # Write to a MIDI file using music21
        music_stream.write('midi', fp=filename)

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

def save_music(music_stream):
    if music_stream:
        # Generate the timestamp and append it to the filename
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f'music_{timestamp}.mid'

        # Write to a MIDI file using music21
        music_stream.write('midi', fp=filename)

        return filename

# Initialize GUI
root = tk.Tk()
root.geometry("600x400")
root.title("MIDI Music Generator")

# Apply theme
style = ThemedStyle(root)
style.set_theme("arc")  # you can change the theme to one you prefer

# Define frames
key_frame = ttk.Frame(root)
mood_frame = ttk.Frame(root)
type_frame = ttk.Frame(root)
complexity_frame = ttk.Frame(root)
bars_frame = ttk.Frame(root)
beats_per_bar_frame = ttk.Frame(root)
button_frame = ttk.Frame(root)

# Pack frames
key_frame.pack(pady=10)
mood_frame.pack(pady=10)
type_frame.pack(pady=10)
complexity_frame.pack(pady=10)
bars_frame.pack(pady=10)
beats_per_bar_frame.pack(pady=10)
button_frame.pack(pady=10)

# Generate music object
music_stream = None

def generate_midi():
    global music_stream
    music_stream = generate_music(key_var.get(), mood_var.get(), music_type_var.get(), complexity_var.get(), bars_var.get(), beats_per_bar_var.get())

def play_music_wrapper():
    play_music(music_stream)

def save_music_wrapper():
    save_music(music_stream)

# Drop-down menus and radio buttons
key_var = tk.StringVar(root)
key_var.set("C")  # default value
key_option_menu = ttk.Combobox(key_frame, textvariable=key_var, values=keys)
key_option_menu.pack(side='left')
ttk.Label(key_frame, text="Select Key:").pack(side='left')

mood_var = tk.StringVar(root)
mood_var.set("happy")  # default value
mood_option_menu = ttk.Combobox(mood_frame, textvariable=mood_var, values=list(moods.keys()))
mood_option_menu.pack(side='left')
ttk.Label(mood_frame, text="Select Mood:").pack(side='left')

music_type_var = tk.StringVar(root)
music_type_var.set("both")  # default value
music_type_radio1 = ttk.Radiobutton(type_frame, text="Chords", variable=music_type_var, value="chords")
music_type_radio1.pack(side='left')
music_type_radio2 = ttk.Radiobutton(type_frame, text="Melody", variable=music_type_var, value="melody")
music_type_radio2.pack(side='left')
music_type_radio3 = ttk.Radiobutton(type_frame, text="Both", variable=music_type_var, value="both")
music_type_radio3.pack(side='left')
ttk.Label(type_frame, text="Select Music Type:").pack(side='left')

complexity_var = tk.StringVar(root)
complexity_var.set("low")  # default value
complexity_option_menu = ttk.Combobox(complexity_frame, textvariable=complexity_var, values=list(complexities.keys()))
complexity_option_menu.pack(side='left')
ttk.Label(complexity_frame, text="Select Complexity:").pack(side='left')

bars_var = tk.StringVar(root)
bars_var.set("1")  # default value
bars_option_menu = ttk.Combobox(bars_frame, textvariable=bars_var, values=["1", "2", "4", "8", "16"])
bars_option_menu.pack(side='left')
ttk.Label(bars_frame, text="Select Bars:").pack(side='left')

beats_per_bar_var = tk.StringVar(root)
beats_per_bar_var.set("4")  # default value
beats_per_bar_option_menu = ttk.Combobox(beats_per_bar_frame, textvariable=beats_per_bar_var, values=["2", "3", "4", "6", "8"])
beats_per_bar_option_menu.pack(side='left')
ttk.Label(beats_per_bar_frame, text="Select Beats Per Bar:").pack(side='left')

# Buttons
generate_button = ttk.Button(button_frame, text="Generate MIDI", command=generate_midi)
generate_button.pack(side='left', padx=10)

play_button = ttk.Button(button_frame, text="Play Music", command=play_music_wrapper)
play_button.pack(side='left', padx=10)

save_button = ttk.Button(button_frame, text="Save Music", command=save_music_wrapper)
save_button.pack(side='left', padx=10)

root.mainloop()
