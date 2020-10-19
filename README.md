# YANG-GETTER

---
date: "2020-15-10"
tags: ["nornir", "YANG"]
---

### Dependencies

```
pip3 install nornir"<3"
pip3 install rich
pip3 install requests
```

### Overview
This script uses the Nornir framework (version 2!) to simplify the retrieval of device (Cisco IOS-XE) information over RESTCONF. 
Simply select a keyword and the ```yang_getter.py ``` script will translate the selection into the correct resource URL and send a HTTP GET request to the targeted devices.
Data will be returned in as a Python dictionary, in form of the Cisco IOS-XE Native YANG model

### How to Use
Simply run the script by typing ```python3 yang_getter.py``` and the script will execute. First a table will appear demonstrating all of the available keywords, after which you can simply type the keyword of the resource you would like to retrieve! Be aware, if you try to pull a resource that isn't configured on the device you will receive an error!
For example, if you use the "eigrp" keyword - EIGRP must be present on the device.


### DEVNET SANDBOX INFORMATION
This script has been designed on operate on the Cisco IOS-XE Always on Sandbox with 16.9.3 code.
The newer version of this code has a slightly different YANG implementation and will break the "ospf" and "eigrp" features, due to a container name-change!
You can find a list of Cisco XE sandboxes here: https://developer.cisco.com/docs/ios-xe/#!sandboxes/reservation-based-sandboxes


### DEMO
![alt text](https://github.com/IPvZero/YANG-GETTER/blob/main/images/yangpull2.png?raw=true)


![alt text](https://github.com/IPvZero/YANG-GETTER/blob/main/images/yangpull3.png?raw=true)


![alt text](https://github.com/IPvZero/YANG-GETTER/blob/main/images/yangpull4.png?raw=true)



### About Me
My name's John McGovern, I maintain a Youtube channel called IPvZero and I am trainer for CBT Nuggets. 
I create instructional videos on Python Network Automation.

### Contact

[Twitter](https://twitter.com/IPvZero)

[Youtube](https://youtube.com/c/IPvZero)

[LinkedIn](https://www.linkedin.com/in/ipvzero)

### CBT Nuggets 

[Advanced Network Automation with Cisco and Python](http://learn.gg/adv-net)

