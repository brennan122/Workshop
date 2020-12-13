#!/usr/bin/env python3
import uuid
from confluent_kafka import Producer, Consumer
 
 #Replace <bootstrap ID> with your bootstrap server located under Cluster Settings
 #example of bootstrap server - pkc-ep5dm.us-east-4.aws.confluent.cloud:9092
 #API key is found under API Acess tab 
c = Consumer({
    'bootstrap.servers': '<bootstrap ID>',
    'sasl.mechanism': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username': '<API Key>',
    'sasl.password': '<Secret>',
    'group.id': str(uuid.uuid1()),  # this will create a new consumer group on each invocation.
    'auto.offset.reset': 'earliest'
})

#here we are subscribing to our users topic
c.subscribe(['users'])
 
try:
    while True:
        msg = c.poll(0.1)  # Wait for message or event/error
        if msg is None:
            # No message available within timeout.
            # Initial message consumption may take up to `session.timeout.ms` for
            #   the group to rebalance and start consuming.
            continue
 
        print('consumed: {}'.format(msg.value()))
 
except KeyboardInterrupt:
    pass
 
finally:
    # Leave group and commit final offsets
    c.close()
