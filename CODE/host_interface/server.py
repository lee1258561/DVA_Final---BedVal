
from tornado.web import Application, RequestHandler, StaticFileHandler
from tornado.ioloop import IOLoop
from Model import Model
from distance import *

import json

import numpy as np

model = Model()
transportation_loc = prepare_transportation_data()

class InputError(Exception):
    def __init__(self, message):
        self.message = message

class  NotFoundError(Exception):
    def __init__(self, message):
        self.message = message
        

class price(RequestHandler):
    def set_default_headers(self):
        print "setting headers!!!"
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with, Content-Type")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def post(self):
        parameters = json.loads(self.request.body)
        self.set_status(200, "Successfully returned price")
        features, _ = extract_features([[float(parameters['latitude']), float(parameters['longitude'])]], transportation_loc['ALL'])
        record = np.array([[
            float(parameters['superHost']),
            float(parameters['listingCount']),
            float(parameters['hasPic']),
            float(parameters['identityVerified']),
            float(parameters['apt']),
            float(parameters['house']),
            float(parameters['entire']),
            float(parameters['accommodates']),
            float(parameters['beds']),
            float(parameters['realbed']),
            float(parameters['wifi']),
            float(parameters['reviewScore']),
            float(parameters['instantBook']),
            float(parameters['phoneVerification']),
            float(parameters['avgAvail']),
            float(parameters['longitude']),
            float(parameters['latitude']),
        ]])
        record = np.hstack((record, features))
        print (record)
        price = model.Price_Predict(record)
        self.write({"price": price})
    def options(self):
        # no body
        self.set_status(204)
        self.finish()


class demain(RequestHandler):
    def set_default_headers(self):
        print "setting headers!!!"
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with, Content-Type")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def post(self):
        parameters = json.loads(self.request.body)
        self.set_status(200, "Successfully returned demain")
        features, _ = extract_features([[float(parameters['latitude']), float(parameters['longitude'])]], transportation_loc['ALL'])
        record = np.array([[
            float(parameters['superHost']),
            float(parameters['listingCount']),
            float(parameters['hasPic']),
            float(parameters['identityVerified']),
            float(parameters['apt']),
            float(parameters['house']),
            float(parameters['entire']),
            float(parameters['accommodates']),
            float(parameters['beds']),
            float(parameters['realbed']),
            float(parameters['wifi']),
            float(parameters['reviewScore']),
            float(parameters['instantBook']),
            float(parameters['phoneVerification']),
            float(parameters['avgAvail']),
            float(parameters['longitude']),
            float(parameters['latitude']),
        ]])
        record = np.hstack((record, features))
        print (record)
        demain = model.Demand_Predict(record)
        self.write({"demain": demain})
    def options(self):
        # no body
        self.set_status(204)
        self.finish()



def make_app():
    urls = [
        (r"/price", price),
        (r"/demain", demain),
        (r"/(.*)", StaticFileHandler, {'path':'static/'}),
    ]
    return Application(urls, debug=True)
  
if __name__ == '__main__':

    app = make_app()
    app.listen(8080)
    IOLoop.instance().start()
