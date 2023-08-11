from .constants import country_code_connection_string, country_code_key, source_container_name_testOrderAddress, destination_container_name_testOrderAddress
from azure.storage.blob import BlobServiceClient
import logging
import json

class testOrderAddress():
    def __init__(self, file) -> None:
        self._blob_name = file
        self._connection_string =  country_code_connection_string
        self._account_key = country_code_key
        self._source_container_name = source_container_name_testOrderAddress
        self._destination_container_name = destination_container_name_testOrderAddress
   
    def process(self):
    # Create client
        try:
            client = BlobServiceClient.from_connection_string(
                self._connection_string)

            container_client = client.get_container_client(self._source_container_name)
            blob_client = container_client.get_blob_client(self._blob_name)
            blobstr = blob_client.download_blob().readall().decode("ISO-8859-1")

            headers = ["SupplierNumber", "FacilityID", "FacilityCode", "FacilityName", "Status"]
            headers_to_change = ["Vendor_No", "AssurX_No", "Code" ,"Name" ,"Status" ,"Address" ,"Address_2" ,"City" ,"County" ,"Post_Code", "Country_Region_Code" ,"Phone_No","Contact" ,"Fax_No" ,"E_Mail"]
            orderAdd = []
            blobstr = json.loads(blobstr)
            for i in range(len(blobstr)):
                dic ={}
                for j in range(len(headers)):
                    dic[headers_to_change[j]] = blobstr[i][headers[j]]
                for k in range(len(headers), len(headers_to_change)):
                    dic[headers_to_change[k]] = None
                orderAdd.append(dic)

            new_blob = client.get_blob_client(
                self._destination_container_name, "output"+self._blob_name)
            
            new_blob.upload_blob(json.dumps(orderAdd), overwrite=True)

            return 200, "Successfully Processed"

        except Exception as e:
            return 404, str(e)