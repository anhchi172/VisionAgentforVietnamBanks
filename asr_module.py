import speech_recognition as sr
import sounddevice as sd
import wavio

class ASRModule:
    def __init__(self, sample_rate=16000, duration=5, filename='output.wav'):
        self.sample_rate = sample_rate
        self.duration = duration
        self.filename = filename
        self.recognizer = sr.Recognizer()

    def record_audio(self):
        print("Recording...")
        recording = sd.rec(int(self.duration * self.sample_rate), samplerate=self.sample_rate, channels=1, dtype='int16')
        sd.wait()  # Wait until recording is finished
        wavio.write(self.filename, recording, self.sample_rate, sampwidth=2)
        print("Recording finished.")

    def listen_and_recognize(self):
        self.record_audio()
        with sr.AudioFile(self.filename) as source:
            audio = self.recognizer.record(source)
            try:
                text = self.recognizer.recognize_google(audio, language='vi-VN')
                print("You said: " + text)
                return text
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                return ""
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                return ""

if __name__ == "__main__":
    asr = ASRModule()
    asr.listen_and_recognize()
