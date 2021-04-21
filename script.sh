#!/bin/sh
for i in 1000 
do
  netcat localhost 44444 < tiny.txt -w 1
  netcat localhost 44444 < small.txt -w 1
  netcat localhost 44444 < medium.txt -w 1
  netcat localhost 44444 < large.txt -w 1
  netcat localhost 44444 < xlarge.txt -w 1
done
