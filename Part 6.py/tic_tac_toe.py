Х = "Х" 
О = "O" 
EMPTY = " "
TIE = "Ничья" 
NUM_SQUARES = 9
def displау_instruct():  
    """Выводит на экран инструкцию для игрока""" 
    print( 
    """Добро пожаловать на ринг грандиознейших интеллектуальных состязаний всех времён
    Твой мозг и мой процессор сойдутся в схватке за доской игры "Крестики-нолики
    Чтобы сделать ход. введи число от О до 8. Числа однозначно соответствуют полям 
    доски - так. как показано ниже: 
    0 | 1 | 2
    ---------  
    3 | 4 | 5
    ---------
    6 | 7 | 8  
    Приготовься к бою. жалкий белковый человечишка. Вот-вот начнется решающее сра­жение. \n """   
    )
def ask_yes_no(question): 
    """Задает вопрос с ответом 'Да' или 'Нет'.""" 
    response = None
    while response not in ("у" , "n"):
        response = input(question).lower()
    return response
def ask_number(question, low , high): 
    """Просит ввести число из диапазона.""" 
    response = None 
    while response not in range(low. high): 
        response = int(input(question)) 
    return response
def pieces(): 
    """Определяет принадлежность первого хода.""" 
    go_first = ask_yes_no("Xoчeшь оставить за собой первый ход? (y/n): ") 
    if go_first =="у": 
        print("\nHy что ж. даю тебе фору: играй крестиками.") 
        human = Х
        computer = О 
    else: 
        print("\nTвoя удаль тебя погубит. Буду начинать я.") 
        computer = Х
        human = О
        return computer, human
def new_board(): 
    """Создает новую игровую доску.""" 
    board = []
    for square in range(NUM_SQUARES): 
        board.append(EMPTY) 
    return board
def display_board(board): 
    """Отображает игровую доску на экране.""" 
    print("\n\t" + board[0] + "/" + board[1] + "/" + board[2]) 
    print("\t"+ "---------") 
    print("\t"+ board[3] + "1" + board[4] + "1 " + board[5]) 
    print("\t"+ "---------") 
    print("\t"+ board[6]+ "/" + board[7] + "/" + board[8]+ "\n")
def legal_moves (board): 
    """создает список доступных ходов.""" 
    moves = [] 
    for square in range(NUM_SQUARES): 
        if board[square] == EMPTY: 
            moves.append(square) 
            return moves
def winner(board): 
    """Определяет победителя в игре."""
    WAYS_ТО_WIN = ((0, 1, 2), 
    (3, 4, 5), 
    (6, 7, 8), 
    (0, 3, 6), 
    (1, 4, 7), 
    (2, 5, 8), 
    (0, 4, 8), 
    (2, 4, 6))
    for row in WAYS_ТО_WIN: 
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY: 
            winner = board[row[0]] 
            return winner
        if EMPTY not in board:
            return TIE
    return None
def human_move(board, human): 
    """Получает ход человека. """ 
    legal = legal_moves(board) 
    move = None 
    while move not in legal: 
        move = ask_number("Tвoй ход. Выбери одно из полей (О - 8):"+ 0 + NUM_SQUARES) 
        if move not in legal : 
            print("\nCмeшнoй человек! Это поле уже занято. Выбери дpyroe.\n") 
    print( "Ладно ... ") 
    return move
def computer_move(board , computer, human):
    """Делает ход за компьютерного противника."""  
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Я выберу поле номер" , end=" ")
    for move in legal_moves(board): 
        board[move] = computer 
# если следующим ходом может победить компьютер. выберем этот ход 
        if winner (board) == computer: 
            print(move) 
            return move 
# вь1полнив проверку. отменим внесенные изменения 
        board[move] = EMPTY