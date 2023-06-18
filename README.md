# Music_Generator
The code is a Python-based MIDI music generator with a GUI. It allows users to generate and play MIDI music based on selected parameters such as key, mood, music type, complexity, bars, and beats per bar.

MIDI Maestro Documentation

Introduction:
MIDI Maestro is a Python program that allows users to generate and play MIDI music compositions based on various parameters. The program utilizes the music21 library for MIDI file handling and composition generation.

Requirements:
To execute MIDI Maestro, you need the following:

Python 3.x installed on your system
The music21 library installed (install using 'pip install music21')
The pygame library installed (install using 'pip install pygame')
The tkinter library, which is usually included with Python
Functionality:
MIDI Maestro provides a graphical user interface (GUI) that allows users to select different parameters for generating music. The parameters include key, mood, music type, complexity, bars, and beats per bar. Users can select a key (C major, C minor, etc.), mood (happy, sad), music type (chords, melody, both), complexity level (low, medium, high), and specify the number of bars and beats per bar for the composition.

Music Generation:
The generate_music() function in MIDI Maestro generates the music composition based on the selected parameters. It creates a music21 Stream object and adds a piano instrument. Depending on the selected music type, it generates chord progressions and/or melodies using random selection of notes and rhythms from the chosen key and complexity level. The rhythm patterns are dynamically generated based on the specified beats per bar.

Playback and Saving:
MIDI Maestro provides options to play the generated music in real-time using the pygame library and to save the composition as a MIDI file. Users can listen to the music they have generated and save it for further use or editing.

Graphical User Interface (GUI):
MIDI Maestro's GUI is implemented using the tkinter library and offers a user-friendly interface for selecting the music parameters and interacting with the program. Users can choose the desired options using drop-down menus and radio buttons. The "Generate MIDI" button triggers the music generation process, while the "Play Music" and "Save Music" buttons allow users to listen to the generated music and save it as a MIDI file, respectively.

Error Handling:
The code in MIDI Maestro incorporates error handling mechanisms to ensure the smooth execution of the program. It includes checks for invalid parameter values and handles exceptions that may occur during MIDI file handling and music playback.

Customization and Extensions:
MIDI Maestro's code can be extended and customized to add more features, such as additional musical scales, moods, and complexity levels. The GUI can be enhanced with additional widgets and functionalities to provide an even more interactive user experience.

Overall, MIDI Maestro offers a simple and intuitive way to create MIDI music compositions based on user-selected parameters, providing a versatile tool for music enthusiasts, composers, and learners.
