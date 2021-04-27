#!/bin/sh
i=0
output_file="small_out.txt"
Line="There are not more than five primary colors (blue, yellow, red, white, and black), yet in combination they produce more hues than can ever been seen."

while [ $i -lt 1000 ]
do
  
  echo $Line >> "$output_file"
  i=$((i+1))
  echo $Line
done

netcat localhost 44444 < small_out.txt -w 1 | ts '[%.s]' >> small_results.txt
