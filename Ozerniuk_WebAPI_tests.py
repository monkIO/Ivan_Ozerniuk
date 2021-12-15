import requests
import json

#Upload request
url_upload = "https://content.dropboxapi.com/2/files/upload"
payload_upload = "Ozerniuk Ivan KA-91 TEST"
headers_upload = {
  'Dropbox-API-Arg': '{"path": "/Matrices.txt","mode": "add","autorename": true,"mute": false,"strict_conflict": false}',
  'Content-Type': 'application/octet-stream',
  'Authorization': 'Bearer 8Yohtu637QUAAAAAAAAAAQTrs_xEgiUMdxcDetdP6HxpDcNLKje3RYoBtuoW_8d1'
}

response_upload = requests.request("POST", url_upload, headers=headers_upload, data=payload_upload)

if not response_upload.ok:
    raise Exception(f"Could not upload a file. Got {response_upload.status_code} error.")
else:
    print("Successfully uploaded!")


#Get file metadata request
url_gfm = "https://api.dropboxapi.com/2/files/get_metadata"
payload_gfm = json.dumps({
  "path": "/Matrices.txt"
})
headers_gfm = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer 8Yohtu637QUAAAAAAAAAAQTrs_xEgiUMdxcDetdP6HxpDcNLKje3RYoBtuoW_8d1'
}

response_gfm = requests.request("POST", url_gfm, headers=headers_gfm, data=payload_gfm)

if not response_gfm.ok:
    raise Exception(f"Could not get file metadata. Got {response_gfm.status_code} error.")
else:
    print("Successfully got file metadata!")
    
    
#Delete request
url_delete = "https://api.dropboxapi.com/2/files/delete_v2"
payload_delete = json.dumps({
  "path": "/Matrices.txt"
})
headers_delete = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer 8Yohtu637QUAAAAAAAAAAQTrs_xEgiUMdxcDetdP6HxpDcNLKje3RYoBtuoW_8d1'
}

response_delete = requests.request("POST", url_delete, headers=headers_delete, data=payload_delete)

if not response_delete.ok:
    raise Exception(f"Could not delete the file. Got {response_delete.status_code} error.")
else:
    print("Successfully deleted the file!")

