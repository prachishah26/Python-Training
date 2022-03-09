# Share single variable between two continuous loops.


import threading, time
result = 2
def cube_of_numbers(result):
    """
    This functin will return cube of the particular number
    """
    for i in range(3):
        time.sleep(1)
        result *= result**3
        print("Cube: {}".format(result))

def square_of_numbers(result):
    """
    This function will return square of the particular number
    """
    for i in range(3):
        time.sleep(1)
        result *= result**2
        print("Square: {}".format(result))

if __name__ == "__main__":
    # creating the thread
    t1 = threading.Thread(target=square_of_numbers, args=(result,))
    t2 = threading.Thread(target=cube_of_numbers, args=(result,))

    # starting thread t1
    t1.start()
    # starting thread t2
    t2.start()

    # wait until t1 is completed
    t1.join()
    # wait until t2 is completed
    t2.join()

    # both threads completed
    print("Done!") 