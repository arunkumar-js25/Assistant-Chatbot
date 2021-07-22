from tqdm import tqdm
import requests


# the url of file you want to download
#Page also we can download -- url = "https://www.download32.com/numxl-d152661.html"

url = "https://www.download32.com/go/390675/http%3A%2F%2Fstockalyze.com%2Fdownload%2Fstockalyze_setup.exe"
#NOTE: without slash in end

# read 1024 bytes every time 
buffer_size = 1024
# download the body of response by chunk, not immediately
response = requests.get(url, stream=True)

# get the total file size
#Content-Length header parameter is the total size of the file in bytes.
file_size = int(response.headers.get("Content-Length", 0))
# get the file name
filename = "DownloadFile\\"+ url.split("/")[-1]

# progress bar, changing the unit to bytes instead of iteration (default by tqdm)
progress = tqdm(response.iter_content(buffer_size), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "wb") as f:
    for data in progress:
        # write data read to the file
        f.write(data)
        # update the progress bar manually
        progress.update(len(data))