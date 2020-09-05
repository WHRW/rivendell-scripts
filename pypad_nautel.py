#!/usr/bin/python3

# CODE IS UNTESTED, IN DEVELOPMENT, DO NOT USE IN PRODUCTION

# pypad_nautel.py
#
# Send Now & Next updates to an Nautel FM Transmitter as TCP for RDS
#
#   (C) Copyright 2018 Fred Gleason <fredg@paravelsystems.com>
#                 2020 Eric Adler <eric@whrwfm.org>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License version 2 as
#   published by the Free Software Foundation.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public
#   License along with this program; if not, write to the Free Software
#   Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#

import sys
import socket
import configparser
import pypad
import time

def eprint(*args,**kwargs):
    print(*args,file=sys.stderr,**kwargs)


def sendvar(var):
    if(len(var)!=0):
        send_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        send_sock.connect((ipaddr,port))
        send_sock.sendall(var.encode('utf-8'))
        send_sock.close()

def getval(section, val):
    configval = update.config().get(section,val)
    return configval

def encode(srcdata, fieldname):
    if(len(srcdata)!=0):
        enc=fieldname+'='+update.resolvePadFields(srcdata),pypad.ESCAPE_NONE)+'\r\n'
    else
        enc=''
    return enc

def getval_encdode(sourcename, fieldname):
    return encode(getval(sourcename), fieldname)

def ProcessPad(update):
    n=1
    section='Rds'+str(n)
    while(update.config().has_section(section)):
        if update.shouldBeProcessed(section) and update.hasPadType(pypad.TYPE_NOW):
            dps=''
            dps=getval_encode('DynamicPS')
            ps=getval_encode('ProgramService')
            text=getval_encode('RadioText')
            picode=getval_encode('PICode')
            pty=getval_encode('ProgramType')
            ptyn=getval_encode('ProgramTypeName')
            trp=getval_encode('TrafficProgram')
            tra=getval_encode('TrafficAnnouncement')
            af1=getval_encode('AltFreq1')
            af2=getval_encode('AltFreq2')
            af3=getval_encode('AltFreq3')
            af4=getval_encode('AltFreq4')
            af5=getval_encode('AltFreq5')
            af6=getval_encode('AltFreq6')
            af7=getval_encode('AltFreq7')
            af8=getval_encode('AltFreq8')
            af9=getval_encode('AltFreq9')
            af10=getval_encode('AltFreq10')
            af11=getval_encode('AltFreq11')
            af12=getval_encode('AltFreq12')
            af13=getval_encode('AltFreq13')
            af14=getval_encode('AltFreq14')
            af15=getval_encode('AltFreq15')
            af16=getval_encode('AltFreq16')
            af17=getval_encode('AltFreq17')
            af18=getval_encode('AltFreq18')
            af19=getval_encode('AltFreq19')
            af20=getval_encode('AltFreq20')
            af21=getval_encode('AltFreq21')
            af22=getval_encode('AltFreq22')
            af23=getval_encode('AltFreq23')
            af24=getval_encode('AltFreq24')
            af25=getval_encode('AltFreq25')
            di=getval_encode('DecoderInfo')
            mus=getval_encode('MusicSpeech')
            dat=getval_encode('Date')
            tim=getval_encode('Time')
            utco=getval_encode('UTCOffset')
            cont=getval_encode('Cont')
            dpsr=getval_encode('DPSRate')
            dpsm=getval_encode('DPSMode')



            #
            # Use TCP output
            #
            waittime=int(update.config().get(section,'Delay'))
            time.sleep(waittime)
            ipaddr=update.config().get(section,'IpAddress')
            port=int(update.config().get(section,'TcpPort'))
            sendvar(dps)
            sendvar(ps)
            sendvar(text)
            
            sendvar(picode)
            sendvar(pty)
            sendvar(ptyn)
            sendvar(trp)
            sendvar(tra)
            sendvar(af1)
            sendvar(af2)
            sendvar(af3)
            sendvar(af4)
            sendvar(af5)
            sendvar(af6)
            sendvar(af7)
            sendvar(af8)
            sendvar(af9)
            sendvar(af10)
            sendvar(af11)
            sendvar(af12)
            sendvar(af13)
            sendvar(af14)
            sendvar(af15)
            sendvar(af16)
            sendvar(af17)
            sendvar(af18)
            sendvar(af19)
            sendvar(af20)
            sendvar(af21)
            sendvar(af22)
            sendvar(af23)
            sendvar(af24)
            sendvar(af25)
            sendvar(di)
            sendvar(mus)
            sendvar(dat)
            sendvar(tim)
            sendvar(utco)
            sendvar(cont)
            sendvar(dpsr)
            sendvar(dpsm)


        n=n+1
        section='Rds'+str(n)

#
# 'Main' function
#
# Create Send Socket
#

rcvr=pypad.Receiver()
try:
    rcvr.setConfigFile(sys.argv[3])
except IndexError:
    eprint('pypad_inno713.py: USAGE: cmd <hostname> <port> <config>')
    sys.exit(1)
rcvr.setPadCallback(ProcessPad)
rcvr.start(sys.argv[1],int(sys.argv[2]))
