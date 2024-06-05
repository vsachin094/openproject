import time
import requests
from prometheus_client import CollectorRegistry, Counter
from remote_pb2 import WriteRequest, TimeSeries, Sample

def push_metrics_directly():
    # Create a registry
    registry = CollectorRegistry()

    # Create a Counter metric with labels
    c = Counter('login_attempts', 'Login attempts by users', 
                ['user_id', 'status', 'method'], registry=registry)

    # Increment the counter for a specific user login attempt
    c.labels(user_id='12345', status='success', method='web').inc()

    # Collect the metrics
    metrics = registry.collect()

    # Prepare the payload for remote write
    payload = generate_payload(metrics)

    # Send the payload to Prometheus's remote write endpoint
    response = requests.post('http://localhost:9090/api/v1/write', data=payload, headers={'Content-Type': 'application/x-protobuf'})

    if response.status_code == 200:
        print("Metrics successfully pushed to Prometheus.")
    else:
        print(f"Failed to push metrics to Prometheus: {response.status_code}")

def generate_payload(metrics):
    write_request = WriteRequest()

    for metric_family in metrics:
        for sample in metric_family.samples:
            time_series = TimeSeries()

            # Set the labels
            for name, value in sample[0].items():
                label = time_series.labels.add()
                label.name = name
                label.value = value

            # Set the sample value and timestamp
            sample_value = Sample()
            sample_value.value = sample[2]
            sample_value.timestamp = int(sample[1] * 1000)  # Convert to milliseconds

            time_series.samples.append(sample_value)

            write_request.timeseries.append(time_series)

    return write_request.SerializeToString()

if __name__ == '__main__':
    while True:
        push_metrics_directly()
        time.sleep(60)  # Push every 60 seconds
