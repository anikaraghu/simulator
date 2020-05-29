import os, argparse
from os import walk
import datetime

INITIALIZATION_TIME = datetime.datetime.strptime('00:16:00', '%H:%M:%S').time() 


ap = argparse.ArgumentParser(description='Analyze streams for connection tracking', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
ap.add_argument('experiment', action="store", type=str, help="path to experiment (e.g. 'shadow-minimal')", metavar='FOLDER', default=None)
args = ap.parse_args()
# print(args.experiment)

starting_time = 0
path_to_server = args.experiment + "/shadow.data/hosts/fileserver/stdout-fileserver.tgen.1000.log" 
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

# TODO: analyze for different values of d
stream_times = []
num_eliminated = 0
for client_file_name in client_files:
    client_file = open(client_file_name, "r")
    for line in client_file:
        if line.find(',streams-created') != -1:
            if line.find(',streams-created=0') == -1:  # Number of streams > 0
                split_line = line.split(' ')
                stream_time = datetime.datetime.strptime(split_line[1], '%H:%M:%S')
                stream_times.append(stream_time)
                # TODO
                # if stream_time < starting_time or stream_time > starting_time.time() + datetime.timedelta(0,1):
                    # num_eliminated += 1
                # total = line.find('total-streams-created')
                # print(line[total:total+25])

print("Time of first HTTP Response packet: " + starting_time)
print("Times of all streams " + stream_times)
#print("Streams eliminated = " + num_eliminated + " out of " + len(stream_times))
