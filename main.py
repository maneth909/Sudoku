import streamlit as st
import numpy as np
import time

# Sudoku boards
sudoku_boards = {
    "Easy": [[5, 3, 0, 0, 7, 0, 0, 0, 0],
             [6, 0, 0, 1, 9, 5, 0, 0, 0],
             [0, 9, 8, 0, 0, 0, 0, 6, 0],
             [8, 0, 0, 0, 6, 0, 0, 0, 3],
             [4, 0, 0, 8, 0, 3, 0, 0, 1],
             [7, 0, 0, 0, 2, 0, 0, 0, 6],
             [0, 6, 0, 0, 0, 0, 2, 8, 0],
             [0, 0, 0, 4, 1, 9, 0, 0, 5],
             [0, 0, 0, 0, 8, 0, 0, 7, 9]],
    "Medium": [[0, 2, 0, 6, 0, 8, 0, 0, 0],
               [5, 8, 0, 0, 0, 9, 7, 0, 0],
               [0, 0, 0, 0, 4, 0, 0, 0, 0],
               [3, 7, 0, 0, 0, 0, 5, 0, 0],
               [6, 0, 0, 0, 0, 0, 0, 0, 4],
               [0, 0, 8, 0, 0, 0, 0, 1, 3],
               [0, 0, 0, 0, 2, 0, 0, 0, 0],
               [0, 0, 9, 8, 0, 0, 0, 3, 6],
               [0, 0, 0, 3, 0, 6, 0, 9, 0]],
    "Hard": [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 3, 0, 8, 5],
             [0, 0, 1, 0, 2, 0, 0, 0, 0],
             [0, 0, 0, 5, 0, 7, 0, 0, 0],
             [0, 0, 4, 0, 0, 0, 1, 0, 0],
             [0, 9, 0, 0, 0, 0, 0, 0, 0],
             [5, 0, 0, 0, 0, 0, 0, 7, 3],
             [0, 0, 2, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 4, 0, 0, 0, 9]]
}


# Function to solve the Sudoku puzzle using backtracking
def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        board[i][j] = 0
                return False
    return True

# Function to check if a number is valid in a particular cell
def is_valid(board, row, col, num):
    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False
    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False
    # Check 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

# Function to check if the input Sudoku puzzle is valid
def is_valid_sudoku(board):
    # Check rows
    for row in board:
        if not is_valid_row(row):
            return False

    # Check columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_row(column):
            return False

    # Check 3x3 subgrids
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            subgrid = [board[i][j] for i in range(row, row + 3) for j in range(col, col + 3)]
            if not is_valid_row(subgrid):
                return False

    return True

# Function to check if a row, column, or subgrid contains valid digits
def is_valid_row(nums):
    nums = [n for n in nums if n != 0]  # Remove zeros
    return len(nums) == len(set(nums))  # Check for duplicates

# Function to display the Sudoku board
def display_board(board):
    for i in range(9):
        for j in range(9):
            st.write(board[i][j], end=" ")
        st.write()

import numpy as np
import streamlit as st

# Define a custom text input component that supports callbacks
class CustomTextInput:
    def __init__(self, label, default_value="", key=None):
        self.label = label
        self.default_value = default_value
        self.key = key
        self.widget = st.empty()
        self.value = self.widget.text_input(label=self.label, value=self.default_value, key=self.key)

    def update(self, new_value):
        self.value = new_value
        self.widget.text_input(label=self.label, value=self.value, key=self.key)

import numpy as np
import streamlit as st

# Define a custom text input component that supports callbacks
class CustomTextInput:
    def __init__(self, label, default_value="", key=None):
        self.label = label
        self.default_value = default_value
        self.key = key
        self.widget = st.empty()
        self.value = self.widget.text_input(label=self.label, value=self.default_value, key=self.key)

    def update(self, new_value):
        self.value = new_value
        self.widget.text_input(label=self.label, value=self.value, key=self.key)

import numpy as np
import streamlit as st

# Define a custom text input component that supports callbacks
class CustomTextInput:
    def __init__(self, label, default_value="", key=None):
        self.label = label
        self.default_value = default_value
        self.key = key
        self.widget = st.empty()
        self.value = self.widget.text_input(label=self.label, value=self.default_value, key=self.key)

    def update(self, new_value):
        self.value = new_value
        self.widget.text_input(label=self.label, value=self.value, key=self.key)

import numpy as np
import streamlit as st

# Define a custom text input component that supports callbacks
class CustomTextInput:
    def __init__(self, label, default_value="", key=None):
        self.label = label
        self.default_value = default_value
        self.key = key
        self.widget = st.empty()
        self.value = self.widget.text_input(label=self.label, value=self.default_value, key=self.key)

    def update(self, new_value):
        self.value = new_value
        self.widget.text_input(label=self.label, value=self.value, key=self.key)

import numpy as np
import streamlit as st

# Define a custom text input component that supports callbacks
class CustomTextInput:
    def __init__(self, label, default_value="", key=None):
        self.label = label
        self.default_value = default_value
        self.key = key
        self.widget = st.empty()
        self.value = self.widget.text_input(label=self.label, value=self.default_value, key=self.key)

    def update(self, new_value):
        self.value = new_value
        self.widget.text_input(label=self.label, value=self.value, key=self.key)


# Define a custom text input component that supports callbacks
class CustomTextInput:
    def __init__(self, label, default_value="", key=None):
        self.label = label
        self.default_value = default_value
        self.key = key
        self.widget = st.empty()
        self.value = self.widget.text_input(label=self.label, value=self.default_value, key=self.key)

    def update(self, new_value):
        self.value = new_value
        self.widget.text_input(label=self.label, value=self.value, key=self.key)


# Define a custom text input component that supports callbacks
class CustomTextInput:
    def __init__(self, label, default_value="", key=None):
        self.label = label
        self.default_value = default_value
        self.key = key
        self.widget = st.empty()
        self.value = self.widget.text_input(label=self.label, value=self.default_value, key=self.key)

    def update(self, new_value):
        self.value = new_value
        self.widget.text_input(label=self.label, value=self.value, key=self.key)

def main():
    start_time = None
    elapsed_time = 0

    start_time = None
    elapsed_time = 0

    def start_timer():
        nonlocal start_time
        start_time = time.time()

    def stop_timer():
        nonlocal elapsed_time
        elapsed_time += time.time() - start_time

    def format_time(seconds):
        minutes, seconds = divmod(seconds, 60)
        return f"{int(minutes):02d}:{int(seconds):02d}"

    previous_boards = []

    def update_previous_boards(board):
        previous_boards.append(board.copy())

    def undo():
        if previous_boards:
            previous_boards.pop()  # Remove the last board state
            if previous_boards:
                return previous_boards[-1]  # Return the previous board state
            else:
                return np.array(sudoku_boards[difficulty])  # Return to the initial state if no more previous states
        else:
            return np.array(sudoku_boards[difficulty])

    st.sidebar.title("Sudoku Difficulty")
    difficulty = st.sidebar.selectbox("Select Difficulty", ("Easy", "Medium", "Hard"))

    st.title("Sudoku Solver")

    col1, col2 = st.columns([3, 1])
    # Create a Sudoku board based on selected difficulty
    with col1:
        board = np.array(sudoku_boards[difficulty])
        update_previous_boards(board)  # Save the initial state of the board
        # Input the Sudoku puzzle
        st.write("Enter the Sudoku puzzle:")
        start_timer() 
        input_fields = [[None] * 9 for _ in range(9)]  # Initialize input fields
        feedback_fields = [[None] * 9 for _ in range(9)]  # Initialize feedback fields
        for i in range(9):
            row = st.empty()
            cols = row.columns(9)
            for j in range(9):
                with cols[j]:
                    value = board[i][j]
                    # Display empty input field if value is 0
                    if value == 0:
                        input_fields[i][j] = st.text_input(label=" ", key=(i, j))
                    else:
                        input_fields[i][j] = st.text_input(label=" ", value=str(value), key=(i, j))

    # Buttons in the sidebar
    st.sidebar.write("Actions:")

    st.sidebar.write("Timer:")
    timer_display = st.sidebar.empty()

    def update_timer():
        timer_display.write(format_time(elapsed_time))

    # First row in the sidebar: Undo and Redo buttons
    undo_col, redo_col = st.sidebar.columns([1, 1])
    with undo_col:
        if st.sidebar.button("Undo"):
            # Undo the last move
            board = undo()
            with col1:
                # Update the displayed Sudoku board
                st.write("Enter the Sudoku puzzle:")
                for i in range(9):
                    for j in range(9):
                        value = board[i][j]
                        if value == 0:
                            input_fields[i][j] = st.text_input(label=" ", key=(i, j))
                        else:
                            input_fields[i][j] = st.text_input(label=" ", value=str(value), key=(i, j))

    with redo_col:
        if st.sidebar.button("Redo"):
            # Add your logic for redoing here
            pass

    # Second row in the sidebar: Solve and Clear buttons
    solve_col, clear_col = st.sidebar.columns([1, 1])
    with solve_col:
        if st.sidebar.button("Solve"):
            with col2:
                if is_valid_sudoku(board):
                    solved_board = board.copy()  # Copy the original board for solving
                    if solve_sudoku(solved_board):
                        st.write("Sudoku puzzle solved:")
                        stop_timer() 
                        # Display the solved Sudoku board in a grid of 9x9
                        for i in range(9):
                            row = st.empty()
                            cols = row.columns(9)
                            for j in range(9):
                                with cols[j]:
                                    st.write(solved_board[i][j], end=" ")
                            st.write()
                    else:
                        st.write("Unable to solve Sudoku puzzle.")
                else:
                    st.write("Invalid Sudoku puzzle. Please check your input.")

    with clear_col:
        if st.sidebar.button("Clear"):
            stop_timer() 
            # Clear all input fields
            with col1:
                st.write("Enter the Sudoku puzzle:")
                for i in range(9):
                    for j in range(9):
                        input_fields[i][j] = st.text_input(label=" ", key=(i, j))

            with col2:
                # Clear feedback messages
                for i in range(9):
                    for j in range(9):
                        st.empty()

    with col2:
        for i in range(9):
            for j in range(9):
                if input_fields[i][j] is not None:
                    value = input_fields[i][j]
                    if value != "":
                        value = int(value)
                        if value != board[i][j]:  # Check if value is different from the initial board
                            feedback_field = st.empty()  # Create an empty slot for feedback
                            if is_valid(board, i, j, value):
                                feedback_field.markdown(f"<span style='font-size:16px;color:green;'>Cell ({i+1},{j+1}): Correct</span>", unsafe_allow_html=True)
                            else:
                                feedback_field.markdown(f"<span style='font-size:16px;color:red;'>Cell ({i+1},{j+1}): Incorrect</span>", unsafe_allow_html=True)
                    else:
                        st.empty()

    def update():
        while True:
            update_timer()
            time.sleep(1)
            st.experimental_rerun()

    # Start updating the timer in a separate thread
    import threading
    threading.Thread(target=update).start()

if __name__ == "__main__":
    main()
