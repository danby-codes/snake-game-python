import random
from snake_view import draw_board


# Starter appen
def app_started(app):
    app.direction = "east"      #Retning
    app.menu_mode = True        #Menymodus aktiv
    app.board = [                 # Spillbrettet: 0 = tom, + = slange, -1 = eple
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    app.snake_size = 3 #Lengde til slangen
    app.head_pos = (3, 4)  #Posisjonskoordinatene til hodet
    app.state = "active"       #Enten er spillet aktiv, eller er den over (gameover)



#Beveger slangen automatisk
def timer_fired(app):   
    if not app.menu_mode and app.state == "active":  
        move_snake(app)

#Funksjon for tastetrykk
def key_pressed(app, event):
    if app.menu_mode: #Hvis spillet er i menyen kan man velge vansklighet
        if event.key == "1":
            app.timer_delay = 700  # Lett
            app.menu_mode = False
        elif event.key == "2":
            app.timer_delay = 500  # Middels
            app.menu_mode = False
        elif event.key == "3":
            app.timer_delay = 300  # Vanskelig (Mindre delay -> slange beveger raskere)
            app.menu_mode = False

    #Når spillet er aktivt
    elif app.state == "active":
        if event.key == "Up" and app.direction not in ("north", "south"): 
            app.direction = "north"
        elif event.key == "Down" and app.direction not in ("south", "north"):
            app.direction = "south"
        elif event.key == "Right" and app.direction not in ("east", "west"):
            app.direction = "east"
        elif event.key == "Left" and app.direction not in ("west", "east"):
            app.direction = "west"
        elif event.key == "Space":
            move_snake(app)

    #Når spillet ikke er aktivt lenger ("gameover")
    elif app.state == "gameover":
        if event.key == "m":          #----> Initialiserer at m tar spiller tilbake til MENU
            app_started(app) 



def redraw_all(app, canvas):    #---> Funksjon for alt det visuelle 
    if app.state == "active" and not app.menu_mode:
        draw_board(canvas, 50, 50, 950, 750, app.board, app.menu_mode) #----> kaller til funksjon fra snake_view.py og tegner brettet
        points = app.snake_size - 3  #Poeng er lengden til slangen minus 3
        canvas.create_text(500, 30, text=f"Points: {points}", font=("Arial", 28, "bold")) #Tegner inn poengscore

    #Menyen
    elif app.menu_mode: #hvis man er i menyen
        canvas.create_rectangle(200, 240, 800, 350, outline='blue', width=6, fill="lightblue") #
        canvas.create_text(500, 300, text='Welcome to SNAKE!', font=("Courier", 50, "bold"), fill="blue")

        # Easy
        canvas.create_rectangle(46, 500, 340, 610, outline='green', width=6, fill="lightgreen")
        canvas.create_text(193, 555, text='PRESS 1 - EASY', font=("Courier", 30, "bold"), fill="green")
        # Medium
        canvas.create_rectangle(346, 500, 640, 610, outline='orange', width=6, fill="lightyellow")
        canvas.create_text(493, 555, text='PRESS 2 - INTER', font=("Courier", 30, "bold"), fill="orange")
        # Hard
        canvas.create_rectangle(646, 500, 940, 610, outline='red', width=6, fill="pink")
        canvas.create_text(793, 555, text='PRESS 3 - HARD', font=("Courier", 30, "bold"), fill="red")

    #Gameover - screen
    elif app.state == "gameover":
        canvas.create_rectangle(300, 240, 700, 440, outline='black', width=10)
        canvas.create_text(500, 300, text='Game Over', font=("Impact", 60), fill="red")
        canvas.create_text(500, 370, text="Press M to return to menu", font=("Courier", 24, "bold"))


#Funksjon for tilfeldig eple-plassering
def add_apple_at_random_location(board):
    empty_cells = []

    # Finner alle celler som er tomme (value=0)
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 0:
                empty_cells.append((r, c)) #Legger alle koordinatene til tom celle i lista

    # Velg en tilfeldig celle fra lista
    if empty_cells:
        r, c = random.choice(empty_cells)
        board[r][c] = -1 #Gi den cella value=-1 (eplet)
    
#funksjon for slangehodets neste posisjon    
def get_next_head_position(head_pos, direction):
    row, col = head_pos #Gjør om koordinatene til en tuple
    if direction == "north": return (row - 1, col)
    if direction == "south": return (row + 1, col) #---> Muterer tupelen ifht. hvilken retning slangen går
    if direction == "east":  return (row, col + 1)
    if direction == "west":  return (row, col - 1)
    return (row, col)    #returnerer en koordinat

def is_legal_move(pos, board): #Sjekker om neste hodets posisjon er lov (Utenfor brettet eller på slangen)
    row, col = pos #Gjør om posisjonen til en tuple
    rows = len(board) #Henter verdien for alle rader og kolonner i gridden
    cols = len(board[0]) 
    if row < 0 or row >= rows: #Sjekker om slangen går ut av toppen/bunnen av brettet
        return False
    if col < 0 or col >= cols: #Sjekker om slangen går ut av sidene av brettet
        return False
    if board[row][col] > 0: #Sjekker om posisjonen til slangen er i slangen
        return False

    return True

#Funksjon som gjør at slangekroppen følger etter
def subtract_one_from_all_positives(board): 
    for r in range(len(board)):
        for c in range(len(board[0])): #For hver r og c koordinat
            if board[r][c] > 0: #Hvis verdien er større enn 0
                board[r][c] -= 1 #Trekkes det fra -1 i verdi fra hver celle som slangen er i

#funksjon for slangekroppens bevegelse
def move_snake(app):
    new_head = get_next_head_position(app.head_pos, app.direction) #henter nye hodets posisjon fra funksjonen

    if not is_legal_move(new_head, app.board): #Sjekker om spillet er over fra funksjonen (Hvis false, app.state = "gameover")
        app.state = "gameover"
        return

    app.head_pos = new_head #Omgjør den nye posisjonen til hodet, og legger den i spillet
    row, col = new_head #gjør den til en tuple

    if app.board[row][col] == -1: #Sjekker om hodet traff et eple
        app.snake_size += 1 #Lengden blir da +1 lenger
        app.timer_delay = max(100, app.timer_delay - 50)  # Øker hastighet for hvert eple spist
        add_apple_at_random_location(app.board) #Legger til et tilfeldig eple
    else:
        subtract_one_from_all_positives(app.board)  #Kjører funksjonen som beveger slangen

    #Oppdater hodets posisjon
    app.board[row][col] = app.snake_size


if __name__ == '__main__':
    from uib_inf100_graphics.event_app import run_app
    run_app(width=1000, height=800, title='Snake')