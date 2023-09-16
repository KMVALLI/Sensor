import os
from datetime import datetime
from sensor import logger



from sensor.constant import training_pipeline


"""
class TrainingPipelineConfig -->
1)TrainingPipelineConfig instance method intialized first as a current data using inbuilt datetime class
2)we are custamizing the  data formate  in the form of string 
3)creating training pipline name 
4)creating a path using arifact name with extention of timestamp
5) creating a final path in timestamp variable

"""

class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp = timestamp.strftime("%d_%m_%Y_%H_%S")
        self.pipline_name: str = training_pipline.pipline_name
        self.artifact_dir: str = os.path.join(training_pipline.ARTIFACT_DIR, timestamp)
        self.timestamp:str = timestamp

print("sucess")