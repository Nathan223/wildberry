try:
    import winsound
    winsound.PlaySound("Audio/wildberry.wav", winsound.SND_FILENAME)
except ImportError:
    pass
