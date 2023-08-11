from .constants import connection_string, key, source_container_name_qualtrics, destination_container_name_qualtrics
from azure.storage.blob import BlobServiceClient
from .commonfuncs import pgp_encrypt
from .constants import recipient_public_key
import logging

class qualitrics():
    def __init__(self, blob_name) -> None:
        self._blob_name = blob_name
        self._connection_string =  connection_string
        self._account_key = key
        self._source_container_name = source_container_name_qualtrics
        self._destination_container_name = destination_container_name_qualtrics
   
    def process(self):
    # Create client
        try:
            client = BlobServiceClient.from_connection_string(
                self._connection_string)

            container_client = client.get_container_client(self._source_container_name)
            blob_client = container_client.get_blob_client(self._blob_name)
            blobstr = blob_client.download_blob().readall().decode("ISO-8859-1")
            # blobstr = blobstr.splitlines()
            # print(blobstr)
            logging.info(blobstr)
            encrypted_data = pgp_encrypt(blobstr, recipient_public_key)
            logging.info("Returning--------------------")
            # logging.info(encrypted_data)
            # decrypted_data = decrypt_message(encrypted_data, recipient_public_key)
            # logging.info(decrypted_data)
            new_blob = client.get_blob_client(
                self._destination_container_name, self._blob_name)
            
            new_blob.upload_blob(str(encrypted_data), overwrite=True)

            return 200, "Successfully Processed!"

        except Exception as e:
            return 404, str(e)