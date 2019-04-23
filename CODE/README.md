# DVA_Final---BedVal
## Host Interface
### Setup
1. Download data from https://drive.google.com/file/d/1deODOOpRnlfjZkFAGrQaUMTOR8RSf7cO/view?usp=sharing to host_interface/, unzip and make sure there is a directory data/ under host_interface/ directory.
2. 
```
cd host_interface/
pip install -r requirements.txt
```
### Run
1. Under host_interface/, launch server: 
```
python server.py
```
2. Open a browser (prefer Chrome or Safari) and enter the following url:
	http://localhost:8080/index.html



## User Visualization
### Setup
1. Github.io has been setup to run the web-based program for the user without them having to do anything else.

2. If prefer to run locally, run a local server to the user_visualization directory. Using [http.server](https://www.npmjs.com/package/http-server) is one way to setup local server in your computer.
		
### Run
1. Open the [Github.io](https://asaj3.github.io/) link using Chrome or Safari browser.

2. To run locally, after setting up your local server, open the url http://localhost:8080/index.html using Chrome or Safari browser.

### Note
This web-based program was developed locally and has been tested to work with Chrome and Safari browsers (latest version),
as long as the the program is run on a local server. Thus, Chrome and Safari are greatly recommended to run this program rather than with Firefox.

## Supervised Learning & Experiment
Make sure the combined1.csv dataset is under the same folder with the scripts. Open a script and run the code, it will generate the results in the Python shell automatically.
### Setup
```
cd supervised_learning_experiments/
pip install numpy pandas sklearn statsmodels
```
### Run
Under supervised_learning_experiments/, run the script files with no argument to reprouce the experiment results, the example command is as follow: 
```
python Experiment.py
```

