Download and install Python 3.5 (https://www.python.org/downloads/release/python-352/).

```
pip3.5 install -r requirements.txt
brew install kafka
brew services start zookeeper
brew services start kafka
python3.5 server.py
open client.html
```

Now from the `python3.5` shell:

```
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost')
producer.send('mytopic', b'Hello World').get(timeout=60)
```
