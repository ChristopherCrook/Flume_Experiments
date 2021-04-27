#!/bin/sh
i=0
output_file="tiny_out.txt"
Line="THIS IS A TEST MESSAGE"

while [ $i -lt 1000 ]
do
  
  echo $Line >> "$output_file"
  i=$((i+1))
  echo $Line
done

netcat localhost 44444 < tiny_out.txt -w 1 | ts '[%.s]' >> tiny_results.txt
