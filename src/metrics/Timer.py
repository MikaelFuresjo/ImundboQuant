import os
import time

class Timer(object):
    startTime = None

    def __init__(self):
        self.startTime = time.time()

    def reset(self):
        self.startTime = time.time()

    def elapsed(self):
        return time.time() - self.startTime

    def print_elapsed(self, message=None, extraNewline=True):
        print("{0} @ {1:.2f} s".format(message, time.time() - self.startTime))
        if (extraNewline):
            print()
