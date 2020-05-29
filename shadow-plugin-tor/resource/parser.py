import os
from os import walk
import datetime

INITIALIZATION_TIME = datetime.datetime.strptime('00:16:00', '%H:%M:%S').time() 

starting_time = 0
# TODO add arg parsing to take in whichever network as input
path_to_server = "shadow-minimal/shadow.data/hosts/fileserver/stdout-fileserver.tgen.1000.log" 
server_file = open(path_to_server, "r")
for line in server_file:
    if starting_time != 0:
        break
    if line.find(',streams-created') != -1:
        if line.find(',streams-created=0') == -1:  # Number of streams > 0
            split_line = line.split(' ')
            stream_time = datetime.datetime.strptime(split_line[1], '%H:%M:%S')
            if stream_time.time() > INITIALIZATION_TIME:
                starting_time = stream_time
                total = line.find('total-streams-created')
                print(line[total:total+25])

client_files = []
for root, dirs, files in os.walk("shadow-minimal/shadow.data/hosts"):
    for filename in files:
        if filename.find("client") != -1:
            client_files.append(root+"/"+filename)

stream_times = []
for client_file_name in client_files:
    client_file = open(client_file_name, "r")
    for line in client_file:
        if line.find(',streams-created') != -1:
            if line.find(',streams-created=0') == -1:  # Number of streams > 0
                split_line = line.split(' ')
                stream_times.append(split_line[1])
                # total = line.find('total-streams-created')
                # print(line[total:total+25])

print(starting_time, stream_times)
# TODO check which of these are within d time of starting time
