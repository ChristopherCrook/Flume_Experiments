#!/bin/sh
i=0
input_file="medium.txt"
output_file="medium_out.txt"
lastLine=""

while [ $i -lt 1000 ]
do
  while IFS= read -r line 
  do
    echo $line >> "$output_file"
    lastLine=$line
    i=$((i+1))
    echo $line
    if [ $i -ge 1000 ]
    then
      exit
    fi
  done
  echo $lastLine >> "$output_file"
  i=$((i+1))
  echo $lastLine
done < "$input_file"

netcat localhost 44444 < medium_out.txt -w 1 | ts '[%.s]' >> medium_results.txt
