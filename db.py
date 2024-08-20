import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('libros')

#print(table.attribute_definitions)
#print(table.scan(Select='ALL_ATTRIBUTES'))

table.put_item(
        Item={
                'part_key':'id2',
                'nombre':'alejandro',
                'edad':5,
        }
)