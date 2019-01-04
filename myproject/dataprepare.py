import json
import pandas as pd
import numpy as np
import pickle 
from collections import Counter 
import math
elasticnet = pickle.load(open('../prepare_utils/models/average_mae=40514063_alpha=1.9000_l1_ratio=0.2000', 'rb'))
term_index = json.load(fp=open('../prepare_utils/term_index.json'))
def dataprepare(source):
	df = pd.read_csv(source)

	apps = set(df['App'].tolist())
	app_size = len(apps)

	Xs = np.zeros( (app_size, len(term_index)), dtype=float ) 

	apps_order = []
	for index, (app, subDf) in enumerate(df.groupby(by=['App'])):
		term_freq = dict(Counter(' '.join(map(str,subDf['Translated_Review'].tolist())).lower().split()))
		for term, freq in term_freq.items():
			if term not in term_index:
				#print(term)
				continue
			Xs[index, term_index[term] ] = math.log(freq+1.0)
			if app not in apps_order:
				apps_order.append(app)
	yps = elasticnet.predict(Xs)

	objs = []
	for app, yp in zip(apps_order, yps):
		obj = {'app':app, 'predict':yp}
		objs.append(obj)
	#pd.DataFrame(objs).to_csv('res.csv', index=None)
	return pd.DataFrame(objs).to_html()

if __name__ == '__main__':
	html = dataprepare('../prepare_utils/googleplaystore_user_reviews.csv')
	print(html)

