import pydantic
from pydantic import BaseModel, Field
from typing import List, Optional
from pydantic import StrictStr,StrictBool


class DeviceSensors(BaseModel):
    sensor: StrictStr
    sensorID: StrictStr
    pins:List[int]
    readings:int
    
class Tasks(BaseModel):
    No:int
    pins:List[int]

from pydantic import StrictStr,StrictBool
class DeviceSetting(BaseModel):
    DeviceName: StrictStr
    DeviceID:StrictStr
    DeviceVerified: StrictBool
    DeviceSensor:Optional[DeviceSensors]
    Tasks:Optional[Tasks]

def json_verify(json_file):
    """
    This function helps to verify the json file
    """
    try:
        json_file = DeviceSetting(**json_file)
        return True
    except pydantic.ValidationError as e:
        print(e)
        return False

