import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation,DataTransformationConfig
from src.components.model_trainer import ModelTrainer,ModelTrainerConfig

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
    train_data,test_data=obj.initiate_data_injestion()
    data_tranformation=DataTransformation()
    train_arr,test_arr,_=data_tranformation.initiate_data_transformation(train_data,test_data)
    model_trainer=ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr,test_arr))
