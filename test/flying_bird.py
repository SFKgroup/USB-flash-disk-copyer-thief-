import os
import numpy as np

class flight(object):
    def __init__(self,file_name):
        self.name = file_name
        self.end  = []
        self.limit = True
        self.wide = 360
        self.deep = 360
        self.location = []
    def build_file(self):
        try:
            os.mkdir('./' + self.name)
            os.mkdir('./' + self.name + '/动作组')
        except:
            if self.limit:
                raise Exception("This file has been built", self.name)
        grand = open('./' + self.name + '/' + self.name + '.fii','w',encoding="utf-8")
        grand.write('''<?xml version="1.0" encoding="utf-8"?>
        <GoertekGraphicXml>
        <DeviceType DeviceType="F400" />\n''')
        grand.close()
        grand = open('./' + self.name + '/动作组/checksums.xml','w',encoding="utf-8")
        grand.write('''<?xml version="1.0" encoding="utf-8"?>
        <CheckSumXml>\n''')
        grand.close()
    def new_action(self,x,y,ips,num):
        self.location.append((x,y,0,0))
        if self.location[int(num)-1] != (x,y,0,0):
            raise Exception("Flights should be named one by one", str(num))
        if (x > self.wide or y > self.deep or x < 0 or y < 0) and self.limit:
            raise Exception("Out of the map", str(x)+ ',' +str(y))
        ip = ips.split('.')
        try:
            os.mkdir('./' + self.name + '/动作组' + '/动作组' + str(num))
        except:
            if self.limit:
                raise Exception("This action has been built",'./' + self.name + '/动作组' + '/动作组' + str(num))
            else:
                pass

        check = open('./' + self.name + '/动作组/checksums.xml','a',encoding="utf-8")
        fii = open('./' + self.name + '/' + self.name + '.fii','a',encoding="utf-8")
        check.write('  <CheckSums flightchecksum="动作组' + str(num) + '无人机' + str(num) + 'UAVID' + str(ip[2]) + '0' + str(ip[3]) + 'CheckSum0" />\n')
        if num == 1:
            fii.write('''  <Actions actionname="动作组1" />
    <AreaL AreaL="400" />
    <AreaW AreaW="400" />
    <AreaH AreaH="300" />
    <动作组1Controls time="0" />
    <ActionFlight actionfname="动作组''' + str(num) + '''无人机''' + str(num) + '''" />
    <ActionFlightID actionfid="动作组''' + str(num) + '''无人机''' + str(num) + '''UAVID''' + str(ip[2]) + '0' + str(ip[3]) + '''" />
    <ActionFlightPosX actionfX="动作组''' + str(num) + '''无人机''' + str(num) + '''pos''' + str(x) + '''" />
    <ActionFlightPosY actionfY="动作组''' + str(num) + '''无人机''' + str(num) + '''pos''' + str(y) + '''" />
    <ActionFlightPosZ actionfZ="动作组''' + str(num) + '''无人机''' + str(num) + '''pos0" />\n''')
        else:
            fii.write('''  <Actions actionname="动作组''' + str(num) + '''" />
    <动作组''' + str(num) + '''Controls time="0" />
    <ActionFlight actionfname="动作组''' + str(num) + '''无人机''' + str(num) + '''" />
    <ActionFlightID actionfid="动作组''' + str(num) + '''无人机''' + str(num) + '''UAVID''' + str(ip[2]) + '0' + str(ip[3]) + '''" />
    <ActionFlightPosX actionfX="动作组''' + str(num) + '''无人机''' + str(num) + '''pos''' + str(x) + '''" />
    <ActionFlightPosY actionfY="动作组''' + str(num) + '''无人机''' + str(num) + '''pos''' + str(y) + '''" />
    <ActionFlightPosZ actionfZ="动作组''' + str(num) + '''无人机''' + str(num) + '''pos0" />\n''')
        check.close()
        fii.close()
        grand = open('./' + self.name + '/动作组/动作组' + str(num) + '/webCodeAll.xml','w',encoding="utf-8")
        grand.write('''<xml xmlns="http://www.w3.org/1999/xhtml">
    <variables></variables>
    <block type="Goertek_Start" x="-400" y="0">\n''')
        grand.close()
    def batch_new_action(self,ipstart,nums,x = 0,y = 0,direction = 'right'):
        if nums == 1 and self.limit:
            print("\033[1;33m [WARN]:You'd better use new_action instead of batch_new_action.\033[0m")
        if direction == 'toward':
            for a in range(nums):
                self.new_action(x,y+80*a,ipstart[:-2] + str(int(ipstart[-2:])+a),a+1)
        elif direction == 'back':
            for a in range(nums):
                self.new_action(x,y-80*a,ipstart[:-2] + str(int(ipstart[-2:])+a),a+1)
        elif direction == 'left':
            for a in range(nums):
                self.new_action(x-80*a,y,ipstart[:-2] + str(int(ipstart[-2:])+a),a+1)
        elif direction == 'right':
            for a in range(nums):
                self.new_action(x+80*a,y,ipstart[:-2] + str(int(ipstart[-2:])+a),a+1)
    def close_file(self):
        grand = open('./' + self.name + '/' + self.name + '.fii','a',encoding="utf-8")
        grand.write('''</GoertekGraphicXml>''')
        grand.close()
        grand = open('./' + self.name + '/动作组/checksums.xml','a',encoding="utf-8")
        grand.write('''</CheckSumXml>''')
        grand.close()
    def takeoff(self,num,time,h):
        if (h > 250 or h < 80) and self.limit:
            raise Exception("Out of the map", str(h))
        self.location[int(num)-1] = (self.location[int(num)-1][0],self.location[int(num)-1][1],h,self.location[int(num)-1][3])
        grand = open('./' + self.name + '/动作组/动作组' + str(num) + '/webCodeAll.xml','a',encoding="utf-8")
        grand.write('''<next>
        <block type="block_inittime">
            <field name="time">''' + time + '''</field>
            <field name="color">#cccccc</field>
            <statement name="functionIntit">
            <block type="Goertek_UnLock">
                <next>
                <block type="block_delay">
                    <field name="delay">0</field>
                    <field name="time">1000</field>
                    <next>
                    <block type="Goertek_TakeOff">
                        <field name="alt">''' + str(h) + '''</field>
                        <next>
                        <block type="block_delay">
                            <field name="delay">0</field>
                            <field name="time">3000</field>\n''')
        grand.close()
        self.end.insert(0,'</block>\n</next>\n</block>\n</next>\n</block>\n</next>\n</block>\n</statement>\n</block>\n</next>\n</block>')
    def sleep(self,num,t):
        grand = open('./' + self.name + '/动作组/动作组' + str(num) + '/webCodeAll.xml','a',encoding="utf-8")
        grand.write('''<next>
            <block type="block_delay">
            <field name="delay">0</field>
            <field name="time">''' + str(t) +'''</field>\n''')
        grand.close()
        self.end.insert(0,'</block>\n</next>')
    def go(self,num,x,y,z,t):
        if (x > self.wide or y > self.deep or z > 250 or z < 80 or x < 0 or y < 0) and self.limit:
            raise Exception("Out of the map", str(x) + ',' + str(y) + ',' + str(z))
        self.location[int(num)-1] = (self.location[int(num)-1][0]+x,self.location[int(num)-1][1]+y,self.location[int(num)-1][2]+z,self.location[int(num)-1][3])
        grand = open('./' + self.name + '/动作组/动作组' + str(num) + '/webCodeAll.xml','a',encoding="utf-8")
        grand.write('''<next>\n<block type="Goertek_Move">
            <field name="X">''' + str(x) + '''</field>
            <field name="Y">''' + str(y) + '''</field>
            <field name="Z">''' + str(z) + '''</field>
            <next>
            <block type="block_delay">
            <field name="delay">0</field>
            <field name="time">''' + str(t) +'''</field>\n''')
        grand.close()
        self.end.insert(0,'</block>\n</next>\n</block>\n</next>')
    def goto(self,num,x,y,z,t):
        if (x > self.wide or y > self.deep or z > 250 or z < 80 or x < 0 or y < 0) and self.limit:
            raise Exception("Out of the map", str(x) + ',' + str(y) + ',' + str(z))
        self.location[int(num)-1] = (x,y,z,self.location[int(num)-1][3])
        grand = open('./' + self.name + '/动作组/动作组' + str(num) + '/webCodeAll.xml','a',encoding="utf-8")
        grand.write('''<next>\n<block type="Goertek_MoveToCoord">
            <field name="X">''' + str(x) + '''</field>
            <field name="Y">''' + str(y) + '''</field>
            <field name="Z">''' + str(z) + '''</field>
            <next>
            <block type="block_delay">
            <field name="delay">0</field>
            <field name="time">''' + str(t) +'''</field>\n''')
        grand.close()
        self.end.insert(0,'</block>\n</next>\n</block>\n</next>')
    def close_action(self,num):
        grand = open('./' + self.name + '/动作组/动作组' + str(num) + '/webCodeAll.xml','a',encoding="utf-8")
        grand.write('<next>\n<block type="Goertek_Land"></block>\n</next>')
        for i in self.end:
            grand.write(i + '\n')
        grand.write('''  <block type="Goertek_Start" x="100" y="20"></block>\n</xml>''')
        grand.close()
    def horizontal_speed(self,num,sp,ap):
        if (sp < 20 or sp > 200 or ap < 50 or ap > 400) and self.limit:
            raise Exception("Unmanageable speed", str(sp) + ',' + str(ap))
        grand = open('./' + self.name + '/动作组/动作组' + str(num) + '/webCodeAll.xml','a',encoding="utf-8")
        grand.write('''<next>
        <block type="Goertek_HorizontalSpeed">
        <field name="VH">''' + str(sp) + '''</field>
        <field name="AH">''' + str(ap) + '''</field>\n''')
        grand.close()
        self.end.insert(0,'</block>\n</next>')
    def vertical_speed(self,num,sp,ap):
        if (sp < 60 or sp > 200 or ap < 50 or ap > 400) and self.limit:
            raise Exception("Unmanageable speed", str(sp) + ',' + str(ap))
        grand = open('./' + self.name + '/动作组/动作组' + str(num) + '/webCodeAll.xml','a',encoding="utf-8")
        grand.write('''<next>
        <block type="Goertek_VerticalSpeed">
        <field name="VV">''' + str(sp) + '''</field>
        <field name="AV">''' + str(ap) + '''</field>\n''')
        grand.close()
        self.end.insert(0,'</block>\n</next>')
    def deg_speed(self,num,sp):
        if (sp < 5 or sp > 60) and self.limit:
            raise Exception("Unmanageable speed", str(sp) + ',' + str(ap))
        grand = open('./' + self.name + '/动作组/动作组' + str(num) + '/webCodeAll.xml','a',encoding="utf-8")
        grand.write('''<next>
              <block type="Goertek_AngularVelocity">
                <field name="w">''' + str(sp) + '''</field>''')
        grand.close()
        self.end.insert(0,'</block>\n</next>')
    def led_colour(self,num,cl,t = 0):
        colour = []
        color = ''
        if type(cl) == type(()):
            for a in cl:
                if (int(a) > 255 or int(a) < 0) and self.limit:
                    raise Exception("Colour must between 0-255", str(cl))
                c = str(hex(int(a)))[2:]
                if len(c) == 1:
                    c = '0' + c
                color = color + c
            for i in range(12):
                colour.append(color)
        else:
            for a in cl:
                if (int(a[0]) > 255 or int(a[0]) < 0 or int(a[1]) > 255 or int(a[1]) < 0 or int(a[2]) > 255 or int(a[2]) < 0) and self.limit:
                    raise Exception("Colour must between 0-255", str(cl))
                R = str(hex(int(a[0])))[2:]
                G = str(hex(int(a[1])))[2:]
                B = str(hex(int(a[2])))[2:]
                if len(R) == 1:
                    R = '0' + R
                if len(G) == 1:
                    G = '0' + G
                if len(B) == 1:
                    B = '0' + B
                colour.append(R + G + B)
            if len(colour) < 12:
                for b in range(12-len(colour)):
                    color.append('000000')
        grand = open('./' + self.name + '/动作组/动作组' + str(num) + '/webCodeAll.xml','a',encoding="utf-8")
        grand.write('''<next>
          <block type="Goertek_LEDTurnOnAll">
            <field name="color1">#''' + str(colour[0]) + '''</field>
            <field name="color2">#''' + str(colour[1]) + '''</field>
            <field name="color3">#''' + str(colour[2]) + '''</field>
            <field name="color4">#''' + str(colour[3]) + '''</field>
            <field name="color5">#''' + str(colour[4]) + '''</field>
            <field name="color6">#''' + str(colour[5]) + '''</field>
            <field name="color7">#''' + str(colour[6]) + '''</field>
            <field name="color8">#''' + str(colour[7]) + '''</field>
            <field name="color9">#''' + str(colour[8]) + '''</field>
            <field name="color10">#''' + str(colour[9]) + '''</field>
            <field name="color11">#''' + str(colour[10]) + '''</field>
            <field name="color12">#''' + str(colour[11]) + '''</field>\n''')
        if t != 0:
            grand.write('''<next>
            <block type="block_delay">
            <field name="delay">0</field>
            <field name="time">''' + str(t) +'''</field>\n''')
            self.end.insert(0,'</block>\n</next>')
        grand.close()
        self.end.insert(0,'</block>\n</next>')
    def turnto(self,num,deg,t):
        #left<0,right>0
        if (deg > 359 or deg < -359) and self.limit:
            raise Exception("Unmanageable degree", str(deg))
        self.location[int(num)-1] = (self.location[int(num)-1][0],self.location[int(num)-1][1],self.location[int(num)-1][2],deg)
        if deg < 0 :
            deg = -1 * deg
            fc = 'l'
        else:
            fc = 'r'
        grand = open('./' + self.name + '/动作组/动作组' + str(num) + '/webCodeAll.xml','a',encoding="utf-8")
        grand.write('''<next>
          <block type="Goertek_TurnTo">
            <field name="turnDirection">''' + fc + '''</field>
            <field name="angle">''' + str(deg) + '''</field>
            <next>
            <block type="block_delay">
            <field name="delay">0</field>
            <field name="time">''' + str(t) +'''</field>\n''')
        grand.close()
        self.end.insert(0,'</block>\n</next>\n</block>\n</next>')
    def turn(self,num,deg,t):
        #left<0,right>0
        if (deg > 360 or deg < -360) and self.limit:
            raise Exception("Unmanageable degree", str(deg))
        self.location[int(num)-1] = (self.location[int(num)-1][0],self.location[int(num)-1][1],self.location[int(num)-1][2],self.location[int(num)-1][3]+deg)
        if deg < 0 :
            deg = -1 * deg
            fc = 'l'
        else:
            fc = 'r'
        grand = open('./' + self.name + '/动作组/动作组' + str(num) + '/webCodeAll.xml','a',encoding="utf-8")
        grand.write('''<next>
          <block type="Goertek_Turn">
            <field name="turnDirection">''' + fc + '''</field>
            <field name="angle">''' + str(deg) + '''</field>
            <next>
            <block type="block_delay">
            <field name="delay">0</field>
            <field name="time">''' + str(t) +'''</field>\n''')
        grand.close()
        self.end.insert(0,'</block>\n</next>\n</block>\n</next>')