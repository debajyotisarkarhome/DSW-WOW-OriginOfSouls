import platform
def block(sites):
    osp=platform.platform()
    osp=osp.lower()
    if osp[:3]=="win":
        host_handler=open("C:\\Windows\\System32\\drivers\\etc\\hosts","a+")
        host_data=host_handler.read()
        #print(host_data)
        for i in sites:
            if str(host_data.find(i))=="-1":
                host_handler.write('''127.0.0.1 '''+i+"\n")
                host_handler.write('''127.0.0.1 www.'''+i+"\n")
        host_handler.close()
def unblock():
    osp=platform.platform()
    osp=osp.lower()
    if osp[:3]=="win":
        host_handler=open("C:\\Windows\\System32\\drivers\\etc\\hosts","w+")
        host_data=host_handler.read()
        host_handler.write("")
        host_handler.close()
        