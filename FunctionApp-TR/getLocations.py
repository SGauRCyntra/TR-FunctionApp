from .constants import connection_string, key, source_container_name_qualtrics, destination_container_name_qualtrics
from azure.storage.blob import BlobServiceClient
import logging
from .constants import company
from .commonfuncs import convert_date_format

class getLocations():
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
            headers = ["Name", "Code", "Address", "City", "County", "Post_Code", "Country_Region_Code"]
            headers_to_change = ["Name", "Code", "Address", "City", "State", "ZipCode", "Country"]

            order = ""
            order += "Company,"
            for j in range(len(headers_to_change)-1):
                order += str(headers_to_change[j]) +","
            order += str(headers_to_change[-1]) + "\n"
            
            for i in range(len(self._payload)):
                for j in range(len(headers)-1):
                    if j==0:
                        order += company + ","
                    if headers[j] in self._payload[i]:
                        order += str(self._payload[i][headers[j]]) +","
                    else:
                        order+=","
                    # logging.info(self._payload[i][headers[-1]])
                logging.info(headers[-1])
                if headers[-1] in self._payload[i]:
                    order += str(self._payload[i][headers[-1]]) + "\n"
            logging.info(order)
            
            # new_blob = client.get_blob_client(
            #     self._destination_container_name, self._blob_name)
            
            # new_blob.upload_blob(str(encrypted_data), overwrite=True)

            return 200, order

        except Exception as e:
            return 404, str(e)