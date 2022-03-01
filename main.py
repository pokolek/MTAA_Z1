import sipfullproxy_edit

if __name__ == "__main__":
    sipfullproxy_edit.logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename='proxy.log',level=sipfullproxy_edit.logging.INFO,datefmt='%H:%M:%S')
    sipfullproxy_edit.logging.info(sipfullproxy_edit.time.strftime("%a, %d %b %Y %H:%M:%S ", sipfullproxy_edit.time.localtime()))
    sipfullproxy_edit.hostname = sipfullproxy_edit.socket.gethostname()
    sipfullproxy_edit.logging.info(sipfullproxy_edit.hostname)
    sipfullproxy_edit.ipaddress = sipfullproxy_edit.socket.gethostbyname(sipfullproxy_edit.hostname)
    if sipfullproxy_edit.ipaddress == "127.0.0.1":
        sipfullproxy_edit.ipaddress = sipfullproxy_edit.sys.argv[1]
    sipfullproxy_edit.logging.info(sipfullproxy_edit.ipaddress)
    sipfullproxy_edit.recordroute = "Record-Route: <sip:%s:%d;lr>" % (sipfullproxy_edit.ipaddress, sipfullproxy_edit.PORT)
    sipfullproxy_edit.topvia = "Via: SIP/2.0/UDP %s:%d" % (sipfullproxy_edit.ipaddress,sipfullproxy_edit.PORT)
    sipfullproxy_edit.server = sipfullproxy_edit.socketserver.UDPServer((sipfullproxy_edit.HOST, sipfullproxy_edit.PORT), sipfullproxy_edit.UDPHandler)
    print("Proxy server adress: %s:%s" % (sipfullproxy_edit.ipaddress, sipfullproxy_edit.PORT))
    sipfullproxy_edit.server.serve_forever()

