# Seatalk1-Raspi-reader
a script to read seatalk1 from the raspi GPIO using pigpio

You can read the Seatalk1 bus from old Raymarine devices with this scrip. The Script sends the sentences via
UDP to the listener (opencpn/SignalK and further more. There the sentences are translated to NMEA0183 or simular.

### Hardware:
First of all you can use our MCS-board. Connect the Yellow signal Seatalk wire to one of the Inputs (In1-In4)
You can also use the Openplotter-MCS app where this script is includet.

If you want to use your own hardware, connect the yellow seatlak wire via an optocoupler to any GPIO. 
The Gpio number in the script must edit and match to the connected GPIO!

Excample:


