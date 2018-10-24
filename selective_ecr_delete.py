import boto3
import re

#Initialise ECR code
client = boto3.client('ecr','region=us-east-1')

# Code to find ACC number
sts_client = boto3.client('sts')
registry_id = sts_client.get_caller_identity()["Account"]
repository_name='test_delete'

stack_id='abcdefg'
awx_version='1.0.1'

# create repo if it does not already exist
response = client.describe_repositories(
    registryId=registry_id,
    repositoryNames [
        repository_name
    ]
)

# Create if it does not exist
if response.length == 0:
    response = client.create_repository(
        repositoryName=repository_name
    )

# Call CLI to push images with tags
# push dummy image with tag
# push dummy image with tag


# List all docker images in the repo
response = ecr_client.describe_images(
    registryId=registry_id,
    repositoryName=repository_name
)

# build list of images to delete
imageIds = []
for imageDetail in response['imageDetails']:

    imageTags = imageDetail['imageTags']
    for imageTag in imageTags:
        pattern = stack_id + '_(.*)'
        if re.match(pattern + '',imageTag):
            imageIds.append(
                {
                    'imageDigest': imageDetail['imageDigest'],
                }
            )

# delete images
response = ecr_client.batch_delete_image(
    registryId=registry_id,
    repositoryName=args.repository_name,
    imageIds=imageIds
)
