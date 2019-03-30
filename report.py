class Report:
    score = 0.0
    lsat_75 = 0.0
    gpa_75 = 0.0

    def __init__(self, score, lsat, gpa):
        self.score = score
        self.lsat_75 = lsat
        self.gpa_75 = gpa

    def to_json(self):
        return { "score" : self.score,
                "lsat_75" : self.lsat_75,
                "gpa_75" : self.gpa_75}