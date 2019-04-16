#!/usr/bin/env python3
import socket as s;z=s.socket(s.AF_INET,s.SOCK_STREAM);z.connect(('',1));z.send(b'!');d=z.recv(8);print(d)