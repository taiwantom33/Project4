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
data_init = pd.read_csv(dataset_url)
data=data_init.head(1000)
response = client.list_dataset_contents(datasetName='emission_data')
print(data_init.head(1675))

data['time'] = data.groupby('machine').cumcount()

# Plotting a line plot for each machine
plt.figure(figsize=(10, 6))

for machine, group in data.groupby('machine'):
    plt.plot(group['time'], group['max_co2'], label=f'Machine {machine}', marker='o')

# Adding labels and title
plt.xlabel('Time')
plt.ylabel('Max CO2')
plt.title('Max CO2 Over Time for Each Machine')
plt.legend()

# Show the plot
plt.show()