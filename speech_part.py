import speech_recognition as sr

class Speech():

    def __init__(self) -> None:
        self.r = sr.Recognizer()


    def microphone_recognition(self) -> str:
        with sr.Microphone() as source:
            print("Say something!")
            audio = self.r.listen(source)

            # recognize speech using Sphinx
            try:
                print("Sphinx thinks you said " +self.r.recognize_sphinx(audio))
            except sr.UnknownValueError:
                print("Sphinx could not understand audio")
            except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))

test = Speech().microphone_recognition()
