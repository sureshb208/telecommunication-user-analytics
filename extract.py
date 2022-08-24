import json
from re import sub
from numpy import source
import pandas as pd
from textblob import TextBlob

excel_data_df = pd.read_excel('data/Week1_challenge_data_source.xlsx')

#excel_data_df.to_json('processed_tweet_data.json', index=False)

def read_json(json_file: str)->list:
    """
    json file reader to open and read json files into a list
    Args:
    -----
    json_file: str - path of a json file
    
    Returns
    -------
    length of the json file and a list of json
    """
    
    tele_data = []
    for tele in open(json_file,'r'):
        tele_data .append(json.loads(tele))
    
    
    return len(tele_data ), tele_data 

class TeleDfExtractor:
    """
    this function will parse tweets json into a pandas dataframe
    
    Return
    ------
    dataframe
    """
    def __init__(self, tele_list):
        
        self.tele_list = tele_list

    # an example function

    def find_bearer_id(self)->list:
        bearer_id= [data['Bearer Id']
            if 'Bearer Id' in data else '' for data in self.tele_list]
        return bearer_id

    def find_duration_ms(self)->list:
        duration_ms= [data['Dur. (ms)']
            if 'Dur. (ms)' in data else '' for data in self.tele_list]
        return duration_ms

    def get_tele_df(self, save = True)->pd.DataFrame:
        """required column to be generated you should be creative and add more features"""
        
             
        columns = ['bearer id ', 'duration ms']

        bearer_id = self.find_bearer_id()
        duration_ms = self.find_duration_ms()

        data = zip(bearer_id,duration_ms)

        df = pd.DataFrame(data=data, columns=columns)

        # if save:
        #     df.to_csv('processed_tele_data.csv', index=True)
        #     print('File Successfully Saved.!!!')
        
        # return df

if __name__ == "__main__":
    # required column to be generated you should be creative and add more features

    columns = ['bearer_id,duration_ms']
    _, tele_list = read_json("data/processed_tele_data.json")
    tele = TeleDfExtractor(tele_list)
    tele_df = tele.get_tele_df()

    


    # use all defined functions to generate a dataframe with the specified columns above