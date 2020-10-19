"""
AUTHOR: IPvZero
DATE: 11th October 2020
NOTES: This script was written using Nornir2 - be aware, Nornir3 is the latest version.
You can install Nornir2 using the follow command:
pip3 install nornir"<3"


WARNING: There has been a change to the latest Cisco-IOXE NATIVE YANG model, 
in which the OSPF and EIGRP containers have changed names
to "router-ospf" and "router-eigrp", respectively.
This code was tested on the Cisco IOS-XE Always On Sandbox running version 16.9.3
"""

import logging
import os
import requests
from nornir import InitNornir
from nornir.plugins.tasks.apis import http_method
from nornir.plugins.functions.text import print_result
from rich import print as rprint
from rich.console import Console
from rich.table import Table

console = Console()
CLEAR = "clear"
os.system(CLEAR)

table = Table(
    title="KEYWORDS", show_header=True, show_lines=True, header_style="bold magenta"
)
table.add_column("running")

table.add_row(
    "[cyan]ip[/cyan]",
    "[red]domain[/red]",
    "[red]ssh[/red]",
    "[red]access-list[/red]",
    "[red]http[/red]",
    "[red]vrf[/red]",
    "[red]cef[/red]",
)

table.add_row(
    "[cyan]interface[/cyan]",
    "[red]GigabitEthernet[/red]",
    "[red]Loopback[/red]",
    "[red]Port-channel[/red]",
)

table.add_row(
    "[cyan]routing[/cyan]", "[red]ospf[/red]", "[red]eigrp[/red]", "[red]bgp[/red]"
)

table.add_row("[cyan]qos[/cyan]", "[red]class-map[/red]", "[red]policy-map[/red]")
table.add_row("[cyan]line[/cyan]", "[red]vty[/red]", "[red]console[/red]")
table.add_row("[cyan]key[/cyan]", "[red]keychain[/red]")

table.add_row("[cyan]crypto[/cyan]", "[red]pki[/red]")
table.add_row("[cyan]license[/cyan]", "[red]udi[/red]")
table.add_row(
    "[cyan]version[/cyan]",
)
table.add_row("[cyan]memory[/cyan]")

table.add_row("[cyan]vrf-definition[/cyan]")

table.add_row("[cyan]service[/cyan]")

table.add_row("[cyan]platform[/cyan]")

table.add_row("[cyan]hostname[/cyan]")

table.add_row("[cyan]username[/cyan]")

table.add_row("[cyan]route-map[/cyan]")

table.add_row("[cyan]login[/cyan]")

table.add_row("[cyan]multilink[/cyan]")

table.add_row("[cyan]spanning-tree[/cyan]")

table.add_row("[cyan]diagnostic[/cyan]")

table.add_row(
    "[red]pki[/red]", "[yellow]certificate[/yellow]", "[yellow]trustpoint[/yellow]"
)

table.add_row("[red]udi[/red]", "[yellow]pid[/yellow]", "[yellow]sn[/yellow]")

os.system(CLEAR)
console.print(table)
rprint("[green]Welcome to IPvZero's IOS-XE Native YANG Getter[/green]")
target = input("Enter the Keyword to wish to select: ")
if target == "routing":
    target = "router"
elif target in ("ospf", "eigrp", "bgp"):
    prefix = "router"
    target = f"{prefix}/{target}"
elif target in ("domain", "ssh", "access-list", "http", "vrf", "cef"):
    prefix = "ip"
    target = f"{prefix}/{target}"
elif target in ("GigabitEthernet", "Loopback", "Port-channel"):
    prefix = "interface"
    target = f"{prefix}/{target}"
elif target == "vrf-definition":
    target = "vrf"
elif target == "qos":
    target = "policy"
elif target in ("class-map", "policy-map"):
    prefix = "policy"
    target = f"{prefix}/{target}"
elif target == "running":
    target = ""
elif target == "keychain":
    prefix = "key"
    target = f"{prefix}/chain"
elif target == "pki":
    prefix = "crypto"
    target = f"{prefix}/{target}"
elif target in ("certificate", "trustpoint"):
    prefix = "crypto/pki"
    target = f"{prefix}/{target}"
elif target == "udi":
    prefix = "license"
    target = f"{prefix}/{target}"
elif target in ("pid", "sn"):
    prefix = "license/udi"
    target = f"{prefix}/{target}"
elif target in ("vty", "console"):
    prefix = "line"
    target = f"{prefix}/{target}"

nr = InitNornir(config_file="config.yaml")
requests.packages.urllib3.disable_warnings()

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}


def pullyang(task):
    send = task.run(
        http_method,
        severity_level=logging.DEBUG,
        verify=False,
        auth=("developer", "C1sco12345"),
        method="get",
        headers=headers,
        url=f"https://{task.host.hostname}:9443/restconf/data/native/{target}",
    )
    printer = send.response.json()
    rprint(printer)


result = nr.run(task=pullyang)
print_result(result)
