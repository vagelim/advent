#!/usr/bin/env python
import md5
SECRET = "iwrupvqb"


def run(keep_going=True, count = 0):
    while keep_going == True:
        m = md5.new()
        s = SECRET + str(count)
        m.update(s)
        if m.hexdigest()[:5] == '00000':
            print count
            keep_going = False
        else:
            count += 1

if __name__ == "__main__":
    run()
