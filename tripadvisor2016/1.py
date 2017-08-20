jobs = [] # NAME #task TIME_TAKEN CAN_START PRIORITY
androids = []

from sys import stdin, exit
input = stdin

line = input.readline()
while line.strip() != '':
    args = line.strip().split()
    if args[0] == "job":
        args[2] = int(args[2])
        args[3] = int(args[3])
        args[4] = int(args[4])
        jobs.append(args[1:])
    else:
        androids.append(args[1])
    line = input.readline()

if len(jobs) == 0:
    exit()
if len(androids) == 0:
    exit()

def finished_time(job, start_time):
    time_taken = job[2]
    return start_time + time_taken

def get_next_available_job(start_time):
    global cur_job_id
    global next_time_tick

    job = jobs[cur_job_id]

    # find next task and update next time tick if necessary
    while job[1] <= 0:
        cur_job_id += 1
        if cur_job_id >= len(jobs):
            exit()

        job = jobs[cur_job_id]
        if start_time < job[3]:
            start_time = job[3]

    if finished_time(job, start_time) < next_time_tick:
        next_time_tick = finished_time(job, start_time)

    return job

def print_assignment(android_id, assignment): # assignment is [job_id, start_time]
    job_name = jobs[assignment[0]][0]
    start_time = assignment[1]
    android = androids[android_id]
    print("{} {} {}".format(start_time, android, job_name))

from operator import itemgetter

jobs.sort(key=itemgetter(3, 4))

cur_job_id = 0

cur_config = [[-1, -1] for android in androids] # [job_id, start_time] indexed by android id

# intialize config
next_time_tick = finished_time(jobs[0], jobs[0][3])

for android_id in range(len(androids)):
    job = jobs[cur_job_id]
    job = get_next_available_job(job[3])

    # make assignment
    start_time = job[3]
    assignment = [cur_job_id, start_time]
    print_assignment(android_id, assignment)

    # save to config
    cur_config[android_id] = assignment
    job[1] -= 1

def update_config():
    global next_time_tick
    global cur_job_id

    current_time_tick = next_time_tick
    next_time_tick = 1 << 32

    count_jobs = [0 for job in jobs]

    for android_id in range(len(androids)):
        assignment = cur_config[android_id]
        job = jobs[assignment[0]]
        end_time = finished_time(job, assignment[1])

        if current_time_tick >= end_time: # assign new task and update tick
            start_time = current_time_tick
            next_job = get_next_available_job(start_time)
            if next_job[3] > start_time:
                start_time = next_job[3]

            # make assignment
            assignment = [cur_job_id, start_time]
            if cur_config[android_id][0] != cur_job_id:
                print_assignment(android_id, assignment)

            # save to config
            cur_config[android_id] = assignment
            next_job[1] -= 1

        count_jobs[cur_config[android_id][0]] += 1

def make_schedule():
    while cur_job_id < len(jobs):
        update_config()

make_schedule()
