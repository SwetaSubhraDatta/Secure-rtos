import pydantic
from pydantic import BaseModel, Field
from typing import List, Optional


class DeviceSensors(BaseModel):
    sensor: str
    sensorID: str
    pins:List[int]
    readings:int

class DeviceSetting(BaseModel):
    DeviceName: str
    DeviceID:str
    DeviceVerified: bool
    DeviceSensor:DeviceSensors

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
    return True
