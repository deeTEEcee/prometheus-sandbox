# Example taken from https://github.com/prometheus/client_python
# The library provides a few different ways to collect data and this is one of them. 

# In this example, we have a running http server where all endpoints will redirect to the same page that lists all the metrics in a certain format. 
# When configuring prometheus (whether in the service itself or 3rd party providers), it may expect a '/metrics' endpoint but since all endpoints redirect, this makes that trivial.


from prometheus_client import start_http_server
from prometheus_client.core import Counter, Gauge
import time

counter = 0

# This will reset to 0 everytime we restart. If you want something like state, you should use a Gauge and store state somewhere like a database. 
c = Gauge('sample_counter_int', 'Description text')

start_http_server(8000)
while True:
    print("Server is running.")
    c.inc()
    time.sleep(5)