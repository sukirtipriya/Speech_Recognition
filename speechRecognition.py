#pip install SpeechRecognition
#pip install pyaudio

import speech_recognition as sr

def main() :
     r = sr.Recognizer ()
     
     with sr.Microphone() as source:
          r.adjust_for_ambient_noise(source)
          
          print("Please say something...")
          
          audio = r.listen(source)
          
          try:
             print("you have said: \n" + r.recognize_google(audio))
             
          except Exception as e:
             print("Error : " + str(e))
             
 if __name__ == "__main__":
        main()
                 
          
## Audio Recorder ###############################################################

import speech_recognition as sr

def main() :
     r = sr.Recognizer ()
     
     with sr.Microphone() as source:
          r.adjust_for_ambient_noise(source)
          
          print("Please say something...")
          
          audio = r.listen(source)
          
          print("Recognizing Now ...")
          
          try:
              print("you have said \n" + r.recognize_google(audio))
              print("Audio Recorder Successfully \n")
          
          except Exception as e:
              print("Error : " + str(e))
          
          with open("recordedaudio.wau", "wb") as f:
              f.write(audio.get_wav_data())


if__name__ == "__main__":
    main()
    
    
    
