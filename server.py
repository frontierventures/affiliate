from twisted.web.server import Site
from twisted.web.static import File
from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.python import log
from twisted.web.server import NOT_DONE_YET

import json
import sys


class Main(Resource):
    def render(self, request):

        request.write("<!DOCTYPE html>\n")
        request.write("<html>\n")
        request.write("<head>\n")
        request.write("</head>\n")
        request.write("<body>\n")
        request.write("Server\n")
        request.write("</body>\n")
        request.write("</html>\n")
        request.finish()
        return NOT_DONE_YET


class Load(Resource):
    def render(self, request):

        request.setHeader('Access-Control-Allow-Origin', '*')
        sessionData = {}
        sessionData['response'] = 'Ok'
        data = json.dumps(sessionData)
        return data


log.startLogging(sys.stdout)
root = Main()
root.putChild('', root)
root.putChild('loadData', Load())
root.putChild('scripts', File("./scripts"))

reactor.listenTCP(8084, Site(root))
reactor.run()
