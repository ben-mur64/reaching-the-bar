class Preferences:
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

    def __init__(self, emp_percent, big_law, small_law, clerkships, public_service, unemp_percent, debt, attrition, prestige, gpa, lsat):
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

def as_preferences(dct):
    return Preferences(dct['emp_percent'], dct['big_law'], dct['small_law'], dct['public_service'], dct['clerkships'], dct['unemp_percent'], dct['debt'], dct['attrition'], dct['prestige'], dct['gpa'], dct['lsat'])