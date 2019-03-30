from serpy import DictSerializer, Serializer, StrField, FloatField

class Report:
    scores = {}

    def __init__(self, names, scores):
        for i in range(len(names)):
            self.scores[names[i]] = scores[i]

class ScoreSerializer(DictSerializer):
    name = StrField()
    score = FloatField()

class ReportSerializer(Serializer):
    scores = ScoreSerializer()
