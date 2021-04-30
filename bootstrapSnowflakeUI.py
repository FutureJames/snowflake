import subprocess
try:
    cmd = "ps -t | grep homescreen.py | grep -v grep"
    pid = subprocess.check_output(cmd, shell=True)
    pid = pid.split(" ")
    # print(pid[1])
    pidnumber = pid[1]
    pidname = pid[len(pid)-1]
    # nb = len(pid)
    # print(nb)
    # print(pid[nb-1])
    print(pidnumber + " => " + pidname)
    cmd = "kill " + pidnumber + " &"
    exe = subprocess.check_output(cmd, shell=True)
    cmd = "python /root/snowflake/homescreen.py &"
    exe = subprocess.check_output(cmd, shell=True)
    exit()
except Exception:
    print("no pid")
    cmd = "python /root/snowflake/homescreen.py &"
    exe = subprocess.check_output(cmd, shell=True)
    exit()
