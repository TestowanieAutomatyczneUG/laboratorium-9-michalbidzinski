from Envi import Envi
class Checker:
    def __init__(self):
        self.env = Envi()
        self.wav_was_played = False
    def wavWasPlayed(self):
        self.wav_was_played = True
    def resetWaw(self):
        self.wav_was_played = False
    def reminder(self):
        if self.env.getTime().hour > 17:
            self.env.playWavFile('file.wav')
            self.wavWasPlayed()
        else:
            self.resetWaw()
