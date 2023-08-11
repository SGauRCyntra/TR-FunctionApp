from .commonfuncs import xml_to_json
import logging
import json


class assurx():
    def __init__(self, body) -> None:
        self._payload = body
   
    def process(self):
    # Create client
        try:
            # logging.info(json.loads(self._payload)["soap:Envelope"]["soap:Body"]["QuerySQLSimpleResponse"]["diffgr:diffgram"]["NewDataSet"]["Table1"])
            payload = json.loads(self._payload)["soap:Envelope"]["soap:Body"]["QuerySQLSimpleResponse"]["diffgr:diffgram"]["NewDataSet"]["Table1"]
            logging.info(payload)
            for i in range(len(payload)):
                logging.info("njsnansj")
                logging.info(payload[i])
                del payload[i]["@diffgr:id"]
                del payload[i]["@msdata:rowOrder"]
            return 200, json.dumps(payload)


        except Exception as e:
            return 404, str(e)