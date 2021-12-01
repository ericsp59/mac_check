from flask import Flask
import re
import time
from telnetlib import Telnet
import cryptocode
import os

app = Flask(__name__)
@app.route('/')

# def hello_world():
#     return 'Hello, Docker!'

# def check_ping():
#   hostname = "192.168.254.5"
#   response = os.system("ping -c 1 " + hostname)
#   print(response)
#   if response == 0:
#       pingstatus = "Network Active"
#   else:
#       pingstatus = "Network Error"
#   print(pingstatus)
#   return pingstatus        

# check_ping()

def get_mac():
  # f = open('./py_script/text.txt', 'r')
  f = open('text.txt', 'r')
  [h, k] = [line.strip() for line in f]

  user = 'admin'
  p = cryptocode.decrypt(h, k)  ### Пароль

  target_mac = ''

  def find_port_by_mac_zyxel(host, mac, sw_ports):
    
    if not (re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower().strip())):
      return('error format mac-address')
    else:
      # msg = ''
      mac = mac.strip()
      tn = Telnet(host.replace('\n', ''), 23, 30)
      tn.read_until(b':')
      tn.write((user + '\n').encode('ascii'))
      tn.read_until(b':')
      tn.write((p + '\n').encode('ascii'))
      tn.read_until(b'#')
      time.sleep(2)
      tn.write(('show mac address-table all' + '\n').encode('ascii'))
      mactable = (str(tn.read_until(b'#'))).split('\\r\\n')
      del mactable[0:2]
      mactable.pop(-1)
      mactable_list = [item.split() for item in mactable]

      for mactable_item in mactable_list:
        mac = mac.replace('-', ':')
        if mactable_item[2].replace(':', '') == mac.replace(':', ''):
          port = mactable_item[0]
          vid = mactable_item[1]
          if port not in sw_ports:
            msg += 'Switch: https://'+host+'\n'
            for mactable_item2 in mactable_list:
              if mactable_item2[0] == port:
                msg += 'PORT '+port+', MAC: '+mactable_item2[2]+', VLAN: '+mactable_item2[1]
                tn.close()
                print(msg)
                # return msg
          return [port, vid, mac, host, msg]
        tn.close()

          ##  # 0 - port
          ##  # 1 - VID
          ##  # 2 - mac
          ##  # 3 - type


  def find_port_by_mac_dlink(host, mac, sw_ports):
    if not (re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower().strip())):
      return('error format mac-address')
      time.sleep(5000)
    else:
      mac = mac.strip()
      tn = Telnet(host.replace('\n', ''), 23, 30)
      tn.read_until(b':')
      tn.write((user + '\n').encode('ascii'))
      tn.read_until(b':')
      tn.write((p + '\n').encode('ascii'))
      tn.read_until(b'#')
      # print(l)
      time.sleep(2)
      tn.write(('show fdb mac_address '+ mac + '\n').encode('ascii'))
      mactable = (str(tn.read_until(b'#'))).split('\\n\\r')
      del mactable[0:5]
      del mactable[2:-1]
      mactable.pop(-1)
      mactable_list = [item.split() for item in mactable]
      #
      for mactable_item in mactable_list:
        mac = mac.replace('-', ':')
        # print(mactable_item[2])
        # print(mac)
        if mactable_item[2].replace('-', '').lower() == mac.replace(':', ''):
          port = mactable_item[3]
          vid = mactable_item[0]
          print(f'device: {host}')
          print(f"PORT: {port}")
          print(f"VID: {vid}")
          print('***********************\n')
          if port not in sw_ports:
            # print('')
            # print(f'Host: {host}')
            for mactable_item2 in mactable_list:
              if mactable_item2 != []:
                if mactable_item2[3] == port :
                  print(f'PORT {port}: {mactable_item2[2]}, VLAN: {mactable_item2[0]}')
                  tn.close()
          return [port, vid, mac, host]
          print(123)

        tn.close()

        ##  # 0 - port
        ##  # 1 - VID
        ##  # 2 - mac
        ##  # 3 - type

  # while(True):
  # target_mac = input("Enter MAC: ")
  target_mac = '10:e7:c6:ec:86:8d'
  msg = ''
  if target_mac != '':
    if not (re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", target_mac.lower().strip())):
      return('error format mac-address')
      print('\n\n')
    else:
      target_mac = target_mac.lower()
      on_zyxel200 = find_port_by_mac_zyxel('192.168.254.200', target_mac, ['1', '2', '3', '4', '5', '11', '25', '26', '29', '30'])

      msg = "MAC: "+target_mac.strip() + "\n"
      msg += 'XGS4600: '+ on_zyxel200[3]+'\n'
      msg += 'Port: '+on_zyxel200[0]+'\n'
      msg += '-------------------\n'
      
      
      if on_zyxel200[0] == '1':
        msg += on_zyxel200[2] + '\n Web Interface Only --> http://192.168.254.5'
      
      if on_zyxel200[0] == '2':
        msg += on_zyxel200[2]+ '\n Web Interface Only --> http://192.168.254.6'
      
      if on_zyxel200[0] == '3':
        msg += on_zyxel200[2]+ '\n Web Interface Only --> http://192.168.254.7'
      
      if on_zyxel200[0] == '4':
        on_dlink21 = find_port_by_mac_dlink('192.168.254.21', target_mac, [])
      
      if on_zyxel200[0] == '5':
        msg += on_zyxel200[2]+ '\n Web Interface Only --> http://192.168.254.22/'
      ##################################################
      
      if on_zyxel200[0] == '11':
        msg += 'Check 254.8...\n'
        on_zyxel8 = find_port_by_mac_zyxel('192.168.254.8', target_mac, [])

      
      if on_zyxel200[0] == '25':
        msg += 'Check 254.35...\n'
        on_zyxel35 = find_port_by_mac_zyxel('192.168.254.35', target_mac, [])
      
      if on_zyxel200[0] == '26':
        msg += 'Check 254.46...\n'
        on_zyxel35 = find_port_by_mac_zyxel('192.168.254.46', target_mac, [])
      ###################################################
      if on_zyxel200[0] == '29':
        msg += 'Check 254.31...\n'
        on_zyxel31 = find_port_by_mac_zyxel('192.168.254.31', target_mac, ['27'])
        if on_zyxel31[0] == '27':
          msg += 'Check 254.32...\n'
          on_zyxel32 = find_port_by_mac_zyxel('192.168.254.32', target_mac, ['27'])
          if on_zyxel32[0] == '27':
            msg += 'Check 254.33...\n'
            on_zyxel33 = find_port_by_mac_zyxel('192.168.254.33', target_mac, ['27'])
            if on_zyxel33[0] == '27':
              msg += 'Check 254.34...\n'
              on_zyxel34 = find_port_by_mac_zyxel('192.168.254.34', target_mac, ['27'])
          else: return on_zyxel32[4]    
      
      if on_zyxel200[0] == '30':
        msg += 'Check 254.41...\n'
        on_zyxel41 = find_port_by_mac_zyxel('192.168.254.41', target_mac, ['27'])
        if on_zyxel41[0] == '27':
          msg += 'Check 254.42...\n'
          on_zyxel42 = find_port_by_mac_zyxel('192.168.254.42', target_mac, ['27'])
          if on_zyxel42[0] == '27':
            msg += 'Check 254.43...\n'
            on_zyxel43 = find_port_by_mac_zyxel('192.168.254.43', target_mac, ['27'])
            if on_zyxel43[0] == '27':
              msg += 'Check 254.44...\n'
              on_zyxel44 = find_port_by_mac_zyxel('192.168.254.44', target_mac, ['27'])
              if on_zyxel44[0] == '27':
                msg += 'Check 254.45...\n'
                on_zyxel45 = find_port_by_mac_zyxel('192.168.254.45', target_mac, [])

      msg += '\n######################################################\n'
      msg += '######################################################\n'
      msg += '######################################################\n\n\n'
      return msg
  ##############################################

# get_mac()