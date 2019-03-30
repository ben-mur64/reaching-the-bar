class Report:
    school = 0.0
    score = 0.0
    lsat_75 = 0.0
    gpa_75 = 0.0

    def __init__(self, school, score, lsat, gpa):
        self.school = school
        self.score = score
        self.lsat_75 = lsat
        self.gpa_75 = gpa