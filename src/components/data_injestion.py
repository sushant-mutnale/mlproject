import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataInjestionConfig :
    train_data_path:str =os.path.join("artifacts",'train.csv')
    test_data_path:str =os.path.join("artifacts",'test.csv')
    raw_data_path:str =os.path.join("artifacts",'data.csv')

class DataInjestion:
    def __init__(self):
        self.injestion_config = DataInjestionConfig()
    
    def initiate_data_injestion(self):
        logging.info("Entered The Data Injestion Method Or Component")
        try:
            df =pd.read_csv("notebbok\data\stud.csv")
            logging.info("Read the dataframe as dataframe")

            os.makedirs(os.path.dirname(self.injestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.injestion_config.raw_data_path,index=False,header=True)

            logging.info("Train Test Split Intiaated.")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.injestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.injestion_config.test_data_path,index=False,header=True)

            logging.info("Data Injestion Completed.")

            return(
                self.injestion_config.train_data_path,
                self.injestion_config.test_data_path,
                
            )



        except Exception as e:
            raise CustomException(e,sys)



if __name__=="__main__":
    obj=DataInjestion()
    obj.initiate_data_injestion()