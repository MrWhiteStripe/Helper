from vosk import Model, KaldiRecognizer
import pyaudio
import wave
#from playsound import playsound
import uuid
from os import path
import shutil
from pydub import AudioSegment
import time

model = Model('D:\\Stepan\\Coding\\Python\\Helper\\vosk-model-small-ru-0.22')
recognizer = KaldiRecognizer(model, 16000)

chunk = 1024
sample_f = pyaudio.paInt16
rate = 44100
channels = 2
timesec = 5
filename = str(uuid.uuid4()) + ".wav"
p = pyaudio.PyAudio()


source_path = str(filename)
print(source_path)

print("Recording...")
stream = p.open(format=sample_f, channels=channels, rate = rate, frames_per_buffer=chunk, input_device_index=1, input = True)

frames =[]

for i in range(0, int(rate / chunk * timesec)):
    data = stream.read(chunk)
    frames.append(data)

    if recognizer.AcceptWaveform(data):
        print(recognizer.Result())

stream.stop_stream()
p.terminate()

print("Recording finished!!!")

wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_f))
wf.setframerate(rate)
wf.writeframes(b''.join(frames))
wf.close()

#a = ''
#print("Do u wanna listen(Y/N)?")
#input(a)
#if a == 'Y':
    #playsound(filename)
sound = AudioSegment.from_wav(filename, format('mp3'))
sound.export(filename, format='wav')
print("Compiling...")
time.sleep(5)
if path.exists(source_path):
    destination_path = "D:\\Stepan\\Coding\\Products"
    new_location = shutil.move(source_path, destination_path)
    print(filename +  " перемещён в " + destination_path)
else: print(filename + " not exists.")


