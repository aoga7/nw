#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import pprint
import datetime

from netaddr import *

path_hearing_sheet = '/etc/ansible/txt/hearing_sheet/hearing_sheet.csv'
path_ZoneDef1 = '/etc/ansible/txt/hearing_sheet/ZoneDef1.csv'
path_ZoneDef2 = '/etc/ansible/txt/hearing_sheet/ZoneDef2.csv'
path_Policy1= '/etc/ansible/txt/hearing_sheet/Policy1.csv'
path_Policy2= '/etc/ansible/txt/hearing_sheet/Policy2.csv'

with open(path_hearing_sheet)as f:
  reader = csv.reader(f,delimiter=';')
#  print(f.read())
  l = [row for row in reader]
print(l)
print(l[0])
print(l[0][0])

with open(path_ZoneDef1) as g:
  reader = csv.reader(g,delimiter=';')
  m = [row for row in reader]
print(m)
print(m[0])
print(m[0][0])

with open(path_ZoneDef2) as g2:
  reader = csv.reader(g2,delimiter=';')
  m2 = [row for row in reader]

print('--------------')



#ここに例外処理。レンジやサブネット指定や複数指定の行が全て同じzoneを指していることを示せればいい
#示せたら置換してしまうのもあり

with open(path_Policy1,'w') as h:
  h.write("Operation;RuleName;SrcZone;SrcAddress;DstZone;DstAddress;Application;Service;Action\n")
  for i in range(len(l)):
    print(l[i])
    for j in range(len(m)): # SrcZoneを探す
      print(m[j])
      if IPAddress(m[j][0]) <= IPAddress(l[i][1]) <= IPAddress(m[j][1]):
        print(m[j][2])
        SrcZone=m[j][2]
        break
    for j in range(len(m)): # DstZoneを探す
      print(m[j])
      if IPAddress(m[j][0]) <= IPAddress(l[i][2]) <= IPAddress(m[j][1]):
        print(m[j][2])
        DstZone=m[j][2]
        break
  h.write("Add;"+l[i][0]+";"+SrcZone+";"+l[i][1]+";"+DstZone+";"+l[i][2]+";"+l[i][3]+"-"+l[i][4]+";\n")
    

with open(path_Policy2,'w') as h2:
  h2.write("Operation;RuleName;SrcZone;SrcAddress;DstZone;DstAddress;Application;Service;Action\n")
  for i in range(len(l)):
    print(l[i])
    for j in range(len(m2)): # SrcZoneを探す
      print(m2[j])
      if IPAddress(m2[j][0]) <= IPAddress(l[i][1]) <= IPAddress(m2[j][1]):
        print(m2[j][2])
        SrcZone=m2[j][2]
        break
    for j in range(len(m2)): # DstZoneを探す
      print(m2[j])
      if IPAddress(m2[j][0]) <= IPAddress(l[i][2]) <= IPAddress(m2[j][1]):
        print(m2[j][2])
        DstZone=m2[j][2]
        break
  h2.write("Add;"+l[i][0]+";"+SrcZone+";"+l[i][1]+";"+DstZone+";"+l[i][2]+";"+l[i][3]+"-"+l[i][4]+";\n")

now = datetime.datetime.now()
#path = ('/etc/ansible/vars/panobjects_{0:%Y%m%d}.yml'.format(now))
#print(path)
#with open(path,'w') as g:
#  g.write("---\npanobjects:\n")
#  for i in range(len(l)):
#    print(l[i])
#    g.write("  - name: '" + l[i][0] + "'\n    value: '" + l[i][1] + "'\n")


#with open('/etc/ansible/playbook/vars/panobjects')

# ファイル読み込んだり、書き込んだり
#f = open("/etc/ansible/txt/acl_sample.txt","r")
#with open("/etc/ansible/playbook/ios_acl.yml","w") as g:
#  g.write("- hosts: Cisco\n  gather_facts: yes\n\n  tasks:\n   - name: ACLSetting\n     ios_config:\n       lines:\n")

#読み込んだデータを表示
#for line in f:
#  print(line)

#line = f.readline()

#while line:
#  # print(line) 101,permit,tcp,192.168.2.1,0.0.0.255,192.168.3.1,0.0.0.255,23
#  oneline = line.split(",")
#  # print(oneline) ['101', 'permit', 'tcp', '192.168.2.1', '0.0.0.255', '192.168.3.1', '0.0.0.255', '23\n']
#  acl = "         - access-list"
#  print(acl)
#  for oneword in oneline:
#    acl = acl + " " + oneword
#  print(acl)  
#  with open("/etc/ansible/playbook/ios_acl.yml","a") as g:
#    g.write(acl) 
#     
#  line = f.readline()
#
#f.close()

