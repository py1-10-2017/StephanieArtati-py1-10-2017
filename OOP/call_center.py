from datetime import datetime

class Call(object):
    def __init__(self, call_id, caller_name, caller_phone_number, time_of_call, reason_for_call):
        self.call_id = call_id
        self.caller_name = caller_name
        self.caller_phone_number = caller_phone_number
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call

    def display_call(self):
        print("Call ID: ", self.call_id)
        print("Caller Name: ", self.caller_name)
        print("Caller Phone Number: ", self.caller_phone_number)
        print("Time of Call: ", self.time_of_call)
        print("Reason for Call: ", self.reason_for_call)
        print("")

class CallCenter(object):
    def __init__(self):
        self.call_list = []
        self.queue_size = 0

    def add(self, call):
        self.call_list.append(call)
        self.queue_size += 1
        return self

    def remove(self,phone_number = None):
        if (phone_number != None):
            for i in range(0,self.queue_size):
                if (self.call_list[i].caller_phone_number == phone_number):
                    self.call_list.pop(i)
                    self.queue_size -= 1
                    break
        else:
            self.call_list.pop(0)
            self.queue_size -= 1

    def info(self):
        self.call_list = sorted(self.call_list, key=lambda Call: Call.time_of_call)
        for call in self.call_list:
            print("Name: "+call.caller_name+" Phone Number: "+call.caller_phone_number)
        print("Queue size: "+str(self.queue_size))

MyCC = CallCenter()
Call1 = Call(1,"Stephanie Artati","4083682886",datetime.now(),"new user sign-up")
Call2 = Call(2,"Junaili Lie","2068176626",datetime.now(),"cancel membership")
MyCC.add(Call1)
MyCC.add(Call2)
MyCC.info()
MyCC.remove("2068176626")
MyCC.info()
# print(MyCC.__dict__)
