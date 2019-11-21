import urllib.request
import urllib.parse
import re
import unicodedata
import os
import subprocess
import time
from pytube import YouTube
import shutil
import myscraping
import time

# PESQUISA O NOME DA MUSICA NO YOUTUBE E RETORNA O PRIMEIRO RESULTADO DA PESQUISA
def pesquisa(musica):
	query_string = urllib.parse.urlencode({"search_query" : musica})
	html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
	search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
	return "http://www.youtube.com/watch?v=" + search_results[0]



# REMOVER CARACTERES ESPECIAIS E ACENTOS DO NOME DA MÚSICA // incompatibilidade na conversao
def remove(palavra):

	nfkd = unicodedata.normalize('NFKD', palavra)
	palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])

	return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)



def downConvert(url, pasta):
	name = ((YouTube(url)).title)
	_filename = remove(name)
	YouTube(url).streams.first().download(filename=_filename)	
	time.sleep(1)
	
	mp4 = (f'{_filename}.mp4')
	mp3 = (f'{_filename}.mp3')
	
	time.sleep(2)

	ffmpeg = (f'ffmpeg.exe -i "{mp4}" "{mp3}"')
	print(ffmpeg)
	subprocess.call(ffmpeg, shell=True)
	
	time.sleep(2)

	#
	#Remove o arquivo .mp4	
	os.remove(_filename + '.mp4')

	#Move para pasta de músicas
	shutil.move(mp3, pasta)


play = str(input("Cole a playlist do Spotify para Download: \n"))

filename = myscraping.spotify(play)	

pasta = filename[:-4]
os.mkdir(pasta)

f = open(filename, 'r')

for lina in f:
	search = pesquisa(lina)
	downConvert(search, pasta)
	time.sleep(1)
os.remove(filename)
	
