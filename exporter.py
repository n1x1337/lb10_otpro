from prometheus_client import start_http_server, Gauge
import psutil
import time
import os

cpu_usage = Gauge('cpu_usage', 'CPU usage percentage')
memory_total = Gauge('memory_total', 'Total memory in bytes')
memory_used = Gauge('memory_used', 'Used memory in bytes')
disk_total = Gauge('disk_total', 'Total disk space in bytes')
disk_used = Gauge('disk_used', 'Used disk space in bytes')

def collect_metrics():
    cpu_usage.set(psutil.cpu_percent(interval=1))
    
    mem = psutil.virtual_memory()
    memory_total.set(mem.total)
    memory_used.set(mem.used)
    
    disk = psutil.disk_usage('/')
    disk_total.set(disk.total)
    disk_used.set(disk.used)

if __name__ == "__main__":
    host = os.getenv("EXPORTER_HOST", "0.0.0.0")
    port = int(os.getenv("EXPORTER_PORT", 8000))
    start_http_server(port, addr=host)
    print(f"Exporter running on http://{host}:{port}")

    while True:
        collect_metrics()
        time.sleep(5)
