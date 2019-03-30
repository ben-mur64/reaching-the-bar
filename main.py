import json
import school
import preferences
import algorithms

import tornado
from tornado.escape import json_encode
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application

harvard = school.School("Harvard", 86.9, 56.7, 0.3, 11.8, 15.9, 7.8, 365164, 0, 2)
vandy = school.School("Vanderbilt", 86.2, 30.3, 3.2, 9.6, 9.6, 7.8, 318887, 0, 18)
ucla = school.School("UCLA", 78.8, 56.7, 36.9, 10.6, 21.8, 3.6, 263740, 0.3, 15)

schools = {}
schools[harvard.name] = harvard
schools[vandy.name] = vandy
schools[ucla.name] = ucla
user_pref = preferences.Preferences(5,5,0,1,1,3,4,3,1,0,0)

names = ["Harvard", "Vanderbilt", "UCLA"]

def get_report(names, scores):
    scores = {}
    for i in range(len(names)):
        scores[names[i]] = algorithms.calculate(schools[names[i]],user_pref)
    return scores

final_report = get_report(names, user_pref)

class SchoolHandler(RequestHandler):
    def get(self):
        self.write(json_encode(school.SchoolSerializer(harvard).data))

class ReportHandler(RequestHandler):
    def get(self):
        '''self.write("Harvard: " + str(algorithms.calculate(harvard, neal)) + 
        "\nVanderbilt: " + str(algorithms.calculate(vandy, neal)) + "\nUCLA: " 
            + str(algorithms.calculate(ucla, neal)))
        '''
        self.write(json.dumps(final_report))

class PreferencesHandler(RequestHandler):
    def get(self):
        self.write(open("pref_form.html", "r").read())

    def post(self):
        user_pref = json.loads(self.request.body, object_hook = preferences.as_preferences)
        self.write("Successfully posted: " + str(user_pref))

class MainHandler(RequestHandler):
    def get(self):
        self.write(open("index.html", "r").read())

def make_app():
    return Application([
        (r"/", MainHandler),
        (r'/report', ReportHandler),
        (r'/harvard', SchoolHandler),
        (r'/preferences', PreferencesHandler)
    ])

def main():
    print("Hello world!")

    app = make_app()
    app.listen(8080)

    print('Listening on port 8080')

    IOLoop.current().start()


if __name__ == "__main__":
    main()