from .constants import connection_string, key, source_container_name_qualtrics, destination_container_name_qualtrics
from azure.storage.blob import BlobServiceClient
import logging
from .constants import company

class loadProduction():
    def __init__(self, body) -> None:
        # self._blob_name = blob_name
        self._payload = body
        self._connection_string =  connection_string
        self._account_key = key
        self._source_container_name = source_container_name_qualtrics
        self._destination_container_name = destination_container_name_qualtrics
   
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
            headers = ["FT Item", "Routing No", "Location", "Flavor", "Item No", "Long Description", "Quantity Per", "UOM", "Item Category", "Product Group", "FG Description", "Units Pack", "L1ItemQty", "L2ItemQty"]
            headers_to_change = ["FG Item","Routing No","Location","Flavor","Item No","Long Description","Quantity Per","UOM","Item Category","Product Group","FG Description","Units Pack","L1ItemQty","L2ItemQty"]
            order = ""
            headers_for_company = [0, 2, 4]
            
            for j in range(len(headers_to_change)-1):
                order += headers_to_change[j] +","
            order += headers_to_change[-1]
            order += "\n"
            for i in range(len(self._payload)):
                if i ==0:
                    for k in range(len(headers_for_company)):
                        if headers[headers_for_company[k]] in self._payload[i]:
                            order += self._payload[i][headers[0]]
                        else:
                            order += ""
                for j in range(len(headers)-1):
                    # if j==0: 
                        # if company == company:
                        #     order += self._payload[i][headers[0]] + "-" + self._payload[i][headers[2]]+ "-" + self._payload[i][headers[4]] +","
                        # else:
                        #     order += self._payload[i][headers[0]] + "-" + self._payload[i][headers[2]]+ "-" + self._payload[i][headers[4]] + "-" + "BIC" +","
                        # order += company + ","
                    if headers[j] in self._payload:
                        order += str(self._payload[i][headers[j]]) +","
                    else:
                        order += ","
                if headers[-1] in self._payload[i]:
                    order += str(self._payload[i][headers[-1]]) + "\n"
                else:
                    order += "\n"
            logging.info(self._payload)

            # new_blob = client.get_blob_client(
            #     self._destination_container_name, self._blob_name)
            
            # new_blob.upload_blob(str(encrypted_data), overwrite=True)

            return 200, order

        except Exception as e:
            return 404, str(e)