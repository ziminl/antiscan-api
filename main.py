






import requests

file_path = 'path/to/your/file.txt'  # Replace with the actual path to your file
##proxy = {'http': 'http://proxy_address:proxy_port', 'https': 'https://proxy_address:proxy_port'}
upload_url = 'https://antiscan.me/api/upload/file'
download_url = 'https://antiscan.me/api/download/result'

files = {'file': open(file_path, 'rb')}
upload_response = requests.post(upload_url, files=files)
##upload_response = requests.post(upload_url, files=files, proxies=proxy)

if upload_response.status_code == 200:
    # File upload successful
    upload_response_json = upload_response.json()
    file_hash = upload_response_json['sha256']
    print('url:', upload_response_json['scan_url'])
    download_params = {'hash': file_hash}
    download_response = requests.get(download_url, params=download_params)
##    download_response = requests.get(download_url, params=download_params, proxies=proxy)
    if download_response.status_code == 200:
        image_file_path = 'path/to/save/downloaded_image.png'
        with open(image_file_path, 'wb') as image_file:
            image_file.write(download_response.content)
        print('pass')
    else:
        print('error:', download_response.text)
else:
    print('Error uploading file:', upload_response.text)


