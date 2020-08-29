
# Copyright (C) 2020 by GeDaD <https://github.com/Thomas-GeDaD/openplotter-MCS>
# you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# any later version.
# You should have received a copy of the GNU General Public License.
# If not, see <http://www.gnu.org/licenses/>.

import pigpio, time, socket, signal, sys

port=4041 #define udp port for sending
ip= '127.0.0.1' #define ip default localhost 127.0.0.1
gpio= 19 #define gpio where the seatalk1 (yellow wire) is connected

if __name__ == '__main__':
    st1read =pigpio.pi()
    try:
        st1read.bb_serial_read_close(gpio) #close if already run
    except:
        pass
    st1read.bb_serial_read_open(gpio, 4800,9)
    data=""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        while True:
            out=(st1read.bb_serial_read(gpio))
            out0=out[0]
            if out0>0:
                out_data=out[1]
                x=0
                while x < out0:
                    if out_data[x+1] ==0:
                        string1=str(hex(out_data[x]))
                        data1=str(string1[2:])
                        if (len(data1)==1):
                            data1="0"+data1
                        data= data+data1+ ","
                    else:
                        data=data[0:-1]
                        data="$STALK,"+data+"\r\n"
                        print(data)
                        sock.sendto(data.encode('utf-8'), (ip, port))
                        string2=str(hex(out_data[x]))
                        string2_new=string2[2:]
                        if len(string2_new)==1:
                            string2_new="0"+string2_new
                        data=string2_new + ","
                    x+=2
                
    except KeyboardInterrupt:
        st1read.bb_serial_read_close(gpio)
        print ("exit")



