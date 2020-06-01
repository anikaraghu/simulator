import matplotlib.pyplot as plt
import argparse
import os
from os import walk

ap = argparse.ArgumentParser(description='Plotting results', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
ap.add_argument('inputfolder', action="store", type=str, help="path to folder for input files", metavar='FOLDER', default=None)
ap.add_argument('outputfilename', action="store", type=str, help="name of file for graphed output", metavar='FOLDER', default=None)
args = ap.parse_args()

fig = plt.figure()
input_files = [] 
for root, dirs, files in os.walk(args.inputfolder):
    print(root, dirs, files)
    for f in files:
        print(f)
        input_files.append(root + f)
print(input_files)

ds = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2.0]
for f in input_files:
    curr_file = open(f, 'r')
    percentages = []
    for line in curr_file:
        percentages.append(float(line))
    # for markers: 'o', markersize = 2, . different dashes: '-', '--', '-.' ':'
    graph_label = f[:f.find('.txt')]
    plt.plot(ds, percentages, ':', label=graph_label) 


plt.title('Start and end stream filter')
plt.ylabel('Percentage of streams eliminated')
plt.xlabel('delay(s)')

plt.xticks([0.2*i for i in range(0,11)])
plt.yticks([i*10 for i in range(0,11)])
plt.axis(xmin=0,xmax=2,ymin=0,ymax=100)
plt.legend(loc='best')
plt.show()
fig.savefig("graphs/" + args.outputfilename) 

