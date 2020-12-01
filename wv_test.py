import re
import string
from glob import glob
import os
from os.path import basename
from pathlib import Path
from os import listdir
from os.path import isfile, join
from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile
from gensim.models import KeyedVectors
a =[]
b = []
def nom_fichier():
	fichiers = [f for f in listdir('test_traite/') if isfile(join('test_traite/', f))]
	return fichiers

def word2vec_test():
	lines = []
	content = []
	tableau = []
	for element in nom_fichier():
		with open('result_embedded/'+element,'w+') as f :
			line =  open('test_traite/'+element,'r').readline()
			wv = KeyedVectors.load("vectors.kv", mmap='r')
			vector = [word.lower() for word in line.split(', ') if word !=''] 
			for word_a_traiter in vector:
				a = wv[word_a_traiter]	
				f.write(str(a) +"\n")		
				
		#content.append(tableau)
	
	#model = Word2Vec(content,window=7, size=100,min_count=1, workers=4)
	#fname = get_tmpfile("vectors.kv")
	#model.wv.save(fname)
	#l = model.wv.most_similar(positive=['android.intent.action.media_shared'], topn=5)
	#print(l)
	#print(model.wv['android.intent.action.media_shared'])
	#print("cv_to_matrix model saved")
	
	
	return 0
if __name__ == "__main__":
	word2vec_test()
	



