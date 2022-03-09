# Share single variable between two continuous loops.


import threading, time
result = 2
def cube_of_numbers():
    """
    This functin will return cube of the particular number
    """
    global result
    for i in range(3):
        time.sleep(1)
        result = result**3
        print("Cube: {}".format(result))

def square_of_numbers():
    """
    This function will return square of the particular number
    """
    global result
    for i in range(3):
        time.sleep(1)
        result = result**2
        print("Square: {}".format(result))

if __name__ == "__main__":
    # creating the thread
    thread1 = threading.Thread(target=square_of_numbers)
    thread2 = threading.Thread(target=cube_of_numbers)

    # starting thread thread1
    thread1.start()
    # starting thread thread2
    thread2.start()

    # wait until thread1 is completed
    thread1.join()
    # wait until thread2 is completed
    thread2.join()

    # both threads completed
    print("Done!") 