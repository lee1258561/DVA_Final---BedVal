1. Description:
	There are three sub directory under CODE/, which is corresponded to three main modules of our project.

	host_interface/ - Host Interface Module:
		This module contain the source code for the interactive interface designed to help host to find out the suggested price and demand of the property given the location and the status of that property.

	user_visualization/ - User Visualization Module:
		This module contain the source code for the visualizations including the distribution of airbnb listing, nearby attraction, and choropleth graph for number of listing, average price, and review. This interface is designed for user to easily find out the desired airbnb property they want to rent.

	supervised_learning_experiments/ - Supervised Learning & Experiments:
		This module contain the source code necessary to reproduce the experiments that is mentioned in our final report.

	The following two sections will guide to setup and this three module. There are also a README.md under CODE/. If you encounter any trouble runung the code, please refer to the README.md and try again following its instruction.

2. Installation:
	Host Interface Module:
		Download data from https://drive.google.com/file/d/1deODOOpRnlfjZkFAGrQaUMTOR8RSf7cO/view?usp=sharing to host_interface/, unzip and make sure there is a directory data/ under host_interface/ directory.
		cd host_interface/
		pip install -r requirements.txt

	User Visualization Module:
		

	Supervised Learning & Experiments:
		Make sure the combined1.csv dataset is under the same folder with the scripts.
		cd supervised_learning_experiments/
		pip install numpy pandas sklearn statsmodels

3. Execution:
	Host Interface Module:
		Under host_interface/, launch server using following command:
			python server.py
		Open a browser (prefer Chrome or Safari) and enter the following url:
			http://localhost:8080/index.html

	User Visualization Module:
		

	Supervised Learning & Experiments:
		Under supervised_learning_experiments/, run the script files with no argument to reprouce the experiment results, the example command is as follow: 
			python Experiment.py

		


