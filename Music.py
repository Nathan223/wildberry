import platform

def load_windows():
    import winsound
    winsound.PlaySound("Audio/wildberry.wav", winsound.SND_FILENAME)

def load_mac():
    import subprocess
    audio_file = "./Audio/wildberry.wav"
    subprocess.call(["afplay", audio_file])

def no_op():
    pass

platform_detector = {
    "Windows": load_windows,
    "Darwin": load_mac,
    "undetected": no_op
}

if __name__ == '__main__':
    platform_detector.get(platform.system(), "undetected")()
