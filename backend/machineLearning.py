import requests
import asyncio

api_key = 'WQsFNeUUTlbh'
username = 'mansooranis'
classifierName = 'mh'

async def userDataProcessed(userData):
    finalText = "+".join(userData.split())
    url = f'https://api.uclassify.com/v1/{username}/{classifierName}/classify/?readKey={api_key}&text={finalText}'
    response = requests.get(url)
    return response.json()