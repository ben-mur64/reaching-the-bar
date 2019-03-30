import school
import preferences

def calculate(school, preferences):
    vals = get_weighted_scores(school, preferences)
    
    top = vals.emp_percent + vals.big_law + vals.small_law + vals.clerkship + vals.public_service + vals.unemp_percent + vals.debt + vals.attrition + vals.prestige
    
    bottom = preferences.emp_percent + preferences.big_law + preferences.small_law + preferences.clerkships + preferences.public_service + preferences.unemp_percent + preferences.debt + preferences.attrition + preferences.prestige

    return top / bottom

def get_weighted_scores(school, preferences):
    max_debt = 378322
    min_debt = 98073
    percent_denom1 = 30

    e_p = school.emp_percent * preferences.emp_percent
    b_l = (school.big_law / 80) * preferences.big_law
    s_l = (school.small_law / percent_denom1) * preferences.small_law
    clerk = (school.clerkships / percent_denom1) * preferences.clerkships
    p_s = (school.public_service / percent_denom1) * preferences.public_service
    u_p = (100 - school.unemp_percent) * preferences.unemp_percent
    debt = (100 - ((school.debt - min_debt)/(max_debt - min_debt) * 100)) * preferences.unemp_percent
    att = (100 - school.attrition) * preferences.attrition
    prest = (101 - school.prestige / 100) * preferences.prestige
    
    return schools.School(e_p, b_l, s_l, clerk, p_s, u_p, debt, att, prest)