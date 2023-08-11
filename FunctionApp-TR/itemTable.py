from .constants import connection_string, key, source_container_name_qualtrics, destination_container_name_qualtrics
from azure.storage.blob import BlobServiceClient
import logging
from .constants import company
from .commonfuncs import convert_date_format

class itemTable():
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
            headers = ["x0032_04oz_Case_Equivalent","Unit Price", "Base_Unit_of_Measure","Blocked", "Brand", "Country_Region_of_Origin_Code", "Description ", "Expiration_Calculation", "Flammable", "Flavor_Description ", "Flavor", "Gen_Prod_Posting_Group","Inner_Packs_per_Case", "Last_Date_Modified", "Last_Direct_Cost", "Long_Description", "No", "Item_Category_Code", "Item_Status","No_2", "Package_Type", "Package_Type_Description ", "Pallet_Item_No", "Product_Group_Code", "Product_Group_Description ", "Product_Line_Description", "Product_Line", "Production_BOM_No", "Purch_Unit_of_Measure", "Unit_Cost", "Routing_No", "Salable_Expiration_Date", "Std_Pack_Unit_of_Measure_Code", "Units_per_Pack", "Gen_Unit_Volume"]
            headers_to_change =  [
                "Company", "204oz Case Equivalent", "Average Selling Price",
                "Base Unit of Measure", "Blocked", "Brand", "Country/Region of Origin Code",
                "Description", "Expiration Calculation", "Flammable",
                "Flavor Description", "Flavor", "Gen. Prod. Posting Group", "Inner Packs per Case",
                "Last Date Modified", "Last Direct Cost", "Long Description", "Item No",
                "Item Category Code", "Item Status", "No. 2", "Package Type",
                "Package Type Description", "Pallet Item No", "Product Group Code",
                "Product Group Description", "Product Line Description", "Product Line Code",
                "Production BOM No", "Purch. Unit of Measure", "Rolled-Up Material Cost",
                "Routing No", "Salable Expiration Date", "Std. Pack Unit of Measure Code",
                "Units per Pack", "Unit Volume"
            ]
            order = ""
            for j in range(len(headers_to_change)-1):
                order += str(headers_to_change[j]) +","
            order += str(headers_to_change[-1]) + "\n"
            
            for i in range(len(self._payload)):
                for j in range(len(headers)-1):
                    if j==0:
                        order += company + ","
                    if headers[j] in self._payload[i]:
                        logging.info(self._payload[i][headers[j]])
                        order += str(self._payload[i][headers[j]]) +","
                    else:
                        order+=","
                    # logging.info(self._payload[i][headers[-1]])
                if headers[-1] in self._payload[i]:
                    order += str(self._payload[i][headers[-1]]) + "\n"
            logging.info(order)
            
            # new_blob = client.get_blob_client(
            #     self._destination_container_name, self._blob_name)
            
            # new_blob.upload_blob(str(encrypted_data), overwrite=True)

            return 200, order

        except Exception as e:
            return 404, str(e)