from prometheus_client import start_http_server, Gauge
import psutil
import time
import os

cpu_core_usage = Gauge('metric_cpu_usage', 'CPU usage percentage per core', ['core'])
memory = Gauge('metric_memory', 'Memory metrics in megabytes', ['type'])
disk = Gauge('metric_disk', 'Disk space metrics in gigabytes', ['type'])

def collect_metrics():
    core_percentages = psutil.cpu_percent(percpu=True)
    for core, usage in enumerate(core_percentages):
        cpu_core_usage.labels(core=str(core)).set(usage)
    
    mem = psutil.virtual_memory()
    memory.labels(type="total").set(mem.total / (1024 * 1024))
    memory.labels(type="used").set(mem.used / (1024 * 1024))
    
    disk_usage = psutil.disk_usage('/')
    disk.labels(type="total").set(disk_usage.total / (1024 * 1024 * 1024))
    disk.labels(type="used").set(disk_usage.used / (1024 * 1024 * 1024))

if __name__ == "__main__":
    host = os.getenv("EXPORTER_HOST", "0.0.0.0")
    port = int(os.getenv("EXPORTER_PORT", 8000))
    start_http_server(port, addr=host)
    print(f"Exporter running on http://{host}:{port}")

    while True:
        collect_metrics()
        time.sleep(5)
