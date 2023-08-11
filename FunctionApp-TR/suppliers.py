from .constants import connection_string, key, source_container_name_suppliers, destination_container_name_suppliers, country_code_key, country_code_connection_string, country_code_container_name, supplier_file_name
from azure.storage.blob import BlobServiceClient
import logging
import json

class suppliers():
    def __init__(self, file, body) -> None:
        self._blob_name = file
        self._body = body
        self._connection_string =  connection_string
        self._account_key = key
        self._source_container_name = source_container_name_suppliers
        self._country_code_connection_string =  country_code_connection_string
        self._country_code_key = country_code_key
        self._country_code_container_name = country_code_container_name
        self._supplier_file_name = supplier_file_name
        self._destination_container_name = destination_container_name_suppliers
   
    def process(self):
    # Create client
        try:
            client = BlobServiceClient.from_connection_string(
                self._connection_string)

            # container_client = client.get_container_client(self._source_container_name)
            # blob_client = container_client.get_blob_client(self._blob_name)
            # blobstr = blob_client.download_blob().readall().decode("ISO-8859-1")
            # blobstr = blobstr.splitlines()

            client_country_code = BlobServiceClient.from_connection_string(
                self._country_code_connection_string)
            container_client_country_code = client_country_code.get_container_client(self._country_code_container_name)
            blob_client_country_code = container_client_country_code.get_blob_client(self._supplier_file_name)
            blobstr_country_code = blob_client_country_code.download_blob().readall().decode("ISO-8859-1")
            blobstr_country_code = blobstr_country_code.splitlines()
            # logging.info(json.loads(blobstr_country_code[0])["UNITED STATES"])
            
            blobstr_country_code = json.loads(blobstr_country_code[0])

            headers = ["SupplierID", "SupplierNumber", "SupplierName", "Address", "City", "State", "PostalCode", "Country", "Contact", "PhoneNo", "E_Mail"]
            headers_to_change = ["AssurX_No", "No", "Name", "Address", "City", "Country", "Post_Code", "Country_Region_Code", "Contact", "Phone_No", "E_Mail"]
            # dic = { "AssurX_No"  : [], "No": [], "Name": [], "Address": [], "City": [], "Country": [], "Post_Code": [], "Country_Region_Code": [], "Contact": [], "Phone_No": [], "E_Mail": []}
            vendor_detail = []
            for i in range(len(self._body)):
                dic = {}
                for j in range(len(headers)):
                    if headers_to_change[j] ==  "Country_Region_Code":
                        logging.info(self._body[i][headers[j]])
                        dic[headers_to_change[j]] =blobstr_country_code[self._body[i][headers[j]]]
                    else:
                        dic[headers_to_change[j]] = self._body[i][headers[j]]
                vendor_detail.append(dic)

            
            logging.info(vendor_detail)
            
            new_blob = client.get_blob_client(
                self._destination_container_name, self._blob_name)
            new_blob.upload_blob(json.dumps(dic), overwrite=True)

            return 200, vendor_detail

        except Exception as e:
            return 404, str(e)