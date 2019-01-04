import pandas as pd
import json
import numpy as np
import math
df = pd.read_csv('install_tf.csv')

term_freqs = df['term_freq'].apply(lambda x:json.loads(x))
term_index = json.load(fp=open('term_index.json'))
installs = df['install'].tolist()

Xs = np.zeros( (len(term_freqs), len(term_index)), dtype=float ) 
Ys = np.zeros( (len(term_freqs)), dtype=float)
for index1, (install, term_freq) in enumerate(zip(installs, term_freqs)):
	Ys[index1] = install
	for term, freq in term_freq.items():
		Xs[index1, term_index[term] ] = math.log(freq+1.0)
np.save('Xs', Xs) 
np.save('Ys', Ys)
