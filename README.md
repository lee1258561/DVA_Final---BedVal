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
### Setup and Run
The code resource for user visualization is under user_visualization/ directory. Do not change the files in the "lib" folder. The program can be opened immediately if Mozilla browser is used. For Chrome and Safari, local server has to be setup to your local directory to run the index.html file. To setup the local server, follow the above steps for the Host Interface but in your user_visualization directory

### Note
This web-based program was developed locally and has been tested to work with Chrome and Safari browsers (latest version),
as long as the the program is run on a local server. It can also run on Mozilla browser without the need of local server.

### Github repo
The following Github repo is a self contain server that can open our web-based program without the need of creating a local server.
It has been tested to work with Chrome, Safari and Mozilla browser.

[Github link](https://asaj3.github.io/)



## Supervised Learning & Experiment
Make sure the combined1.csv dataset is under the same folder with the scripts. Open a script and run the code, it will generate the results in the Python shell automatically. 
