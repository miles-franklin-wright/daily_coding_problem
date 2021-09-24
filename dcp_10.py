import schedule

# Good morning! Here's your coding interview problem for today.

# This problem was asked by Apple.

# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.


#### Code begins below ####



# DESCRIPTION: running jobs after x amount of minutes = from a tutorial
# def job():
#     print("a simple python scheduler")


# schedule.every(2).seconds.do(job)


# while True: 
#     schedule.run_pending()
#     None



# DESCRIPTION: my own solution
def job():
    print('job')

milliseconds = 100

def job_scheduler(job, milliseconds):
    schedule.every(milliseconds/1000).seconds.do(job)

job_scheduler(job, milliseconds)

while True:
    schedule.run_pending()
