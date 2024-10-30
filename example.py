from PlayPy import PyMediaPlay

if __name__ == "__main__":
    player = PyMediaPlay()

    # Prompt user for a file path
    file_path = input("Enter the path to the audio or video file: ")

    try:
        player.play(file_path)
    except Exception as e:
        print(e)
