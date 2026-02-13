import time

# time.sleep(3)
# print("Wattiing for 3 seconds...")


my_time = 3605

for i in range(my_time, 0, -1):
    seconds = i % 60
    minutes = (i // 60) % 60
    hours = (i // 3600) % 24
    
    print(f"{hours:02}:{minutes:02}:{seconds:02} ")
    
    ''' 
    print(f"{seconds} seconds remaining...")
    print(f"{minutes} minutes remaining...")
    print(f"{hours} hours remaining...")
    # print(i)
    '''
    time.sleep(1)
print("Time's up!")    