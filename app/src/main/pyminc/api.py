from __future__ import print_function
import sys
import zerorpc
import datetime
import json
from ws4py.client.threadedclient import WebSocketClient


class MinControlAPI(object):
    def __init__(self):
        print('initialised')
        self.message="init message"
        self.minwsip = "ws://"+ "127.0.0.1" + ":9500/"
        self.helper = HelpTheMinion(self.minwsip)
        self.helper.connect()

    #def process_shizzle(self):
    #    for minION in minIONdict:
    #        print minION

    def fetchminIONdict(self):
        try:
            #return self.message+text
            return json.dumps(minIONdict)
        except Exception as e:
            print (e)
            pass
    def calc(self, text):
        """based on the input text, return the int result"""
        try:
            return text
        except Exception as e:
            return 0.0
    def echo(self, text):
        """echo any text"""
        print ('start running on {}'.format(type(text)))
        return text
    def sendtime(self,msg):
        """echo current time"""
        msg = unicode(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print ('start running on {}'.format(type(msg)))
        return msg
    def sendversion(self):
        return version
        #return text

class HelpTheMinion(WebSocketClient):

#    def __init__(self,minIONdict):
#        self.minIONdict = minIONdict

    def opened(self):
        print ("Connected to Master MinION Controller!")

    def initialiseminion():
        result = self.send(json.dumps({"params": "null", "id": 5, "method": "initialization_status"}))
        #print result

    def received_message(self, m):
        ##print "message received!"
        for thing in ''.join(map(chr,map(ord,str(m)))).split('\n'):
            if len(thing) > 5 and "2L" not in thing and "2n" not in thing:
                if thing[1:8] not in minIONdict:
                    #print "INITIALISING MINIONDICT"
                    minIONdict[thing[1:8]]=dict()
                print ("minION ID:{}".format(thing[1:8]))
                ##print map(ord,thing)
                minIONports =  map(lambda x:x-192+8000,filter(lambda x:x>190,map(ord,thing)))
                ##print minIONports
                if len(minIONports) > 0:
                    minIONdict[thing[1:8]]["state"]="active"
                    port = minIONports[0]
                    ws_longpoll_port = minIONports[1]
                    ws_event_sampler_port = minIONports[2]
                    ws_raw_data_sampler_port = minIONports[3]
                    minIONdict[thing[1:8]]["port"]=port
                    minIONdict[thing[1:8]]["ws_longpoll_port"]=ws_longpoll_port
                    minIONdict[thing[1:8]]["ws_event_sampler_port"]=ws_event_sampler_port
                    minIONdict[thing[1:8]]["ws_raw_data_sampler_port"]=ws_raw_data_sampler_port
                else:
                    minIONdict[thing[1:8]]["state"]="inactive"
                    minIONdict[thing[1:8]]["port"]=""
                    minIONdict[thing[1:8]]["ws_longpoll_port"]=""
                    minIONdict[thing[1:8]]["ws_event_sampler_port"]=""
                    minIONdict[thing[1:8]]["ws_raw_data_sampler_port"]=""


def parse_port():
    port = 4242
    try:
        port = int(sys.argv[1])
    except Exception as e:
        pass
    return '{}'.format(port)

def main():
    global version
    version = '0.1'
    global minIONdict
    minIONdict=dict()
    addr = 'tcp://127.0.0.1:' + parse_port()
    s = zerorpc.Server(MinControlAPI())
    s.bind(addr)
    print('start running on {}'.format(addr))
    s.run()

if __name__ == '__main__':
    main()
