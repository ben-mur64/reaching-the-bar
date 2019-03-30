import json
import school
import preferences
import algorithms
import scraper

import tornado
from tornado.escape import json_encode
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application

'''harvard = school.School("Harvard", 86.9, 56.7, 0.3, 11.8, 15.9, 7.8, 365164, 0, 2)
vandy = school.School("Vanderbilt", 86.2, 30.3, 3.2, 9.6, 9.6, 7.8, 318887, 0, 18)
ucla = school.School("UCLA", 78.8, 56.7, 36.9, 10.6, 21.8, 3.6, 263740, 0.3, 15)

schools = {}
schools[harvard.name] = harvard
schools[vandy.name] = vandy
schools[ucla.name] = ucla '''
user_pref = preferences.Preferences(5,5,0,1,1,3,4,3,1,0,0)

names = ["harvard", "vanderbilt", "ucla"]

def get_report(names):
    scores = {}
    global user_pref
    schools = scraper.get_all_schools(names)
    for i in range(len(names)):
        scores[names[i]] = algorithms.calculate(schools[i],user_pref)
    return scores

class ReportHandler(RequestHandler):
    def get(self):
        final_report = get_report(names)
        self.write(json.dumps(final_report))

class PreferencesHandler(RequestHandler):
    def get(self):
        self.write(open("pref_form.html", "r").read())

    def post(self):
        global user_pref 
        user_pref = json.loads(self.request.body, object_hook = preferences.as_preferences)

class ScrapeTestHandler(RequestHandler):
    def get(self):
        data = scraper.get_all_schools(names)
        for val in data:
            self.write(school.SchoolSerializer(val).data)

class MainHandler(RequestHandler):
    def get(self):
        self.write(open("index.html", "r").read())

def make_app():
    return Application([
        (r"/", MainHandler),
        (r'/report', ReportHandler),
        (r'/preferences', PreferencesHandler),
        (r'/scrape', ScrapeTestHandler)
    ])

def main():
    print("Hello world!")

    app = make_app()
    app.listen(8080)

    print('Listening on port 8080')

    IOLoop.current().start()


if __name__ == "__main__":
    main()