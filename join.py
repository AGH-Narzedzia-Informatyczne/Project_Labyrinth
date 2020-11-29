import labirynth_generator as bk_lab
import PySimpleGUI as sg
import PyMazeDFS
import PyMazeBFS

sg.theme('Topanga')


def bartek():
    layout = [[sg.Text("Labirynt generwany algorytmem BFS wersja 2", justification='center', font='Helvetica 15')],
              [sg.Text('Podaj wymiar N labiryntu:', justification='center', font='Helvetica 15'),
               sg.InputText(size=(8, 5), font='Helvetica 18')],
              [sg.Button("Generuj labirynt NxN", size=(15, 1), font='Helvetica 18')],
              [sg.Button("Zamknij okno", size=(10, 1), font='Helvetica 18')]
              ]
    # Create the Window
    window = sg.Window('Generator labiryntów', layout, size=(500, 200), element_justification='c')
    # Event Loop to process "events"
    while True:
        event, values = window.read()
        print(event, values)
        if event in (None, 'Zamknij okno'):
            break
        if event in (None, 'Generuj labirynt NxN'):
            bk_lab.generate(int(values[0]))
    window.close()



def konrad_dfs():
    layout = [[sg.Text("Labirynt generwany algorytmem DFS", justification='center', font='Helvetica 15')],
              [sg.Text('Podaj wymiar N labiryntu:', justification='center', font='Helvetica 15'),
               sg.InputText(size=(8, 5), font='Helvetica 18')],
              [sg.Button("Generuj labirynt NxN", size=(15, 1), font='Helvetica 18')],
              [sg.Button("Zamknij okno", size=(10, 1), font='Helvetica 18')]
              ]
    # Create the Window
    window = sg.Window('Generator labiryntów', layout, size=(500, 200), element_justification='c')
    # Event Loop to process "events"
    while True:
        event, values = window.read()
        print(event, values)
        if event in (None, 'Zamknij okno'):
            break
        if event in (None, 'Generuj labirynt NxN'):
            PyMazeDFS.generate(int(values[0]))
    window.close()


def konrad_bfs():
    layout = [[sg.Text("Labirynt generwany algorytmem BFS", justification='center', font='Helvetica 15')],
              [sg.Text('Podaj wymiar N labiryntu:', justification='center', font='Helvetica 15'),
               sg.InputText(size=(8, 5), font='Helvetica 18')],
              [sg.Button("Generuj labirynt NxN", size=(15, 1), font='Helvetica 18')],
              [sg.Button("Zamknij okno", size=(10, 1), font='Helvetica 18')]
              ]
    # Create the Window
    window = sg.Window('Generator labiryntów', layout, size=(500, 200), element_justification='c')
    # Event Loop to process "events"
    while True:
        event, values = window.read()
        print(event, values)
        if event in (None, 'Zamknij okno') or None:
            break
        if event in (None, 'Generuj labirynt NxN'):
            PyMazeBFS.generate(int(values[0]))
    window.close()


layout = [
    [sg.Text("Witaj! Wybierz jeden z poniższych generatorów labiryntów.", justification='center', font='Helvetica 15')],
    [sg.Text("Naciśnięcie jednego z poniższych przycisków otworzy nowe okno konfiguracji", justification='center',
             font='Helvetica 15')],
    [sg.Button('DFS', size=(15, 1), font='Helvetica 18')],
    [sg.Button('BFS', size=(15, 1), font='Helvetica 18')],
    [sg.Button('BFS wersja 2', size=(15, 1), font='Helvetica 18')],
    [sg.Button("Zakończ program", size=(10, 1), font='Helvetica 18')]
]
# Create the Window
window = sg.Window('Wybór generatora', layout, size=(550, 280), element_justification='c')
# Event Loop to process "events"
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Zakończ program') or None:
        break

    if event in (None, 'DFS'):
        konrad_dfs()
    if event in (None, 'BFS wersja 2'):
        bartek()
    if event in (None, 'BFS'):
        konrad_bfs()
window.close()