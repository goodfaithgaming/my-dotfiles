 #!/usr/bin/python3

import subprocess, re

def signal_strength():
    output = subprocess.run(["nmcli", "-f", "IN-USE,SIGNAL,SSID", "device", "wifi"], capture_output=True, text=True, check=True).stdout
    regex = re.findall(r"\n\*(?: )+([0-9]+)(?: )+(.*?)(?: *)\n", output, flags=0)
    matches = []
    #for match in regex:
    #    matches.append((match[1],match[2]))
    return regex

def get_connections():
   output = subprocess.run(["nmcli", "-f", "UUID,TYPE,NAME", "c", "show", "--active"], capture_output=True, text=True, check=True).stdout
   regex = re.findall(r"\n([0-9a-f\-]+)(?: )+([a-zA-Z]+)(?: )+(.*?)(?: *)\n", output, flags=0)
   return regex

strengths = signal_strength()
connections = get_connections()
wifi = ["󰤮", "󰤯", "󰤟", "󰤢", "󰤥", "󰤨"]
cell = ["󰢿", "󰢼", "󰢽", "󰢾"]
net  = ["󰣽", "󰣾", "󰣴", "󰣶", "󰣸", "󰣺"]
tether = ["󰂯"]
hotspot = ["󰀂"]
link = ["󰒎", "󰒍"]

icons = wifi

if len(strengths) == 0:
    output = "  (0%) " + icons[0] + "  "
else:
    output = "  " + strengths[0][1]
    output += " (" + strengths[0][0] + "%) "
    output += icons[int(((len(icons)-2)*int(strengths[0][0]))/100)+1] + "  "
real_output = '{"text": "' + output + '","tooltip": "\\n' + output + '"}'
print(real_output)
