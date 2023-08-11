# from pgpy import PGPKey, PGPMessage
import logging
from datetime import datetime
import json
import xmltodict

def xml_to_json(xml_string):
  json_dict = xmltodict.parse(xml_string)
  json_string = json.dumps(json_dict)
  return json_string

def convert_date_format(date_string):
    # Convert the input string to a datetime object
    datetime_obj = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")

    # Format the datetime object into the desired format
    formatted_date = datetime_obj.strftime("%m/%d/%Y")

    return formatted_date

def delete_blob(blob_service_client, container_name, blob_name):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    blob_client.delete_blob()

def get_current_date_and_time_as_string():
  """Returns the current date and time as a string."""
  import datetime

  now = datetime.datetime.now()
  return now.strftime("%Y-%m-%d %H:%M:%S")

def is_csv(data):
  if data[len(data)-3:]=="csv":
      return True
  else:
      return False
  # pattern = r"^,\s*(.*?)\s*,\s*$"
  # match = re.search(pattern, data)
  # if match:
  #   return True
  # else:
  #   return False


def pgp_encrypt(plain_text, recipient_public_key):
    #   logging.info(type(empty_key))
    # pubkey, _ = PGPKey.from_file("FA-TR-HTTP\pgp_key.asc")
    # message = PGPMessage.new(plain_text)
    # encrypted_message = pubkey.encrypt(message)
    # logging.info(encrypted_message)

    # return encrypted_message
      return True

# def decrypt_message(message, public_key):
#     pubkey, _ = PGPKey.from_file("FA-TR-HTTP\pgp_key.asc")

#     # Decrypt the message using the recipient's public key.
#     decrypted_message = pubkey.decrypt(message)

#     # Return the plaintext message.
#     return decrypted_message.message