import os

import psutil

total_cpu_usage=psutil.cpu_percent(interval=1)
print(f"Total CPU USAGE: {total_cpu_usage}%")

physical_cores=psutil.cpu_count(logical=False)
print(f"Number of physical cores: {physical_cores}")

logical_cores=psutil.cpu_count(logical=True)
print(f"Number of logical cores: {logical_cores}")

current_process = psutil.Process()
os_thread_count = current_process.num_threads()

print(f"Total OS-level threads: {os_thread_count}")