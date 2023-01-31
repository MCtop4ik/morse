from tkinter import Tk
import tkinter as tk


class Assets:

    def __init__(self):
        self.morse = {'A': '.- ', 'B': '-... ', 'C': '-.-. ',
                      'D': '-.. ', 'E': '. ', 'F': '..-. ',
                      'G': '--. ', 'H': '.... ', 'I': '.. ',
                      'J': '.--- ', 'K': '-.- ', 'L': '.-.. ',
                      'M': '-- ', 'N': '-. ', 'O': '--- ',
                      'P': '.--. ', 'Q': '--.- ', 'R': '.-. ',
                      'S': '... ', 'T': '- ', 'U': '..- ',
                      'V': '...- ', 'W': '.-- ', 'X': '-..- ',
                      'Y': '-.-- ', 'Z': '--.. ', ' ': '   ',
                      }

        self.reverse_morse = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
                              '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                              '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
                              '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                              '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                              '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                              '-.--': 'Y', '--..': 'Z'}


class EncodeDecode(Assets):

    def __init__(self):
        Assets.__init__(self)

    def encode_to_morse(self, text: str) -> str:
        try:
            nt = ""
            for letter in text:
                nt += self.morse[letter]
            return nt
        except KeyError:
            raise KeyError('Неправильная форма ввода. Есть запрещеные символы')

    def decode_to_morse(self, text: str) -> str:
        try:
            results = []
            flag = True
            for item in text.split(' '):
                if self.reverse_morse.get(item) is not None:
                    results.append(self.reverse_morse.get(item))
                    flag = True
                else:
                    if flag:
                        results.append(' ')
                        flag = False
            return ''.join(results)
        except KeyError:
            raise KeyError('Неправильная форма ввода шифра Морзе')


ed = EncodeDecode()


def ec():
    value = name.get().upper()
    if value:
        label['text'] = ed.encode_to_morse(value)
        name.delete(0, 'end')
        name.insert(0, ed.encode_to_morse(value)[:-1])
    else:
        raise TypeError("Argument shouldn't be empty")


def dc():
    value = name.get().upper()
    if value:
        label['text'] = ed.decode_to_morse(value)
        name.delete(0, 'end')
        name.insert(0, ed.decode_to_morse(value))
    else:
        raise TypeError("Argument shouldn't be empty")


def delete():
    name.delete(0, 'end')


root = Tk()
root.title("Азбука Морзе")
name = tk.Entry(root, foreground="#470736", font="Arial 18")
label = tk.Label(root, text='Here is encoding', foreground='#6600ff', font='Times 20')
label.grid(row=3, column=1)
name.grid(row=0, column=1)
tk.Label(root, text="Ввод ::", foreground="#00008b", font="Arial 15").grid(row=0, column=0)
tk.Button(root, text='Decode', command=dc, foreground="#1a153f", font="Arial 16").grid(row=4, column=1)
tk.Button(root, text='Encode', command=ec, foreground="#1a153f", font="Arial 16").grid(row=4, column=0)
tk.Button(root, text='Auto Delete', command=delete, foreground="#1a153f", font="Arial 16").grid(row=2, column=1)
root.mainloop()
