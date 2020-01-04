from subprocess import check_output
import psutil

# Iterate over all running process
for proc in psutil.process_iter():
    try:
        # Get process name & pid from process object.
        processName = proc.name()
        processID = proc.pid
        if "EscapeFromTarkov" in processName or 'calc' in processName:
            print(processName , ' ::: ', processID)            
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        print("Except:", proc)
