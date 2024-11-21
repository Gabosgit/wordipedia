import time 

def set_timer(time_limit):
    start_time = time.time()
    print (f"You have {time_limit} seconds to answser")
    while True:
        time_passed = time.time() - start_time
        remaining_time = time_limit - time_passed
        if remaining_time <= 0: 
            print ("Time's up!")
            return None

