import requests


url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"

Reg_NUM = input('reg num: ')
payload_response = '{\n\t\"registrationNumber\": \"'+ Reg_NUM + '\"\n}'


headers = {
  'x-api-key': 'API-key-here',
  'Content-Type': 'application/json'
}


response = requests.request("POST", url, headers=headers, data = payload_response)

print(response.text.encode('utf8'))
