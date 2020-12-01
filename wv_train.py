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
a =[]
b = []
def nom_fichier():
	fichiers = [f for f in listdir('manifest/traiter/') if isfile(join('manifest/traiter/', f))]
	return fichiers

def word2vec_entrainement():
	lines = []
	content = []
	tableau = []
	for element in nom_fichier():
		with open('manifest/traiter/'+element,'r') as f :
			for line in f.readlines():
				tableau=[a.lower() for a in line.split(', ') if a !=''] 
		content.append(tableau)
	for epoch in range(50):	
	    model = Word2Vec(content,window=7, size=100,min_count=1, workers=4)
	fname = get_tmpfile("vectors.kv")
	model.wv.save(fname)
	l = model.wv.most_similar(positive=['com.datahopper.tinyture.permission.c2d_message'], topn=5)
	print(l)
	print(model.wv['com.datahopper.tinyture.permission.c2d_message'])
	print("cv_to_matrix model saved")
	return 0
if __name__ == "__main__":
	word2vec_entrainement()
	



