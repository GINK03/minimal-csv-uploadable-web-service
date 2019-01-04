import pandas as pd

from collections import Counter
dfSells = pd.read_csv('./googleplaystore.csv')
dfUR = pd.read_csv('./googleplaystore_user_reviews.csv')

app_installs = {}
for app, subDfSells in dfSells.groupby(by=['App']):
	try:
		app_installs[app] = int(subDfSells['Installs'].tolist()[-1][:-1].replace(',', ''))
	except:
		print(subDfSells['Installs'].tolist()[-1][:-1].replace(',', ''))

term_index = {}
import json
objs = []
for app, subDfUR in dfUR.groupby(by=['App']):
	if app not in app_installs:
		continue
	print(app)
	print(app_installs[app])
	term_freq = dict(Counter(' '.join(map(str,subDfUR['Translated_Review'].tolist())).lower().split()))
	print(term_freq)
	for term in term_freq.keys():
		if term_index.get(term) is None:
			term_index[term] = len(term_index)
	obj = {'install': app_installs[app], 'term_freq': json.dumps(term_freq)}
	objs.append(obj)

json.dump(term_index, fp=open('term_index.json', 'w'), indent=2)

pd.DataFrame(objs).to_csv('install_tf.csv', index=None)
