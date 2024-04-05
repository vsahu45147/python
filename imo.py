import tkinter as tk
from tkinter import ttk

class CricketScoreGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cricket Score")
        
        # Label to display the current score
        self.score_label = ttk.Label(self.root, text="Score: ")
        self.score_label.grid(row=0, column=0, padx=10, pady=10)
        
        # Entry widget to input the score
        self.score_entry = ttk.Entry(self.root)
        self.score_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Button to update the score
        self.update_button = ttk.Button(self.root, text="Update", command=self.update_score)
        self.update_button.grid(row=0, column=2, padx=10, pady=10)
        
        # Label to display the updated score
        self.updated_score_label = ttk.Label(self.root, text="")
        self.updated_score_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
    
    def update_score(self):
        # Retrieve the score from the entry widget
        new_score = self.score_entry.get()
        # Update the label with the new score
        self.updated_score_label.config(text=f"Updated Score: {new_score}")

def main():
    root = tk.Tk()
    cricket_score_gui = CricketScoreGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
