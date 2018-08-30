import requests
import json  
print("NOTE: Before beginning please ensure you have Requests: HTTP for Humans installed.");

# For Axiomatics, this would look like: 
# https://localhost.localdomain:8643/asm-pdp/authorize
uri =(raw_input('What is your REST authorization endpoint?'));

# We included request.json as an example file, which is also illustrative of
# the structure required for the input.

jsonfile = (raw_input('What is the location of your JSON file?'));
json_payload = open(jsonfile);
datastore = json.load(json_payload);

uri = str(uri);

# This is required for the request to work.
headers = {'Content-type': 'application/xacml+json'};
# verify=False returns a warning regarding certificate validation from urllib3. 
# Please address this if moving to production.
r = requests.post(uri, data=json.dumps(datastore),verify=False, auth=('pdp-user', 'password'), headers=headers);

# Return the response.
print(r.text);          
