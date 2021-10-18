# class to pull data from collection level opensea api
# must cast query url to variable url
# url = 'https://api.opensea.io/api/v...'

# openseacollection syntax is data_name = openseacollection (url)
# url = the query url from opensea 'https://api.opensea.io/api/v...'

import requests
import pandas as pd

class OpenSeaCollection:
    def __init__ (self, url):
        self.url = url   #assign query url to "self.url"
        self.get_data()  #run get_data method
        self.get_attributes() #run get attribute method

    def get_data(self):
        self.data = requests.request("GET", self.url).json() #assign query json to "self.data"

    def get_attributes(self): # run functions for each attribute
        self.num_sales = [x['num_sales'] for x in self.data['assets']]
        self.token_id = [x['token_id'] for x in self.data['assets']]
        self.name = [x['name'] for x in self.data['assets']]
        self.last_sale = [x['last_sale'] for x in self.data['assets']]
        self.project_des = self.data['assets'][0]['asset_contract']['description']

    def as_df(self): # cast attributes into df
        return pd.DataFrame({'Token ID':self.token_id,'Name':self.name})