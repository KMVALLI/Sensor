


"""
The code you provided defines a custom exception class SensorException that includes detailed error information, 

such as the file name and line number where the exception occurred. When you raise an instance of SensorException, 

it provides this detailed information along with the error message.

"""

import sys                                                                             

"""
function :- error_message_detail 
1) taking an error message
2)with help of sys module we will trace the error  details (sys interact with python interpretector)
3)cetract file name ,line number ,errormessage using exception  trace back 
4)return the error message 

"""






def error_message_detail(error, error_detail: sys):      
    _, _, exc_tb = error_detail.exc_info()                         # exc_tb -> exception trace back 

    file_name = exc_tb.tb_frame.f_code.co_filename                  #get filename  where    you get an error
 
    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format( 
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


"""
class SensorException:-
1) SensorException is a coustem exception we are inherting from prent class as a Exception
1) intilized the instannce method as of SensorException in that we are passing the  our coustem  error meassage  it is expecteded  from sys
2) with help of supe().we are initilizing the parent class instance method
3)in instance methos we aee calling the normal function as  error_message_detail 
4)instance string method written the error meassage in the form f error message

if you want to use this function in exception handeling 
rasi SensorException(e,sys)
"""



class SensorException(Exception):
    def __init__(self, error_message, error_detail:sys):
        """
        :param error_message: error message in string format
        """
        super().__init__(error_message)

        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message
