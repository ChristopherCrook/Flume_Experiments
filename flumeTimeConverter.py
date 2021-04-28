from datetime import datetime
import re

py_ts = []
fl_ts = []
delta = []

epoch = datetime.utcfromtimestamp(0)
gmt_conv = 18000 #seconds

#REMOVE THE ACK FROM END OF EACH TIMESTAMP SENT TO FLUME
remove_chars = "OK"
pattern = "[" + remove_chars + "]"

#py is output of python script, fl is flume log
py_file = open('tiny_results.txt','r')
fl_file = open('tiny_log.txt', 'r')

py_lines = py_file.readlines()
fl_lines = fl_file.readlines()

for line in py_lines:
    strip_line = re.sub(pattern,"",line).strip()[1:-1]
    py_ts.append(strip_line)

for line in fl_lines:
    if "SinkRunner-PollingRunner-DefaultSinkProcessor" in line:
        info_idx = line.index(" INFO")
        #NODATE - print("{}".format(line[info_idx - 13:info_idx]))
        dt = line[:info_idx]
        day, mon, year, time = dt.split(" ")
        hour, min, ms = time.split(":")
        sec, t_mil = ms.split(",")
        mil = int(t_mil)
        tmp_ts = day + ":" + mon + ":" + year + ":" + hour + ":" + min + ":" + sec + ":" + str(mil)
        ts_obj = datetime.strptime(tmp_ts, "%d:%b:%Y:%H:%M:%S:%f")
        flume_dt = (ts_obj - epoch).total_seconds() + gmt_conv
        fl_ts.append(flume_dt)


print("Check Lengths:  Py & Fl")
print(len(fl_ts))
print(len(py_ts))

maxlength = max(len(fl_ts), len(py_ts))

for i in range(1, maxlength):
    delta.append([py_ts[i], fl_ts[i], float(fl_ts[i]) - float(py_ts[i])])

print(delta)
print("done")
