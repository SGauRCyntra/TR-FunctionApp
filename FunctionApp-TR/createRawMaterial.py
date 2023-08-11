from .constants import connection_string, key, source_container_name_qualtrics, destination_container_name_qualtrics
from azure.storage.blob import BlobServiceClient
import logging

class createRawMaterial():
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

            headers = ["ParentFormID", "RawMaterialID", "RawMaterialName", "Status"]
            headers_to_change = ["AssurX_No", "No_Series", "Description", "Item_Status", "Long_Description", "Base_Unit_of_Measure", "Color", "Vendor_No", "Vendor_Item_No", "Purch_Unit_of_Measure", "Country_Region_of_Origin_Code"]
            headers_with_val = ["Item_Category_Code","Product_Group_Code", "Gen_Prod_Posting_Group", "Inventory_Posting_Group", "Tax_Group_Code", "Replenishment_System", "Item_Tracking_Code","Lot_Nos", "E_Ship_Tracking_Code"]
            headers_val = ["ING", "CN", "RM", "RAW", "NONTAX", "PURCHASE", "LOTALL", "LOT", "LOT"]
            orderAdd = []
            for i in range(len(self._payload)):
                dic ={}
                for j in range(len(headers)):
                    dic[headers_to_change[j]] = self._payload[i][headers[j]]
                for k in range(len(headers), len(headers_to_change)):
                    dic[headers_to_change[k]] = None
                for l in range(len(headers_with_val)):
                    dic[headers_with_val[l]] = headers_val[l]
                if dic["Item_Status"] == "Pending":
                    dic["Item_Status"] = "INACTIVE"
                orderAdd.append(dic)
            logging.info(self._payload)

            # new_blob = client.get_blob_client(
            #     self._destination_container_name, self._blob_name)
            
            # new_blob.upload_blob(str(encrypted_data), overwrite=True)

            return 200, orderAdd

        except Exception as e:
            return 404, str(e)