from .constants import country_code_connection_string, country_code_key, source_container_name_anaplan, destination_container_name_anaplan, archive_container_name, error_container_name
from azure.storage.blob import BlobServiceClient
from .commonfuncs import get_current_date_and_time_as_string
import logging
from .commonfuncs import is_csv, delete_blob

headers = ["Payroll ID Number","First name","Last name","Preferred Name","Email","Start date","Departure date","Job Title","DOL Status","Reports To Full Name","Cost Center Hierarchy","Cost Center ID","Cost Center Name","Job Family"]
headers_to_take = ["Employee ID","Legal Name - First Name","Legal Name - Last Name","Full Name","Email - Primary Work","Worker's Manager","Active Status","Job Title","Hire Date","Termination Date","Time Type","Cost Center Hierarchy","Cost Center - ID","Cost Center - Name","Job Family"]

class anaplan():
    def __init__(self, blob_name) -> None:
        self._blob_name = blob_name
        logging.info(blob_name)
        self._connection_string =  country_code_connection_string
        self._account_key = country_code_key
        self._source_container_name = source_container_name_anaplan
        self._destination_container_name = destination_container_name_anaplan
        self._archive_container_name = archive_container_name
        self._error_container_name = error_container_name
   
    def process(self):
    # Create client
        try:
            client = BlobServiceClient.from_connection_string(
                self._connection_string)

            container_client = client.get_container_client(self._source_container_name)
            blob_client = container_client.get_blob_client(self._blob_name)
            blobstr = blob_client.download_blob().readall().decode("ISO-8859-1")
            if not is_csv(self._blob_name):
                # error_blob = client.get_blob_client(
                # self._error_container_name, self._blob_name[:-4] +"_" + get_current_date_and_time_as_string().replace(" ","").replace("-","").replace(":","")+ self._blob_name[-4:])
                # error_blob.upload_blob(blobstr, overwrite=True)
                # delete_blob(client, self._source_container_name, self._blob_name)
                return 400, "Not a CSV file"
            new_blobstr = blobstr.splitlines()
            if new_blobstr[0] != ",".join(headers_to_take):
                # error_blob = client.get_blob_client(
                # self._error_container_name, self._blob_name[:-4] +"_" + get_current_date_and_time_as_string().replace(" ","").replace("-","").replace(":","")+ self._blob_name[-4:])
                # error_blob.upload_blob(blobstr, overwrite=True)
                # delete_blob(client, self._source_container_name, self._blob_name)
                return 400, "Error in file"
            new_blobstr[0] = ", ".join(headers)
            data =''
            j=1
            for i in range(len(new_blobstr)):
                    line = new_blobstr[i].split(",")
                    line[7].replace(',','-')
                    data += ','.join(line) + '\n'   
            # Create new blob and start upload operation
            print(self._blob_name[:-4] + get_current_date_and_time_as_string().replace(" ","").replace("-","").replace(":","")+".csv")
            
            archive_blob = client.get_blob_client(
                self._archive_container_name, "Archived_" + self._blob_name[:-4] +"_" + get_current_date_and_time_as_string().replace(" ","").replace("-","").replace(":","")+".csv")
            archive_blob.upload_blob(blobstr, overwrite=True)
            
            delete_blob(client, self._source_container_name, self._blob_name)

            new_blob = client.get_blob_client(
            self._destination_container_name, "Output_" + self._blob_name[:-4] +"_" + get_current_date_and_time_as_string().replace(" ","").replace("-","").replace(":","")+".csv")
            new_blob.upload_blob(data, overwrite=True)

            return 200, "Output_"+self._blob_name

        except Exception as e:
            return 404, str(e)