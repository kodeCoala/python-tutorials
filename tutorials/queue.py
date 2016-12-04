#! /usr/bin/env python

class Queue(object):
    def __init__(self, name):
        self.name = name
        self.queue = []

    def push(self, val):
        print "push:", val
        self.queue.append(val)

    def pop(self):
        if len(self.queue) > 0:
            val = self.queue[0]
            self.queue = self.queue[1:]
            print "pop:", val
            return val

    def size(self):
        return len(self.queue)

    def __repr__(self):
        tmp_list = []
        for i in range(len(self.queue)-1, -1, -1):
            tmp_list.append(self.queue[i])
        return "queue: {}".format(" ".join(str(v) for v in tmp_list))


if __name__ == '__main__':
    q = Queue("simple")
    q.push(100)
    print q
    q.push(200)
    print q
    q.push(300)
    print q
    q.pop()
    print q

