import random
import tkinter as tk

# Função para gerar as letras randomizadas
def generate_letters():
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random.shuffle(alphabet)

    for letter in alphabet:
        remaining_letters = len(alphabet) - 1
        yield letter, remaining_letters

# Função para exibir a letra em uma janela
def display_letter(letter_generator):
    root = tk.Tk()
    root.title('STOP GAME')
    root.geometry('300x300')

    # PARAR o programa
    def stop_programm():
        root.destroy()

    # Proxima letra
    def next_letter():
        try:
            nonlocal remaining_letters
            letter, remaining = next(letter_generator)
            letter_label.config(text=letter)
            remaining_letters -= 1
            remaining_label.config(text=f'Left words: {remaining_letters}', fg='black')
        except StopIteration:
            letter_label.config(text='End :)')

    stop_button = tk.Button(root, text='Stop', command=stop_programm, fg='red')
    stop_button.pack(
        ipadx= 6,
        ipady= 6,
        padx= 3,
        pady= 3,
        side= tk.BOTTOM,
        fill= tk.X
    )

    next_button = tk.Button(root, text='Next Word', command=next_letter, fg='green')
    next_button.pack(
        ipadx= 6,
        ipady= 6,
        padx= 3,
        pady= 3,
        side= tk.BOTTOM,
        fill= tk.X
    )

    letter_label = tk.Label(root, text='', font=('Helvetica',50), fg='blue')
    letter_label.pack(
        side= tk.TOP,
        fill= tk.X,
        expand= True
    )

    remaining_letters = 26
    remaining_label = tk.Label(root, text=f'Left Words: {remaining_letters}', font=('Arial',16), fg='black')
    remaining_label.pack()

    next_letter()

    root.mainloop()

# IF para mostrar no terminal e no display
if __name__ == "__main__":
    letter_generator = generate_letters()
    display_letter(letter_generator)

