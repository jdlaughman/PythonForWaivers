#Objective: demonstrate ability to understand API documentation (here, Microsoft Azure) and connect to APIs
#Note: Code will not execute successfully because personal API Key is not provided within code

#import modules
#import module to use POST with Microsoft APIs
import requests

#import JSON module to better view results from API (that will be in JSON format)
import json


#Define API connection details to use Azure Cognitive Comptuer Vision service with a provided image
#provide the API key associated with the service
API_key= "!!!"  #API Key is not provided for security so API interaction will fail

#Define address of MSFT computer vision service.  In documentation, the endpoint is provided as:
service_endpoint = "https://msftvisionapi.cognitiveservices.azure.com/"   

#and specific method of computer vision API (Analyze) as:
method_detail_analyze = "vision/v1.0/analyze"

#Concatenated URL address for API
address_analyze = service_endpoint + method_detail_analyze



#Provide API content and parameter details
#Define HTTP header. Content-Type is application/octet-stream when you pass in an image directly
headers = {"Content-Type": "application/octet-stream", "Ocp-Apim-Subscription-Key": API_key}

#Define additional parameters: Visual Features, Language
parameters  = {"visualFeatures":"Categories,Tags,Description,Color", "language":"en"}

#Define the image path location
image_path = "!!!.jpg"  #image path needs to be provided by user
image_data = open(image_path, "rb").read()



#Call API and diplay results
#Use HTTP POST for call
response = requests.post(address_analyze, headers=headers, params=parameters, data=image_data)

# Display the JSON results returned
results = response.json()
format_results=json.dumps(results, indent=2)
print(format_results)



#Connect to a different method from the API: Describe Image
#URL component for describe image
method_detail_describe = "vision/v1.0/describe"

#Complete API URL address (reuses service endpoint)
address_describe = service_endpoint + method_detail_describe

#Call API and diplay results
#Use HTTP POST for call (note that "headers" and "data" are reused while "params" is not defined this time)
response_describe = requests.post(address_describe, headers=headers, data=image_data)



# Display the JSON results returned
results = response_describe.json()
format_results=json.dumps(results, indent=2)
print(format_results)

