import pandas as pd
import json
import numpy as np

if __name__ == "__main__":
	data = pd.read_csv('SF_attractions.csv')
	host_attractions = data[['id', 'attractions']].values

	conv = 0.621371
	radius = 0.7

	attraction_features = []
	for i in range(host_attractions.shape[0]):
		host_id = host_attractions[i][0]
		attraction_list = json.loads(host_attractions[i][1])
		attraction_distance = [attraction['properties']['distance'] for attraction in attraction_list]
		sorted_distance = np.array(sorted(attraction_distance), dtype=float)
		sorted_distance = sorted_distance / 1000 * conv

		top1 = sorted_distance[0]
		top5_avg = np.mean(sorted_distance[:5])
		#print (sorted_distance[sorted_distance < radius])
		within_radius_avg = np.mean(np.ma.masked_where(sorted_distance> radius, sorted_distance))
		within_radius_count = sorted_distance[sorted_distance < radius].shape[0]
		total_avg = np.mean(sorted_distance)

		attraction_features.append([host_id, top1, top5_avg, within_radius_avg, total_avg, within_radius_count])



	attraction_df = pd.DataFrame(np.array(attraction_features, dtype=object),
                  columns=['id', 'top1', 'top5_avg', 'within_radius_avg', 'total_avg', 'within_radius_count'])

	attraction_df.to_csv(path_or_buf='attraction_features.csv', index=False)
