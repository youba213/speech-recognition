import speech_recognition as sr
import serial

ser = serial.Serial('COM3', 9600, timeout=1.0)

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))

        if text == 'green':
            ser.write(b'1')
        elif test == 'red':
            ser.write(str.encode('2'))
            print('okay')
        elif test == 'blue':
            ser.write('3')
            print('okay')
        else:
            print('type something else')

    except:
        print("Sorry could not recognize what you said")