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