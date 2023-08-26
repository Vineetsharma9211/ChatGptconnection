import openai
import pyttsx3
import speech_recognition as sr
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data
s= recordAudio()
openai.api_key="Use your own api key from the website open ai"


eng=pyttsx3.init()
rate=eng.getProperty('rate')
voices=eng.getProperty("voices")
eng.setProperty('rate',125)
eng.setProperty('voice',voices[0].id)
eng.say(s)
eng.runAndWait()

eng.say("Please wait while we finding your answer")
eng.runAndWait()

completion=openai.Completion.create(engine="text-davinci-003"
                                    ,prompt=s
                                    ,max_tokens=1000)

print(completion.choices[0]["text"])
d=completion.choices[0]["text"]
eng.say(d)
eng.runAndWait()
