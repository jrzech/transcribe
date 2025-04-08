import os

directory = '/Users/jrzech/openai/in'
out = '/Users/jrzech/openai/out/'
from openai import OpenAI
client = OpenAI()

for filename in os.listdir(directory):
	f = os.path.join(directory,filename)
	if os.path.isfile(f):
		try:
			audio_file= open(f, "rb")
			transcription = client.audio.transcriptions.create( 
			model="whisper-1", 
			file=audio_file)
			#print(transcription.text)
			f = open(out+filename+".txt", "w")
			f.write(transcription.text)
			f.close()
		except:
			print("fail on "+f)
