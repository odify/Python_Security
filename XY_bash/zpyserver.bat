#!/bin/bash


if [ $# -eq 0 ]; then PORT=8000; else PORT=$1; fi; python -c 'import socket; print "^[[92mhttp://" + str( socket.gethostbyname( socket.gethostname() ) ) + ":'$PORT'^[[0;0m";'; python -m SimpleHTTPServer $PORT;


