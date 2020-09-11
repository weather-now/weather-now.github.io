import SimpleHTTPServer
import SocketServer
import netifaces as ni


def getipaddress():
    interfaces =  ni.interfaces()
    ips = ['127.0.0.1']
    for i_name in interfaces:
        try:
            ifaddres = ni.ifaddresses(i_name)
            if ifaddres.get(ni.AF_INET) is not None and ifaddres.get(ni.AF_LINK) is not None:
                ips.append(ifaddres[ni.AF_INET][0]['addr'])
        except:
            pass

    return ips

if __name__ == '__main__':
    ips = getipaddress()
    PORT = 9000
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)

    for ip in ips:
        print "serving at http://%s:%s" % (ip, PORT)
    httpd.serve_forever()