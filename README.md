# A way for beginners to test prometheus (using pushgateway). 

### Installing on OS X
0. Install prometheus_client on your python environmen.t 
1. Install Prometheus: `brew install prometheus`
2. Download the darwin directory for alertmanager
3. Configure slack to the correct url. 
4. Sandbox: Configure a new set of alert rules and metrics that go to the pushgateway. For an example, 


### Running the environment ### 
This requires running three processes: prometheus, alertmanager, and the pushgateway. 
1. cd into this directory and run "prometheus"
2. Run the alertmanager and run `./alertmanager --config.file="<insert_dir_here>/sandbox/prometheus-test/alert_config.yml`
3. Run the pushgateway with docker. (see "Using Docker" in https://github.com/prometheus/pushgateway)
4. If you have your alerts properly configured, the remaining thing to do is to insert metrics (the example in main.py has some code that should cause an alert to happen.)
5. Run `ma prometheus_metrics -p 9091`

### Quick Prometheus Startup Advice ###
I would not recommend using pushgateway because imo, it just adds an extra layer to the service. If you can, just use existing exporters or create your own custom exporters. For a prometheus beginner, what does that mean exactly? Well, you normally have the following:
1. A simple http endpoint with a `/metrics` endpoint that will provide metrics in a prometheus style format. If you already have some useful monitoring data but it isn't in a prometheus format, then I would search up whether they have an existing client-side library that would help you do that in https://github.com/prometheus. 
2. Once you have the metrics endpoint setup, it's possible you want to run a prometheus server as well as an alertmanager to have a system that supports alerting you on the fly. That's where you setup configuration which would "scrape" your metrics and record that in a timeseries at different intervals.  
