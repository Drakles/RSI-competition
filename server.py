#!/usr/bin/env python3
import socket as s
z = s.socket(s.AF_INET,s.SOCK_STREAM)
z.bind(('',1))
z.listen()
while 1:
    c, a = z.accept()
    d = c.recv(1)
    print(d)
    c.send(d)