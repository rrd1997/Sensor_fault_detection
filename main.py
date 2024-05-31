import sys
import os
from src.exception import SensorException

def test_exception():
    try:
        a=1/0
    except Exception as e:
         raise SensorException("Something went wrong!", sys.exc_info())

if __name__=="__main__":
    try:
        test_exception()
    except Exception as e:
        print(e)