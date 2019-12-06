import subprocess as run

def stop_kodi():
    run.Popen(["systemctl", "stop", "kodi"])

def restart_kodi():
    run.Popen(["systemctl", "try-restart", "kodi"])

def start_kodi():
    run.Popen(["systemctl", "restart", "kodi"])
    
def stop_hyperion():
    run.Popen(["systemctl", "stop", "hyperion"])

def restart_hyperion():
    run.Popen(["systemctl", "try-restart", "hyperion"])

def start_hyperion():
    run.Popen(["systemctl", "restart", "hyperion"])

def hyperion_interactive():
    run.Popen(["/usr/bin/hyperion-remote", "--clearall"])

def hyperion_sendcolor(color):
    run.Popen(["/usr/bin/hyperion-remote", "-c", color])

def reboot_rpi():
    run.Popen(["systemctl", "reboot"])

def poweroff_rpi():
    run.Popen(["systemctl", "poweroff"])
