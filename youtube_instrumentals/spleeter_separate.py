# from spleeter.separator import Separator
# import time
# import threading


# TODO: idk why this try to rerun whole app after each iteration

def spleeter_2stems(link_list):
    x = threading.Thread(target=seapration(link_list[0]), args=(1,))
    x.start()
    time.sleep(10)
    x.join()
