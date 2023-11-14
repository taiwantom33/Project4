%matplotlib inline
import boto3
import pandas as pd
import matplotlib.pyplot as plt

# Configure your AWS credentials and region
aws_access_key_id = 'AKIA44JK72ZOSSIVNAX4'
aws_secret_access_key = 'Jvay3b900YEI69ab/yWwvDFu+s0szeoO5sic7c9l'
region_name = 'us-east-1'

# Initialize the IoT Analytics client
client = boto3.client('iotanalytics', region_name=region_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Now you can use the 'client' variable to make calls to AWS IoT Analytics
dataset_url = client.get_dataset_content(datasetName='emission_data')['entries'][0]['dataURI']
data = pd.read_csv(dataset_url)
response = client.list_dataset_contents(datasetName='emission_data')
print(data.max_co2)

fig, ax = plt.subplots()
bars = ax.bar(data.machine, data.max_co2, color=['green'])
ax.set_xlabel('Machine', fontsize=12)
ax.set_ylabel('Max CO2', fontsize=12)
ax.set_title('Max CO2 Levels for Machines', fontsize=14)

# Adjusting the size of x and y axes labels
ax.tick_params(axis='both', labelsize=10)

# Adding data values on top of bars

# Show the plot
plt.show()

