from suds.client import Client
import os
import json
import ssl
import logging

"""
@PARAMS : event -  Contains the request body.

Since this is a lambda function so i'm mapping others details also in the event parameter like header, request body and others.

"""

def lambda_handler(event, context):
    logging.info(event)
    try:
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context
            
        
        #pass the wsdl location thr environment variable.

        url= os.environ['url']
        c = Client(
            url,
            faults=False
        )
        param = event['parameter'].strip()
        # check if the query param is numeric
        if param.isnumeric():

            res = c.service.yoursoapmethod(param)

            # fetching the status code from response
            status_code = res[0]

            # parameter_ Computation
            parameter_ = " "
            parameter_ = parameter_.join(res[1:])
            parameter_ = parameter_.replace(" ", ",")
            print(f"status code:{status_code}")
            print(f"raw response: {parameter_}")

            if status_code == 200:
                response = {
                    "message": parameter_
                }
                print(response)
                return response
            elif status_code == 500:
                response = {
                    "message": "SOAP Service not available."
                }
                print(response)
                return response
            else:
                return {
                    "message": parameter_
                }
        else:
            return {
                "Error": "Invalid query parameter."
            }
    except Exception as ae:
        print("Exception occurred while hitting the SOAP Service: ", ae)
        return {
            "Error": f"Exception occurred while hitting the SOAP Service : {ae}"
        }
