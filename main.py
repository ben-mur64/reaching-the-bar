import json
import school
import preferences
import algorithms
import scraper
import dao
import report

import os
import tornado
from tornado.escape import json_encode
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application

user_pref = preferences.Preferences(5,5,0,1,1,3,4,3,1,0,0)

names = ["harvard"]

def get_reports(names):
    reports = []
    global user_pref
    schools = dao.get_all_schools()
    for i in range(len(names)):
        reports.append(report.Report(names[i], algorithms.calculate(schools[i], user_pref), schools[i].lsat, schools[i].gpa))
    return reports

class ReportHandler(RequestHandler):
    def get(self):
        for report in get_reports(dao.get_school_names()):
            self.write(json.dumps(report.__dict__))

class PreferencesHandler(RequestHandler):
    def get(self):
        self.write(open("pref_form.html", "r").read())

    def post(self):
        global user_pref 
        user_pref = json.loads(self.request.body, object_hook = preferences.as_preferences)

class ScrapeTestHandler(RequestHandler):
    def get(self):
        dao.create_tables()
        for s in scraper.get_all_schools(scraper.get_school_names()):
            dao.insert_school(s)
        self.write(str(dao.get_all_schools()))
        '''data = scraper.get_all_schools(names)
        for val in data:
            self.write(school.SchoolSerializer(val).data)'''

class ResyncHandler(RequestHandler):
    def get(self):
        dao.create_tables()
        schools = scraper.get_all_schools(scraper.get_school_names())
        for s in schools:
            dao.insert_school(s)
        self.write("Successfully synced data for " + str(len(schools)) + " schools.")

class MainHandler(RequestHandler):
    def get(self):
        self.write(open("index.html", "r").read())

def make_app():
    settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "web"),
    "template_path":os.path.join(os.path.dirname(__file__), "templates"),
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    "login_url": "/login",
    "xsrf_cookies": False,
}
    return Application([
        (r"/", MainHandler),
        (r'/report', ReportHandler),
        (r'/preferences', PreferencesHandler),
        (r'/scrape', ScrapeTestHandler),
        (r'/resync', ResyncHandler),
        (r"/(apple-touch-icon\.png)", tornado.web.StaticFileHandler,
     dict(path=settings['static_path'])),
    ], **settings)

def main():
    print("Hello world!")

    app = make_app()
    app.listen(8080)

    print('Listening on port 8080')

    IOLoop.current().start()


if __name__ == "__main__":
    main()