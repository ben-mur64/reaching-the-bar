import json
import school

from tornado.escape import json_encode
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application

harvard = school.School("Harvard", 10, 10, 10, 10, 10, 10, 10, 10)

class SchoolHandler(RequestHandler):
    def get(self):
        self.write(json_encode(school.SchoolSerializer(harvard).data))

def main():
    print("Hello world!")

    Application([(r'/harvard', SchoolHandler)]).listen(8080)
    print('Listening on port 8888')

    IOLoop.current().start()


if __name__ == "__main__":
    main()