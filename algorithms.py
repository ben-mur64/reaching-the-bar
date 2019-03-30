import school
import preferences

def calculate(school, preferences):
    vals = get_weighted_scores(school, preferences)
    
    top = vals["e_p"] + vals["b_l"] + vals["s_l"] + vals["clerk"] + vals["p_s"] + vals["u_p"] + vals["debt"] + vals["att"] + vals["prest"]
    
    bottom = preferences.emp_percent + preferences.big_law + preferences.small_law + preferences.clerkships + preferences.public_service + preferences.unemp_percent + preferences.debt + preferences.attrition + preferences.prestige

    return top / bottom

def get_weighted_scores(school, preferences):
    max_debt = 378322
    min_debt = 98073
    percent_denom1 = 30

    vals = {}

    vals["e_p"] = school.emp_percent * preferences.emp_percent
    vals["b_l"] = (school.big_law / 80) * preferences.big_law
    vals["s_l"] = (school.small_law / percent_denom1) * preferences.small_law
    vals["clerk"] = (school.clerkships / percent_denom1) * preferences.clerkships
    vals["p_s"] = (school.public_service / percent_denom1) * preferences.public_service
    vals["u_p"] = (100 - school.unemp_percent) * preferences.unemp_percent
    vals["debt"] = (100 - ((school.debt - min_debt)/(max_debt - min_debt) * 100)) * preferences.unemp_percent
    vals["att"] = (100 - school.attrition) * preferences.attrition
    vals["prest"] = (101 - school.prestige / 100) * preferences.prestige
    
    return vals