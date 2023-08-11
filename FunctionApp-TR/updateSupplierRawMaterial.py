from .constants import connection_string, key, source_container_name_qualtrics, destination_container_name_qualtrics
from azure.storage.blob import BlobServiceClient
import logging

class updateSupplierRawMaterial():
    def __init__(self, body) -> None:
        # self._blob_name = blob_name
        self._payload = body
        # self._connection_string =  connection_string
        # self._account_key = key
        # self._source_container_name = source_container_name_qualtrics
        # self._destination_container_name = destination_container_name_qualtrics
   
    def process(self):
    # Create client
        try:
            # client = BlobServiceClient.from_connection_string(
            #     self._connection_string)

            # container_client = client.get_container_client(self._source_container_name)
            # blob_client = container_client.get_blob_client(self._blob_name)
            # blobstr = blob_client.download_blob().readall().decode("ISO-8859-1")
            # blobstr = blobstr.splitlines()
            # print(blobstr)

            headers = ["SupplierNo", "RawMaterialNo"]
            headers_to_change = ["Vendor_No" ,"Item_No"]
            orderAdd = []
            for i in range(len(self._payload)):
                dic ={}
                for j in range(len(headers)):
                    dic[headers_to_change[j]] = self._payload[i][headers[j]]
                orderAdd.append(dic)
            logging.info(self._payload)

            # new_blob = client.get_blob_client(
            #     self._destination_container_name, self._blob_name)
            
            # new_blob.upload_blob(str(encrypted_data), overwrite=True)

            return 200, orderAdd

        except Exception as e:
            return 404, str(e)