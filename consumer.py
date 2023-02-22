# # Import KafkaConsumer from Kafka library
# from kafka import KafkaConsumer

# # Import sys module
# import sys

# # Define server with port
# bootstrap_servers = ['localhost:29092']

# # Define topic name from where the message will recieve
# topicName = 'demo1'

# # Initialize consumer variable
# consumer = KafkaConsumer (topicName, bootstrap_servers =
#    bootstrap_servers)

# # Read and print message from consumer
# for msg in consumer:
#     print("Topic Name=%s,Message=%s"%(msg.topic,msg.value))

# # Terminate the script
# sys.exit()


import json

f = open('json.txt')

data = json.load(f)

print(data)