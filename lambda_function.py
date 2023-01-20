from suds.client import Client
import os
import json
import ssl
import logging


def lambda_handler(event, context):
    logging.info(event)
    try:
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context

        url= os.environ['url']
        c = Client(
            url,
            faults=False
        )
        query_string_app_number = event['app_num'].strip()
        # check if the query param is numeric
        if query_string_app_number.isnumeric():

            res = c.service.fetchAppNumsForSS(query_string_app_number)

            # fetching the status code from response
            status_code = res[0]

            # App Number Computation
            appNumbers = " "
            appNumbers = appNumbers.join(res[1:])
            appNumbers = appNumbers.replace(" ", ",")
            print(f"status code:{status_code}")
            print(f"raw response: {appNumbers}")

            if status_code == 200:
                response = {
                    "fetchAppNumsForSSReturn": appNumbers
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
                    "message": appNumbers
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
