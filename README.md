# Seatalk1-Raspi-reader
A script to read SeaTalk1 from the Raspberry Pi GPIO using pigpio

You can read out the SeaTalk1 bus from old Raymarine devices using this script. The Script sends the sentences via
UDP to the listener (opencpn/SignalK and potentially others. These translate the sentences to NMEA0183 or similar.

## Hardware:
Preferably, use an MCS-board: Connect the yellow SeaTalk1 signal wire to one of the inputs (In1-In4).
You can also use the Openplotter-MCS app, which includes this script:
https://www.gedad.de/shop/gecos-wired/#cc-m-product-15562399022  
https://www.gedad.de/2019/12/27/gedad-marine-control-server/  


If you want to use your own hardware, connect the yellow SeaTalk1 wire via an optocoupler to any GPIO. 
The GPIO number in the script must be edited to match the GPIO port number used!

Example:

![](
https://github.com/Thomas-GeDaD/Seatalk1-Raspi-reader/blob/master/connections.png)

## Software
The Software uses pigpio for bitbanging 9-bit mode. Thus, you have to enable pigpio:

### Installing pigpio:
Usually, pigpio is already installed on your Raspberry Pi. Else:  
<code>sudo apt-get install pigpio</code> 

To start pigpio:  
<code>sudo pigpiod</code>   

To enable pigpio by default:  
<code>sudo systemctl enable pigpiod</code>   


### Using the script:  
Download STALK_read.py   
<code>git clone https://github.com/Thomas-GeDaD/Seatalk1-Raspi-reader</code>  
On top of the script, edit the GPIO, Port, and IP to match your setup. 
 
Then start the script:  
<code>sudo python /home/pi//Seatalk1-Raspi-reader/STALK_read.py</code> 



## Checking the UDP datastream
To check if UDP sends correctly, check in another terminal:  
<code>nc -ulkw 0 ipaddress port</code>  
    
    
## General:
If you need help or want changes let me know ...  
(tested with Raspberry Pi 3/4B and pigpio version V1.71)
