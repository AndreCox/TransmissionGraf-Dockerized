import sched
import time
import os

def run_tg(path):
    os.system('python3 ' + path + 'TG.py')
    
def main():
    print("Starting TransmissionGraf")
    # run TG.py every minute
    s = sched.scheduler(time.time, time.sleep)
    path = os.path.dirname(os.path.realpath(__file__)) + '/'
    run_tg(path)
    while True:
        s.enter(60, 1, run_tg, (path,))
        s.run()

if __name__ == '__main__':
    main()
