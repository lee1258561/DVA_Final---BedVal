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
The code resource for user visualization is under user_visualization/ directory.
### Note
This web-based program does NOT WORK properly with Mozilla Firefox browser. We did not have enough time to troubleshoot the problem
as to what is the reason that caused this issue. The program was developed locally and tested to work with Chrome and Safari (latest version),
as long as the the program is run on a local server.

### Github repo
The following Github repo is a self contain server that can open our web-based program without the need of creating a local server.
Again, this program was only tested to work with Chrome and Safari browser.

[Github link](https://asaj3.github.io/)

### Supervised Learning & Experiment
Make sure the combined1.csv dataset is under the same folder with the scripts. Open a script and run the code, it will generate the results in the Python shell automatically. 
