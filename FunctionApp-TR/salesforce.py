from .commonfuncs import xml_to_json
import logging
import json


class salesforce():
    def __init__(self, body) -> None:
        self._payload = body
   
    def process(self):
    # Create client
        try:
            headers_output = ['Sub-Category', 'Description', 'DatePurchased', 'CodeDateBottom', 'Brand', 'Item', 'VarietyPackType', 'Subject', 'Plant', 'Category', 'CreatedDate', 'SalesforceCaseNumber', 'CodeDateTop', 'Flavor', 'Id', 'Date/TimeClosed']
            headers_input = ['Sub_Category__c', 'Description', 'Date_Purchased__c', 'Code_Date_Bottom__c', 'Brand__c', 'Item__c', 'Variety_Pack_Type__c', 'Subject', 'Plant__c', 'Category__c', 'CreatedDate', 'CaseNumber', 'Code_Date_Top__c', 'Flavor__c','Id', 'ClosedDate']
            arr_payload = []
            for i in range(len(self._payload)):
                dic= {}
                for j in range(len(headers_input)):
                    dic[headers_output[j]] = self._payload[i][headers_input[j]]
                arr_payload.append(dic)
            return 200, json.dumps(arr_payload)


        except Exception as e:
            return 404, str(e)