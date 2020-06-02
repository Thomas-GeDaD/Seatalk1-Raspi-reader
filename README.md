# Seatalk1-Raspi-reader
a script to read seatalk1 from the raspi GPIO using pigpio

You can read the Seatalk1 bus from old Raymarine devices with this scrip. The Script sends the sentences via
UDP to the listener (opencpn/SignalK and further more. There the sentences are translated to NMEA0183 or simular.

## Hardware:
First of all you can use our MCS-board. Connect the Yellow signal Seatalk wire to one of the Inputs (In1-In4)
You can also use the Openplotter-MCS app where this script is includet.:
https://www.gedad.de/shop/gecos-wired/#cc-m-product-15562399022  
https://www.gedad.de/2019/12/27/gedad-marine-control-server/  


If you want to use your own hardware, connect the yellow seatalk wire via an optocoupler to any GPIO. 
The Gpio number in the script must edit and match to the connected GPIO!

Excample:

![](
https://github.com/Thomas-GeDaD/Seatalk1-Raspi-reader/blob/master/connections.png)

## Software
The Software uses pigpio for bitbanging 9bit mode. For using you must enable pigpio

### For install pigpio:
Normaly Pigpio is already installed on your Pi. Else:  
<code>sudo apt-get install pigpio</code> 

For start pgpio:  
<code>sudo pigpiod</code>   

For enable Pigpio by default:  
<code>sudo systemctl enable pigpiod  </code>   


### For the script:  
Download the STALK_read.py.   
<code>git clone https://github.com/Thomas-GeDaD/Seatalk1-Raspi-reader</code>  
On the Head of the script you can edit the GPIO, Port and IP. 
 
Then start the script:  
<code>sudo python /home/pi//Seatalk1-Raspi-reader/STALK_read.py</code> 



## Check UDP datastrem
If the UDP sends correctly you can check in another Terminal with:  
<code>nc -ulkw 0 ipaddress port</code>  
    
    
## General:

If you need help or want changes let me know...  
(tested with Pi3 /4B and pigpio Version V1.71)
