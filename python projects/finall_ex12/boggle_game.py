import tkinter as tk

""" 
 this class is the GUI of the game 'boggle'. the GUI display the game to the
  the user graphically
  """
BUTTON_STYLE = {"font": ("Courier", 30), "borderwidth": 1, "relief": tk.RAISED,
                "bg": 'SlateGray1', "activebackground": 'lavender'}


class BoggleGUI:
    """
       the init method initiate the board and is widgets which are the buttons,
       the labels and the listbox. for each widget its configures it size,
       location, width and height. also its store is buttons info in
        dictionaries. the GUI allowed the user to play in graphical way
     """
    __board_buttons = {}
    __init_buttons = {}
    __enter_button = {}
    __all_buttons = {}
    time_loop_continue = True
    empty_board =[
        ["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]
    ]

    def __init__(self):
        root = tk.Tk()  # main root
        root.title("My boggle")
        root.resizable(False, False)
        self.root = root

        self.main_frame = tk.Frame(self.root, width=500, height=500,
            background='LightSkyBlue')
        self.main_frame.pack()  # main frame

        self.title = tk.Label(self.main_frame, text="boggle game",
            font=("Cooper black", 15), bg='LightSkyBlue')
        self.title.place(x=170, y=1)  # 1 label

        self.word_box_label = tk.Label(self.main_frame, text='word:',
            font=("Courier", 20, "bold"), bg='SlateGray1', width=20)
        self.word_box_label.place(x=18, y=157)  # 2 label

        self.score = 0
        self.score_label = tk.Label(self.main_frame, bg='LightSkyBlue',
            font=("Courier", 15, "bold"), text="score: " + str(self.score))
        self.score_label.place(x=178, y=95)  # 3 label

        self.words_box = tk.Listbox(self.main_frame, bg="SlateGray1", font=(
            "Courier", 10), width=16, height=14)
        self.words_box.place(x=360, y=201)
        self.scrollbar = tk.Scrollbar(self.words_box,
            command=self.words_box.yview)
        self.scrollbar.place_configure(x=109, y=1, height=235)
        self.words_box.configure(yscrollcommand=self.scrollbar.set)
        self.words_box.insert(0, "my words:")  # box of words

        self._create_buttons_in_lower_canvas()  # the board buttons

        start = tk.Button(self.root, text='start', font=("Courier", 15, "bold"),
            bg='lavender', width=7, height=1)
        start.place(x=360, y=450)
        self.__init_buttons["start"] = start
        self.__all_buttons["start"] = start  # start bottom
        self.__all_buttons["restart"] = start

        enter = tk.Button(self.root, text='Enter', font=("Courier", 15, "bold"),
            bg='lavender', width=7, height=1)
        enter.place(x=360, y=155)
        self.__enter_button["Enter"] = enter
        self.__all_buttons["Enter"] = enter  # enter button

        how_to_play = tk.Button(self.root, text='game instructions',
            font=("Courier", 10), activebackground="lavender")
        how_to_play.place(x=0, y=0)
        self.__all_buttons["instructions"] = how_to_play  # instructions button

        self.__minutes = 3  # time
        self.__sec = 00
        self.__minutes_to_dis = '03'
        self.__sec_to_dis = '00'
        self.timer_label = tk.Label(self.main_frame, bg='LightSkyBlue',
            borderwidth=2, text="time left " + self.__minutes_to_dis + ":" +
                                self.__sec_to_dis, font=("Courier", 15, "bold"))
        self.timer_label.place(x=145, y=60)

    def _get_board_cor(self):
        """
        this method return the coordinates of the buttons ob the board
        """
        board_cor = []
        for a in range(4):
            for b in range(4):
                board_cor.append((b, a))
        return board_cor

    def _create_buttons_in_lower_canvas(self):
        """
        the method creates the buttons on the board and adding them into
        dictionaries
        """
        coordinate = self._get_board_cor()
        ind = 0
        for i in range(20, 261, 80):
            for j in range(201, 418, 72):
                button = tk.Button(self.root, text="", width=3, height=1,
                    **BUTTON_STYLE)
                button.place(x=i, y=j)
                self.__board_buttons[coordinate[ind]] = button
                self.__all_buttons[coordinate[ind]] = button
                ind += 1

    def time(self):
        """
        the method is responsible for the countdown of the timer. it also
        distinct if the timer was set in the middle of a game or after full
        round
        """
        if self.time_loop_continue:
            if self.__sec > 0:
                self.__sec -= 1
                string = str(self.__sec)
                if len(string) == 1:
                    self.__sec_to_dis = '0' + string
                else:
                    self.__sec_to_dis = string
            elif self.__minutes > 0:
                self.__sec = 59
                self.__sec_to_dis = '59'
                self.__minutes -= 1
                self.__minutes_to_dis = '0' + str(self.__minutes)
            else:
                self.time_over()
                return
            self.set_time()
            self.main_frame.after(1000, self.time)

    def set_time(self):
        """
        this method sets the label of the time according to the changes of
        the timer by the time method
        """
        self.timer_label.configure(text="time left " + self.__minutes_to_dis +
                                        ":" + self.__sec_to_dis)

    def pop_up_message(self, title, question, func):
        """"
        the method creates a pop up message that has two buttons that let the
        user decide what action does he want to do and according to it the
        method performed an action
        """
        pop_massage = tk.Toplevel(self.root)
        pop_massage.title(title)
        pop_massage.geometry("350x150")
        pop_massage.config(bg="thistle")

        pop_frame = tk.Frame(pop_massage, bg="thistle")
        pop_frame.pack(pady=10)

        yes_buttons = tk.Button(pop_frame, text="YES",
            font=("Courier", 10),
            command=lambda: func("YES", pop_massage))
        yes_buttons.grid(row=0, column=1)

        no_buttons = tk.Button(pop_frame, text="NO", font=("Courier", 10),
        command=lambda: func("NO", pop_massage))
        no_buttons.grid(row=0, column=2)

        pop_massage_label = tk.Label(pop_massage, text=question,
            font=("Courier", 10), bg="thistle", fg="black")
        pop_massage_label.pack(pady=10)

    def choice(self, choice, pop_massage):
        """"
        the method closes the game if the player pressed the 'NO' button and
        reset a new game if the player pressed the 'YES' button
        """
        pop_massage.destroy()
        if choice == "YES":
            self.__init_buttons["start"].invoke()
        elif choice == "NO":
            self.root.destroy()

    def get(self):
        """
        :return: the dictionary of the buttons
        """
        return self.__init_buttons

    def choice2(self, choice, pop_massage):
        """
        the method raise a pop up message that lets the player choose if
        he wants to restart a new game by clicking on the 'YES' button and
        keeping the current game if the player decided to continue with the
        game
        """
        pop_massage.destroy()
        if choice == "YES":
            self.time_loop_off()
            self.reset_game()
            self.__all_buttons["restart"].configure(text="start",
                bg="lavender")

            button_to_change = self.__board_buttons | self.__enter_button
            for button_name in button_to_change.keys():
                self.set_button_cmd(button_name, lambda: True)

        elif choice == "NO":
            pass

    def set_button_cmd(self, button_name, cmd):
        """
        the method set an action for each button
        """
        self.__all_buttons[button_name].configure(command=cmd)

    def display_found_word(self, word):
        """
        the method display the title of the found words
        """
        self.words_box.insert(1, word)

    def display_board(self, matrix):
        """
        :param matrix:
        the method gets a matrix which has coordinates to where to position
         each letter and display it on the board
        """
        for cor, button in self.__board_buttons.items():
            a = cor[0]
            b = cor[1]
            letter = matrix[a][b]
            button.configure(text=letter)

    def set_score(self, score):
        """
        :param score:
        rhe method get score and set the label that display it
        """
        self.score = score
        self.score_label.configure(text="score: " + str(self.score))

    def display_cur_word(self, word):
        """
        :param word:
        the method set the screen where the player forms a word
        """
        self.word_box_label.configure(text=word)

    def time_over(self):
        """
        the method raises a pop up message whenever the time is over.
        when the timer is ends there no option fir the player to keep search
        for word because by keep clicking on the board the buttons raises the
        message
        """
        title = "time's up"
        question = "Game over\n would you like to play again?"
        function = self.choice
        self.pop_up_message(
            title, question, function)
        button_to_change = self.__board_buttons | self.__enter_button
        for button_name in button_to_change.keys():
            self.set_button_cmd(button_name, lambda: self.pop_up_message(
                title, question, function))

    def get_board_buttons(self):
        """
        the method return a dictionary of the board buttons excluding the
        'start button and the 'enter' button
        :return: dictionary
        """
        return self.__board_buttons

    def clock_reset(self):
        """
        the method reset the timer and the display of it
         """
        self.__minutes = 3
        self.__sec = 0
        self.__minutes_to_dis = '03'
        self.__sec_to_dis = '00'
        self.set_time()

    def time_loop_on(self):
        """
        the method initiate the time loop
        """
        self.time_loop_continue = True

    def time_loop_off(self):
        """
        the method initiate the time loop
        """
        self.time_loop_continue = False

    def reset_game(self):
        """
        the method reset the whole game including the time, the score, the
         list of the found words and the screen where the word is display
         """
        self.clock_reset()
        self.display_board(self.empty_board)
        self.display_cur_word('word:')
        self.set_score(0)
        self.words_box.delete(1, tk.END)

    def start_before_finish(self):
        """
        the method raise a pop up message whenever the player choose to
        reset a new game before the current game is over
        """
        if self.__minutes == 0 and self.__sec == 0:
            return False
        elif self.__minutes == 3 and self.__sec == 0:
            return False
        else:
            title = "wait..."
            question = "are you sure you want to restart the game?"
            function = self.choice2
            self.pop_up_message(title, question, function)
            return True

    def change_start_to_restart(self):
       """
       the method change the label of the start game to 'restart' - let the
       player know that of he wants to play again he can press the restart game
       """
       self.__all_buttons["start"].configure(text="restart", bg="lavender")

    def game_instructions(self, text):
        """
        :param text:
        the method present the instructions of the game by clicking on the
        instructions button
        """
        root_instructions = tk.Toplevel(self.root)
        root_instructions.title("how to play")
        root_instructions.geometry("450x250")
        root_instructions.config(bg="lavender")

        inst_frame = tk.Frame(root_instructions, bg="lavender")
        inst_frame.pack(pady=10)

        text_inst = tk.Label(root_instructions, text=text, font=("Courier",
        10), bg="lavender", fg="black")
        text_inst.pack(pady=10)

    def start_game(self):
        """"
        the method that start the game
        """
        self.root.mainloop()

if __name__ == '__main__':
    gui = BoggleGUI()
    gui.start_game()
