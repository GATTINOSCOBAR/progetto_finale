import sounddevice            
import speech_recognition       
import scipy.io.wavfile as wav  

def trascrittore(lingua):
    try:
        durata_rec = 5
        num_segm = 44100

        registrazione=sounddevice.rec(frames=(durata_rec * num_segm), samplerate=num_segm, channels=1, dtype='int16')
        sounddevice.wait()
        wav.write('rec.wav', num_segm, registrazione)

        riconoscitore=speech_recognition.Recognizer()
        with speech_recognition.AudioFile('rec.wav') as source:
            audio= riconoscitore.record(source)
        
        trascrizione= riconoscitore.recognize_google(audio, language=lingua)

        return trascrizione
    except Exception as e:
        return e

