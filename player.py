import pygame
import cv2
import os

class PyMediaPlay:
    def __init__(self):
        pygame.init()
        self.video_window_name = "Video Playback"

    def play(self, path: str):
        """Play an audio or video file based on the file extension.

        Args:
            path (str): Path to the audio or video file.
        """
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")

        # Check the file extension to determine if it's audio or video
        _, ext = os.path.splitext(path)
        ext = ext.lower()

        if ext in ['.mp3', '.wav', '.ogg', '.flac']:
            self._play_audio(path)
        elif ext in ['.mp4', '.avi', '.mov', '.mkv']:
            self._play_video(path)
        else:
            raise ValueError(f"Unsupported file format: {ext}")

    def _play_audio(self, audio_file: str):
        """Play an audio file.

        Args:
            audio_file (str): Path to the audio file.
        """
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        print(f"Playing audio: {audio_file}")
        while pygame.mixer.music.get_busy():  # Wait for the audio to finish
            pygame.time.Clock().tick(10)

    def _play_video(self, video_file: str):
        """Play a video file.

        Args:
            video_file (str): Path to the video file.
        """
        cap = cv2.VideoCapture(video_file)
        if not cap.isOpened():
            raise ValueError("Error: Could not open video.")

        cv2.namedWindow(self.video_window_name)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            cv2.imshow(self.video_window_name, frame)

            # Exit if 'q' is pressed
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        print("Video playback finished.")

# Example usage
if __name__ == "__main__":
    player = PyMediaPlay()

    # Prompt user for a file path
    file_path = input("Enter the path to the audio or video file: ")

    try:
        player.play(file_path)
    except Exception as e:
        print(e)
