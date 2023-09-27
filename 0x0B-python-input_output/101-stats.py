import sys
import signal

total_size = 0
status_counts = {}

def print_metrics():
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) >= 9:
            status_code = parts[-2]
            file_size = int(parts[-1])
            total_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1
        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    print_metrics()
    sys.exit(0)
