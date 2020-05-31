import os, argparse
from os import walk
import datetime

INITIALIZATION_TIME = 1000

ap = argparse.ArgumentParser(description='Analyze streams for connection tracking', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
ap.add_argument('experiment', action="store", type=str, help="path to experiment (e.g. 'shadow-minimal')", metavar='FOLDER', default=None)
args = ap.parse_args()

path_to_client = args.experiment + "/shadow.data/hosts/client/stdout-client.tgen.1000.log" 
server_file = open(path_to_client, "r")
first_line = server_file.readline()
start = round(float(first_line.split(' ')[2]), 2)
print("start of experiment", start)


start_tracking = 0
path_to_server = args.experiment + "/shadow.data/hosts/fileserver/stdout-fileserver.tgen.1000.log" 
server_file = open(path_to_server, "r")

# get time of first http response
for line in server_file:
    if start_tracking != 0:
        break
    if line.find(',streams-created') != -1:
        if line.find(',streams-created=0') == -1:  # Number of streams > 0
            stream_time = round(float(line.split(' ')[2]) - start, 2)
            # print("stream time", stream_time + start)
            if stream_time >  INITIALIZATION_TIME:
                start_tracking = stream_time
                # total = line.find('total-streams-created')
                # print(line[total:total+25])
                print("relative start time ", start_tracking)

# get all client log files
client_files = []
for root, dirs, files in os.walk("shadow-minimal/shadow.data/hosts"):
    for filename in files:
        if filename.find("client") != -1:
            client_files.append(root+"/"+filename)

def stream_analysis():
    stream_times = []
    for client_file_name in client_files:
        client_file = open(client_file_name, "r")
        for line in client_file:
            if line.find(',streams-created') != -1:
                if line.find(',streams-created=0') == -1:  # Number of streams > 0
                    stream_time = round(float(line.split(' ')[2]) - start, 2)
                    stream_times.append(stream_time)
    return stream_times

def percent_eliminated(streams, d):
    num_eliminated = 0
    for stream in streams:
        if stream < start_tracking or stream > start_tracking + d:
            num_eliminated += 1
    print(num_eliminated)
    return float(num_eliminated)/len(streams)


f = open("logging.txt", "w")
f.write(args.experiment + "\n")

streams = stream_analysis()
# for stream in streams
f.write(str(streams) + "\n")

# TODO write this out to a file with a specific example 
ds = [0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
for d in ds:
    eliminated = percent_eliminated(streams, d)
    f.write(str(d) + " " + str(eliminated) + "\n")

f.close()
