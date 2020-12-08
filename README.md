# A sandbox to help beginners test prometheus and understand how it works


### Installing on OS X
1. Install Prometheus: `brew install prometheus`
1. `pip install prometheus_client`
1. (Optional) Setup alerts for slack.
* Configure slack to the correct url. 
* Download the darwin directory for alertmanager (https://prometheus.io/download/#alertmanager)
1. The services have been preconfigured for you but you still need to modify a few things:
* Update `prometheus.yml` with the correct rules dir.
* Update `alert_config.yml` for alerts set up with slack. 

### Running the environment ### 
This requires running three processes: prometheus, alertmanager, and the metrics source that prometheus scrapes from.
1. cd into this directory and run "prometheus"
1. If available, run the alertmanager: `./alertmanager --config.file="<insert_dir_here>/prometheus-sandbox/alert_config.yml`
1. Run `python custom_exporter.py`. 
1. With prometheus running, you can go to the UI with localhost:9090. There is an 'Alerts' tab and after about 15 seconds, it should switch to an "Active" state. 
1. With alerts, you should see a slack message pop up after a minute. (If you didn't get alerts, checking the logs for prometheus and alertmanager or the UI alert page is a good start)


### Quick Prometheus Startup Advice ###
* A simple http endpoint with a `/metrics` endpoint that will provide metrics in a prometheus style format. If you already have some useful monitoring data but it isn't in a prometheus format, then I would search up whether they have an existing exporter that would help you do that in https://prometheus.io/docs/instrumenting/exporters/
* We have two simple goals here:
    * Create an alert for our system. (At the very least, requires a metric)
    * Add metrics that would be useful. These don't necessarily have to turn into alerts. 
* I would not recommend using pushgateway because imo, it just adds an extra layer to the service. I'd try a custom exporter like the example in `custom_exporter.py`. 
