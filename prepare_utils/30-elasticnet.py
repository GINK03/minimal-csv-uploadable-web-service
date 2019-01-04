
import pickle
import numpy as np
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_absolute_error as mae
import random
import concurrent.futures
from sklearn.model_selection import KFold
import statistics

Xs, Ys = np.load('Xs.npy'), np.load('Ys.npy')
size = len(Xs)
folder = KFold(n_splits=5, random_state=777, shuffle=False)

def pmap(arg):
	param = arg

	scores = []
	for tIndex, TIndex in folder.split(Xs):
		_Xs, _Ys, _Xst, _Yst = Xs[tIndex], Ys[tIndex], Xs[TIndex], Ys[TIndex]
		alpha, l1_ratio = param
		elasticnet = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, selection='random', random_state=0)
		elasticnet.fit(_Xs,_Ys)
		yps = elasticnet.predict(_Xst)
		scores.append( mae(_Yst, yps) )
	name = (f'average_mae={int(statistics.mean(scores)):08d}_alpha={alpha:0.4f}_l1_ratio={l1_ratio:0.4f}')
	print(name)
	elasticnet = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, selection='random', random_state=0)
	elasticnet.fit(Xs, Ys)
	open(f'models/{name}', 'wb').write( pickle.dumps(elasticnet) )


alphas		= [0.1*i for i in range(10,20)]
l1_ratios = [0.1*i for i in range(1,11)]
params = []
for alpha in alphas:
	for l1_ratio in l1_ratios:
		params.append( (alpha, l1_ratio) )
params = random.sample(params, len(params))
print(params)
[pmap(param) for param in params]
#with concurrent.futures.ProcessPoolExecutor(max_workers=3) as exe:
#	exe.map(pmap, params)
