import redis





def attempt_redis_connect(host):
    port = 6379

    known_hosts = []
   
    client = redis.Redis(host=host, port = port, socket_connect_timeout=0.1)
   
       

    try:
        if(client.ping()):
            known_hosts.append(host)
            print(host)
    except:
        return

            


def get_ip_list():
#159.65.214.48
    oct1 = 47
    oct2 = 214
    oct3 = 65
    oct4 = 159 
    oct4_old = 0

    while(oct4<256):
        oct1+=1
        

        if(oct1%255==0):
            oct2+=1
            oct1=1
        

        if(oct2%255==0):
            oct3+=1
            oct2=1

        if(oct3%255==0):
            oct4+=1
            oct3=1
            print("Status: oct3 = {}".format(str(oct3)))

        attempt_redis_connect(("{}.{}.{}.{}".format(str(oct4),str(oct3),str(oct2),str(oct1))))

        if(oct4_old != oct4):
            print(oct4)
            oct4_old = oct4
        

    
    



get_ip_list()
print(client.ping())
