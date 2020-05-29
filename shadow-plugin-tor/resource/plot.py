START_TIME = 16:40:00 #after 1000 seconds, we care about the log!

d = [0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
percentages = [[],[],[],[]]
for run in range(4):
    potential_times = []
    log_list = open("list" + run ".txt")
    times = []
    server_time = float(log_list.next()) #assuming first line is the time of first HTTP request
    for line in log_list:
        times.append(float(line))
    for delay in d:
        for time in times:
            if  time >= server_time - d :
                potential_times.append(time)
        percent = potential_times.size() / times.size()
        percentages[run].append(percent) 
