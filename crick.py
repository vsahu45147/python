import tkinter as tk
import random

class CricketGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Cricket Game")
        self.root.geometry("600x400")

        self.runs = 0

        self.create_widgets()

    def create_widgets(self):
        self.run_label = tk.Label(self.root, text="Runs: 0")
        self.run_label.pack()

        self.hit_button = tk.Button(self.root, text="Hit!", command=self.hit)
        self.hit_button.pack()

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack()

    def hit(self):
        run = random.randint(0, 6)
        self.runs += run
        self.run_label.config(text="Runs: {}".format(self.runs))

if __name__ == "__main__":
    root = tk.Tk()
    game = CricketGame(root)
    root.mainloop()
