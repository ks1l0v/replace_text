import time
import keyboard


data = {"!": "!", "@": "\"", "#": "№", "$": ";", "%": "%", "^": ":", "&": "?", "q": "й",
        "w": "ц", "e": "у", "r": "к", "t": "е", "y": "н", "u": "г", "i": "ш", "o": "щ", "p":
        "з", "[": "х", "]": "ъ", "a": "ф", "s": "ы", "d": "в", "f": "а", "g": "п", "h": "р",
        "j": "о", "k": "л", "l": "д", ";": "ж", "'": "э", "z": "я", "x": "ч", "c": "с", "v":
        "м", "b": "и", "n": "т", "m": "ь", ",": "б", ".": "ю", "/": ".", "Q": "Й", "W": "Ц",
        "E": "У", "R": "К", "T": "Е", "Y": "Н", "U": "Г", "I": "Ш", "O": "Щ", "P": "З", "{": "Х",
        "}": "Ъ", "A": "Ф", "S": "Ы", "D": "В", "F": "А", "G": "П", "H": "Р", "J": "О", "K": "Л",
        "L": "Д", ":": "Ж", "\"": "Э", "Z": "Я", "X": "Ч", "C": "С", "V": "М", "B": "И", "N": "Т",
        "M": "Ь", "<": "Б", ">": "Ю", "?": ","}


def replace_text(paste: str):
    final = ''
    for i in paste:
        if i in data:
            final += data[f"{i}"]
        else:
            final += i
    return final


def main():
    keyboard.press_and_release('ctrl+a')
    keyboard.press_and_release('ctrl+c')
    keyboard.press_and_release('ctrl+x')
    time.sleep(0.01)
    keyboard.press_and_release('ctrl+v')


if __name__ == '__main__':
    keyboard.add_hotkey("ctrl+\\", lambda: main())
    keyboard.wait('Esc')


