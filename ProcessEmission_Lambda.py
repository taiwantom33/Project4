#
# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#

# greengrassHelloWorldCounter.py
# Demonstrates a simple publish to a topic using Greengrass core sdk
# This lambda function will retrieve underlying platform information and send a hello world message along with the
# platform information to the topic 'hello/world/counter' along with a counter to keep track of invocations.
#
# This Lambda function requires the AWS Greengrass SDK to run on Greengrass devices.
# This can be found on the AWS IoT Console.

import json
import logging
import platform
import sys
import time

import greengrasssdk

# Setup logging to stdout
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Creating a greengrass core sdk client
client = greengrasssdk.client("iot-data")

# Retrieving platform information to send from Greengrass Core
my_platform = platform.platform()

# Counter to keep track of invocations of the function_handler
my_counter= 0
max_co2 = [0 for _ in range(5)]

def lambda_handler(event, context):
    global max_co2
    global my_counter
    machine=int(event['machine'])
    my_counter = my_counter + 1
    new_data=float(event['data'])
    if new_data>max_co2[machine]:
        max_co2[machine]=new_data
    try:      
        client.publish(
            topic="emission/data",
            queueFullPolicy="AllOrException",
            payload=json.dumps(
                {
                    "CO2": max_co2[machine],
                    "machine": machine
                }
            ),
        )
        
    except Exception as e:
        logger.error("Failed to publish message: " + repr(e))
    return