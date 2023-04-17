from asyncore import write
import http.client
import json
import csv

#accessing the API
conn = http.client.HTTPSConnection("url goes here")
payload = ''  

headers = {
    'client-id': 'client id goes here',
    'client-secret': 'client secret goes here'
  }

conn.request("GET", "/api/devices", payload, headers)
res = conn.getresponse()
data = res.read()
data = json.loads(data)
deviceName = []
serialNumber = []
imei = []
online = []
lastOnline = []
agentid = []
cc = []
lastBackup = []
freeSpace = []
productName = []
version = []
number = []

for device in data:
  deviceName.append(device['Device Name'])
  serialNumber.append(device['Serial Number'])
  imei.append(device['iMEI'])
  number.append(device['Phone Number'])
  online.append(device['Online'])
  lastOnline.append(device['Last Online'])
  agentid.append(device['agentid']) 
  cc.append(device['Current Carrier'])
  lastBackup.append(device['Days Since Last Cloud Backup'])
  freeSpace.append(device['Free Disk Space (GB)'])
  productName.append(device['Product Name'])
  version.append(device['System Version'])
  
with open('Addigy-Report.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Device Name', 'Serial Number', 'IMEI','Phone Number', 'Current Carrier',
     'Product Name', 'System Version', 'Free Disk Space (GB)', 'Days Since Last Cloud Backup', 'Online', 'Last Online', 'Agent ID'])
    for i in range(len(deviceName)):
        writer.writerow([deviceName[i], serialNumber[i], imei[i], number[i], 
        cc[i], productName[i], version[i], freeSpace[i], lastBackup[i], online[i], lastOnline[i], agentid[i]])
