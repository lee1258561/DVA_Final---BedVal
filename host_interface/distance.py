import numpy as np
import pandas as pd
from geopy.distance import geodesic
from scipy.spatial.distance import cdist

transportation_input_files = [
								"data/BART/stops.txt", 
								"data/SFMTA/stops.txt", 
								"data/Caltrain/stops.txt"
							]
distance_output_files = [
							"data/distances/SanFran_BART.csv", 
							"data/distances/SanFran_SFMTA.csv", 
							"data/distances/SanFran_Caltrain.csv"
						]
output_files = [
					"data/features/SanFran_BART.csv", 
					"data/features/SanFran_SFMTA.csv", 
					"data/features/SanFran_Caltrain.csv"
				]
listing_file = "data/SanFran.csv"

radius = 0.7
def get_distance_features(distances):
	distances = np.sort(distances, axis=1)

	data = {
		"top1": distances[:, 0],
		"top5_avg": np.mean(distances[:, :5], axis=1),
		"within_radius_avg": np.mean(np.ma.masked_where(distances > radius, distances), axis=1).data,
		"total_avg": np.mean(distances, axis=1),
	}

	return pd.DataFrame(data=data)

def extract_features(listing, transportation):
	distances = cdist(listing, transportation, lambda x, y: geodesic(x, y).miles)
	features = get_distance_features(distances)
	return features, distances

def prepare_transportation_data():
	data = {}
	transportation = pd.read_csv(transportation_input_files[0])
	data['BART'] = transportation[['stop_lat', 'stop_lon']].values
	transportation = pd.read_csv(transportation_input_files[1])
	data['SFMTA'] = transportation[['stop_lat', 'stop_lon']].values
	transportation = pd.read_csv(transportation_input_files[2])
	data['Caltrain'] = transportation[['stop_lat', 'stop_lon']].values

	data['ALL'] = np.vstack((data['BART'], data['SFMTA'], data['Caltrain']))
	return data

if __name__  == "__main__":
	listing = pd.read_csv(listing_file)
	listing_loc = listing[['latitude', 'longitude']].values
	listing_id = listing[['id']]

	# listing_loc = np.array([[37.803768,-122.271450]])
	# listing_id = pd.DataFrame(data={"id": [123]})

	all_distances = None

	for input_file, output_file, distance_output_file in zip(transportation_input_files, output_files, distance_output_files):
		transportation = pd.read_csv(input_file)
		transportation_loc = transportation[['stop_lat', 'stop_lon']].values
		print (transportation_loc.shape)

		distance_features, distances = extract_features(listing_loc, transportation_loc)
		distance_features = pd.concat([listing_id, distance_features], axis=1)
		distance_features.to_csv(path_or_buf=output_file, index=False)

		distances.tofile(distance_output_file, sep=',')
		if all_distances is not None: all_distances = np.hstack((all_distances, distances))
		else: all_distances = distances

	distance_features = get_distance_features(all_distances)
	distance_features = pd.concat([listing_id, distance_features], axis=1)
	distance_features.to_csv(path_or_buf="data/features/SanFran_ALL.csv", index=False)
	#all_distances.tofile("data/distances/SanFran_ALL.csv", sep=',')
	# data = prepare_transportation_data()
	# print (data['BART'].shape, data['SFMTA'].shape, data['Caltrain'].shape, data['ALL'].shape)
	# features, distances = extract_features([[37.803768,-122.271450]], data['ALL'])
	# print (features)




