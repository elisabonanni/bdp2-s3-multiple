# bdp2-s3-multiple

To upload to the S3 bucket all the images in the */data* directory in the VM2 use the command in local:
```
scp -ri /Users/elisa/Documents/Bioinformatics/BDP2/Esercizi/bdp2.pem ubuntu@ec2-44-193-76-148.compute-1.amazonaws.com:data/ .
```

It will copy all the files in data directory in the current directory from which the command is executed. The -r flag is used to recursively copy all the files with the .pdf extension.

Then the files are uploaded to the S3 bucket through the AWS interface.

To retrieve all the files from S3 bucket on the virtual machine, firstly download the *index.html* file, which will contains all the objects present in the bucket (in this case _ebonanni_). Remember that to perform all the following operations the bucket must be public.

```
wget https://ebonanni.s3.amazonaws.com/ --output-document=test.xml
```

The html file is a little confusing, so, to retrieve the name of the objects present in the bucket with the .pdf extension can be used the ```grep``` command as follow:
```
grep -o "<Key>.*pdf" <(paste -sd_ index.html) | tr '<>' '\n' | grep -o ".*pdf" > file.txt
```

In this way is created a *file.txt* with all the name of the images.

A python file named *s3_multiple.py* has been created with ```vim``` to download all the elements which name is present in the *file.txt* file:

```
import requests

files = open("file.txt")
for line in files:
    line=line.rstrip()
    url = 'https://ebonanni.s3.amazonaws.com/'+line # URL of the S3 file (it must be public)
    r = requests.get(url)
    open("output_"+line, 'wb').write(r.content) # name for the output file
```

Then, to check in locally to have retrieved the correct images in the right format the following command can be executed:
```
scp -i /Users/elisa/Documents/Bioinformatics/BDP2/Esercizi/bdp2.pem ubuntu@ec2-44-197-219-63.compute-1.amazonaws.com:s3_multiple/output_n02088094_1023_bw.pdf .
```

In this way the *output_n02088094_1023_bw.pdf* image will be downloaded in the directory in which is executed the command.
