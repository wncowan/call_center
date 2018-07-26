from datetime import datetime

class Call(object):
    def __init__(self, id, caller_name, caller_phone, time_of_call, reason_for_call):
        self.id = id
        self.caller_name = caller_name
        self.caller_phone = caller_phone
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call
    def display(self):
        print "caller_name: {} caller_phone: {} time_of_call: {} reason_for_call: {}".format(self.caller_name, self.caller_phone, self.time_of_call, self.reason_for_call) 
        return self


class Call_Center(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0
    def add(self, call):
        self.calls.append(call)
        self.queue_size += 1
        return self
    def remove(self):
        self.calls.pop(0)
        self.queue_size -= 1
        return self
    def display(self):
        print self.queue_size
        return self
    def info(self):
        for call in self.calls:
            print "caller_name: {} caller_phone: {} time_of_call: {} reason_for_call: {}".format(call.caller_name, call.caller_phone, call.time_of_call, call.reason_for_call)
        return self

current_time = datetime.now()
print current_time
call1 = Call(111, "greg", "888-798-6866", str(current_time), "Advice")
call2 = Call(112, "creg", "888-798-6866", str(current_time), "Sorrow")
call3 = Call(113, "Dreg", "888-798-6866", str(current_time), "Worrow")

CC1 = Call_Center()
CC1.add(call1).add(call2).add(call3).info()