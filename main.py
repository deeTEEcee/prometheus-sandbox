from prometheus_client import (
    CollectorRegistry,
    Gauge,
    pushadd_to_gateway
)
import time

REGISTRY = CollectorRegistry()

# Prometheus Metrics
gauge = Gauge(
    'test_gauge',
    'Current state of an error machine',
    ['tenant', 'machine'], # labels
    registry=REGISTRY 
)

gauge.labels(tenant='cs', machine='some_machine').set(1)
pushadd_to_gateway('localhost:9091', job='monitor_etl', registry=REGISTRY)
