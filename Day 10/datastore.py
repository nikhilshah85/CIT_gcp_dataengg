from google.cloud import datastore

client = datastore.Client()

# Create a new entity
key = client.key('Task', 'sampletask1')
task = datastore.Entity(key=key)
task.update({
    'description': 'Buy milk',
    'done': False
})
client.put(task)

# Fetch entity
retrieved = client.get(key)
print(f"Task: {retrieved['description']} Done: {retrieved['done']}")

# Query entities
query = client.query(kind='Task')
query.add_filter('done', '=', False)
for entity in query.fetch():
    print(entity.key.name, entity['description'])
