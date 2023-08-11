from .constants import country_code_connection_string, country_code_key, source_container_name_anaplan, destination_container_name_anaplan
from azure.storage.blob import BlobServiceClient
from .commonfuncs import get_current_date_and_time_as_string
import logging
from .commonfuncs import is_csv

headers = ["Payroll ID Number","First name","Last name","Preferred Name","Email","Start date","Departure date","Job Title","DOL Status","Reports To Full Name","Cost Center Hierarchy","Cost Center ID","Cost Center Name","Job Family"]

class anaplan():
    def __init__(self, body) -> None:
        # self._blob_name = blob_name
        # logging.info(blob_name)
        self._payload = body
        self._connection_string =  country_code_connection_string
        self._account_key = country_code_key
        self._source_container_name = source_container_name_anaplan
        self._destination_container_name = destination_container_name_anaplan
   
    def process(self):
    # Create client
        try:
            # client = BlobServiceClient.from_connection_string(
            #     self._connection_string)

            # container_client = client.get_container_client(self._source_container_name)
            # blob_client = container_client.get_blob_client(self._blob_name)
            # blobstr = blob_client.download_blob().readall().decode("ISO-8859-1")
            # logging.info(blobstr)
            # blobstr[0] = ", ".join(headers)
            data =''
            j=1
            for i in range(len(blobstr)):
                    line = blobstr[i].split(",")
                    line[7].replace(',','-')
                    data += ','.join(line) + '\n'   
            print(data)  
            print(self._blob_name[:-4] + get_current_date_and_time_as_string().replace(" ","").replace("-","").replace(":","")+".csv")
            # Create new blob and start upload operation
            new_blob = client.get_blob_client(
                self._destination_container_name, "Output_"+self._blob_name)
            new_blob.upload_blob(data, overwrite=True)

            return 200, "Output_"+self._blob_name

        except Exception as e:
            return 404, str(e)



def map_payload(payload01, indexOfPayload01):
  """
  Maps the MuleSoft payload to a Python dictionary.

  Args:
    payload01: The MuleSoft payload.
    indexOfPayload01: The index of the payload in the list of payloads.

  Returns:
    A Python dictionary.
  """

  dictionary = {
    "origin": payload01.Origin,
    "Age__c": payload01.Age__c,
    "External_Case_ID__c": payload01.External_Case_ID__c,
    "Store_Address__c": payload01.Store_Address__c,
    "Days_Expired_Or_Remaining__c": payload01.Days_Expired_Or_Remaining__c,
    "Plant_Test__c": payload01.Plant_Test__c,
    "Code_Date_Bottom__c": payload01.Code_Date_Bottom__c,
    "type": payload01.type,
    "Package__c": payload01.Package__c,
    "Variety_Pack_Type__c": payload01.Variety_Pack_Type__c,
    "Web_Type__c": payload01.Web_Type__c,
    "Bottle_Status__c": payload01.Bottle_Status__c,
    "Company_Organization_Name__c": payload01.Company_Organization_Name__c,
    "Plant__c": payload01.Plant__c,
    "City__c": payload01.City__c,
    "SuppliedName": payload01.SuppliedName,
    "Inquiry_Category__c": payload01.Inquiry_Category__c,
    "Metropolitan_Area__c": payload01.Metropolitan_Area__c,
    "Due_Date__c": payload01.Due_Date__c,
    "SuppliedPhone": payload01.SuppliedPhone,
    "Code_Date_Top__c": payload01.Code_Date_Top__c,
    "Flavor__c": payload01.Flavor__c,
    "Root_Cause__c": payload01.Root_Cause__c,
    "Vendor_Goods_Or_Services__c": payload01.Vendor_Goods_Or_Services__c,
    "Status": payload01.Status,
    "Sub_Category__c": payload01.Sub_Category__c,
    "IsDeleted": payload01.IsDeleted,
    "Priority": payload01.Priority,
    "UPC_Code__c": payload01.UPC_Code__c,
    "Item__c": payload01.Item__c,
    "State_Province__c": payload01.State_Province__c,
    "IsEscalated": payload01.IsEscalated,
    "Category__c": payload01.Category__c,
    "Flavor_Suggestion__c": payload01.Flavor_Suggestion__c,
    "CreatedDate": payload01.CreatedDate,
    "Coupon_Total__c": payload01.Coupon_Total__c,
    "First_Name__c": payload01.First_Name__c,
    "Originating_Customer_Ticket__c": payload01.Originating_Customer_Ticket__c,
    "Store_Purchased__c": payload01.Store_Purchased__c,
    "Last_Name__c": payload01.Last_Name__c,
    "Description": payload01.Description.replace("\n", ""),
    "SuppliedCompany": payload01.SuppliedCompany,
    "Date_Purchased__c": payload01.Date_Purchased__c,
    "ContactId": payload01.ContactId,
    "IsClosed": payload01.IsClosed,
    "Reason": payload01.Reason,
    "SuppliedEmail": payload01.SuppliedEmail,
    "ContactPhone": payload01.ContactPhone,
    "OwnerId": payload01.OwnerId,
    "Sample_Status__c": payload01.Sample_Status__c,
    "Shipping_Expense__c": payload01.Shipping_Expense__c,
    "RecordTypeId": payload01.
