import boto3

s3 = boto3.resource('s3')

#s3.Bucket('mi-bucket-unaj').upload_file("nubes.ods","nubes.ods")
#s3.Bucket('mi-bucket-unaj').download_file("nubes.ods","nubes_nuevo.ods")
respuesta = s3.Object('mi-bucket-unaj','algo2.txt').get()
print(respuesta['Body'].read())