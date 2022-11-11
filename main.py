import pyaudio
import wave
from playsound import playsound
import uuid
chunk = 1024
sample_f = pyaudio.paInt16
channels = 2
rate = 44100
timesec = 5
filename = str(uuid.uuid4()) + '.wav'
p = pyaudio.PyAudio()

print("Recording...")
stream = p.open(format=sample_f, rate=rate, channels=channels, frames_per_buffer=chunk, input_device_index=1,input=True)

frames =[]

for i in range(0, int(rate / chunk * timesec)):
    data = stream.read(chunk)
    frames.append(data)

stream.stop_stream()
p.terminate()

print("Recording finished!!!")

wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_f))
wf.setframerate(rate)
wf.writeframes(b''.join(frames))
wf.close()
playsound(filename)


