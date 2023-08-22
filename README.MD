# Bulk loading files to DELL EMC object storage

Note: This script is based off of the one from [here](https://min.io/docs/minio/linux/developers/python/minio-py.html)

## Steps: 

1) Pip install Minio:

* pip3 install minio

2) Pip install dotenv

* pip install python-dotenv

3) Download the source:

* git clone https://github.com/minio/minio-py
* cd minio-py
* python setup.py install

4) Copy the contents of `.env.example` into a new file`.env`, and update the values as appropriate.

5) update the OBJECT and FILE variables with their appropriate values

* Note: the secret key can be found by going to: 

* https://mgmt.objectstore.gov.bc.ca/#/vdc//provisioning/users/object
* find the object user, associated with the the bucket your using, in the list
* click on the edit button
* the secret key can be found under the Object Access section 

6) After running the script, you can view the upload through an S3 client such as S3 browser

* If you choose to use S3 browser, when adding an account ensure to select: S3 compatible storage for the account type