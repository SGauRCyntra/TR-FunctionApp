from .commonfuncs import xml_to_json
import logging
import json


class complaints2():
    def __init__(self, body) -> None:
        self._payload = body
   
    def process(self):
    # Create client
        try:
            headers_assurx_input = ['ActionID', 'StandardText020', 'ShortText2', 'Title', 'StandardText032', 'Date2', 'StandardText024', 'StandardText019', 'Memo1', 'StandardText043', 'StandardText006', 'StandardText010', 'StandardText042', 'StandardText026', 'StandardText048', 'DateClosedGoal', 'StandardText014']
            payload1 = self._payload["Salesforce"]
            payload2 = self._payload["Assurx"]
            null_dic = {}
            for i in range(len(headers_assurx_input)):
                null_dic[headers_assurx_input[i]]= None
            payload = []
            for i in range(len(payload1)):
                for j in range(i,len(payload2)):
                    logging.info(payload1[i])
                    if payload1[i]["SalesforceCaseNumber"] == payload2[j]["StandardText020"]:
                        payload.append({**payload1[i], **payload2[j]})
                    else:
                        payload.append({**payload1[i], **null_dic})
            return 200, payload


        except Exception as e:
            return 404, str(e)