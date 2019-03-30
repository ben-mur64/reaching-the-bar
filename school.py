from serpy import Serializer, FloatField, StrField

class School:
    name = None
    full_name = None
    emp_percent = 0.0
    big_law = 0.0
    small_law = 0.0
    public_service = 0.0
    clerkships = 0.0
    unemp_percent = 0.0
    debt = 0.0
    attrition = 0.0
    prestige = 0.0
    gpa = 0.0
    lsat = 0.0

    def __init__(self, name, full_name, emp_percent, big_law, small_law, clerkships, public_service,
    unemp_percent, debt, attrition, prestige, gpa, lsat):
        self.name = name
        self.full_name = name
        self.emp_percent = emp_percent
        self.big_law = big_law
        self.small_law = small_law
        self.clerkships = clerkships
        self.public_service = public_service
        self.unemp_percent = unemp_percent
        self.debt = debt
        self.attrition = attrition
        self.prestige = prestige
        self.gpa = gpa
        self.lsat = lsat

    def calculate_score(self, weights):
        return None

class SchoolSerializer(Serializer):
    name = StrField(required = True)
    emp_percent = FloatField(required = True)
    big_law = FloatField(required = True)
    small_law = FloatField(required = True)
    public_service = FloatField(required = True)
    clerkships = FloatField(required = True)
    unemp_percent = FloatField(required = True)
    debt = FloatField(required = True)
    attrition = FloatField(required = True)
    prestige = FloatField(required = True)