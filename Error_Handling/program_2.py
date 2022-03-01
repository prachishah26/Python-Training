# Create while loop which increase counter by one every second.
# -> Start count from 0
# -> Stop while loop when counter is grater than 500
# -> Program must not stop on any keyboard press. (Not even ctrl + c or ctrl + x) 

import time
count = 0
while count >=0:
    try :
        count += 1
        print(count)
        time.sleep(1)
        if count == 500:
            break
    except KeyboardInterrupt:
        pass


