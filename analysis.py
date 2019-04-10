import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt


feature_list = [
					"data/features/SanFran_BART.csv", 
					"data/features/SanFran_SFMTA.csv", 
					"data/features/SanFran_Caltrain.csv",
					"data/features/SanFran_ALL.csv"
				]
prefixes = ["BART", "SFMTA", "Caltrain", "ALL"]
if __name__ == "__main__":
	labels = []
	datas = []
	for input_file, prefix in zip(feature_list, prefixes):
		input_df = pd.read_csv(input_file)
		datas.append(input_df.values[:, 1:])
		labels.extend(list(map(lambda label: prefix + '_' + label, input_df.columns.values[1:])))

	distance_features = np.hstack(datas)
	corr = np.corrcoef(distance_features.T)
	with sns.axes_style("white"):
	    ax = sns.heatmap(corr,
	    				 xticklabels=labels,
	    				 yticklabels=labels,
	    				 square=True, 
	    				 linewidth=0.5,  
	    				 cmap="YlGnBu")
	    plt.subplots_adjust(left=0.3, bottom=0.4)
	    plt.show()