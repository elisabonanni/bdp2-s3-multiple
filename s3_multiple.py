import requests

files = open("file.txt")
for line in files:
    line=line.rstrip()
    url = 'https://ebonanni.s3.amazonaws.com/'+line # this is the URL of your S3 file (it must be public)
    r = requests.get(url)
    open("output_"+line, 'wb').write(r.content) # put a name for the output file here

