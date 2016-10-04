Download and install Python 3.5 (https://www.python.org/downloads/release/python-352/), then:

```
pip3.5 install -r requirements.txt
brew install kafka
brew services start zookeeper
brew services start kafka
python3.5 server.py
```

Now open client.html, then run `python3.5 kafka_producer.py 50` and check your browser!
