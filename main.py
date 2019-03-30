import json
import school
import report

from tornado.escape import json_encode
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application

harvard = school.School("Harvard", 10, 10, 10, 10, 10, 10, 10, 10)

names = ["Harvard", "Yale", "UC Berkley", "BYU"]
scores = [10.0, 9.0, 5, 6]
final_report = report.Report(names,scores)

class SchoolHandler(RequestHandler):
    def get(self):
        self.write(json_encode(school.SchoolSerializer(harvard).data))

class ReportHandler(RequestHandler):
    def get(self):
        self.write(json_encode(report.ReportSerializer(final_report)))

class MainHandler(RequestHandler):
    def get(self):
        self.write(open("index.html", "r").read())

def make_app():
    return Application([
        (r"/", MainHandler),
        (r'/report', ReportHandler),
        (r'/harvard', SchoolHandler)
    ])

def main():
    print("Hello world!")

    app = make_app()
    app.listen(8080)

    print('Listening on port 8080')

    IOLoop.current().start()


if __name__ == "__main__":
    main()