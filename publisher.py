from twisted.web.server import Site
from twisted.web.static import File
from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.python import log
from twisted.web.server import NOT_DONE_YET

import sys


class Main(Resource):
    def render(self, request):

        request.write("<!DOCTYPE html>\n")
        request.write("<html>\n")
        request.write("<head>\n")
        request.write("</head>\n")
        request.write("<body>\n")
        request.write("Publisher\n")
        request.write("<script src=\"http://127.0.0.1:8084/scripts/widget.js\" type=\"text/javascript\"></script>")
        request.write("<div id=\"widget\"></div>")
        request.write("</body>\n")
        request.write("</html>\n")
        request.finish()
        return NOT_DONE_YET


log.startLogging(sys.stdout)
root = Main()
root.putChild('', root)
root.putChild('scripts', File("./scripts"))

reactor.listenTCP(8085, Site(root))
reactor.run()
