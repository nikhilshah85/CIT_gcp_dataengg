from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path('cit-training-457207', 'my-topic')
future = publisher.publish(topic_path, b'My first message!')
