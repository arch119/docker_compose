#!/usr/bin/env python

from redis import Redis
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=5000, help="run on the given port", type=int)

redis = Redis(host='redis', port=6379)
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        count = redis.incr('hits')
        self.write('Hello from Docker compose! I have been seen {} times.\n'.format(count))

def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()