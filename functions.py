def monument(name, province, start_tier, tier1, tier2, tier3):
    return {'name' : name, 'province' : province, 'start_tier' : start_tier, 'tier1' : tier1, 'tier2' : tier2, 'tier3' : tier3}

def tier(tier, upgrade_time, upgrade_cost, province_mods, area_mods, country_mods, on_upgraded):
    return {'tier' : 'tier_' + str(tier),
            'upgrade_time' : upgrade_time,
            'upgrade_cost' : upgrade_cost,
            'province_mods' : province_mods,
            'area_mods' : area_mods,
            'country_mods' : country_mods,
            'on_upgraded' : on_upgraded}

def modifs_to_txt(lis):
    if not lis:
        return '\n'
    else:
        lines = ''
        for mod in lis:
            lines += '            %(i)s\n' % {'i' : mod}
        return lines
    
def tier_to_txt(tier):
    txt = '    %(tier)s = {\n        upgrade_time = {\n            months = %(time)d\n        }\n        province_modifiers = {\n%(prov)s        }\n        area_modifier = {\n%(area)s        }\n        country_modifiers = {\n%(coun)s        }\n        on_upgraded = {\n%(upgr)s        }\n    }' % {'tier' : tier['tier'], 'time' : tier['upgrade_time'], 'cost' : tier['upgrade_cost'], 'prov' : modifs_to_txt(tier['province_mods']), 'area' : modifs_to_txt(tier['area_mods']), 'coun' : modifs_to_txt(tier['country_mods']), 'upgr' : modifs_to_txt(tier['province_mods'])}
    return txt

def to_txt(monum):
    txt = '%(name)s = {\n    start = %(prov)d\n    date = 1444.01.01\n    build_cost = 0\n    can_be_moved = no\n    move_days_per_unit_distance = 1\n    starting_tier = %(start_tier)d\n    type = monument\n    time = {\n        months = 0\n    }\n    build_trigger = {\n    }\n    can_use_modifiers_trigger = {\n    }\n    can_upgrade_trigger = {\n    }\n    keep_trigger = {\n    }' % {"name": monum['name'], "prov": monum['province'], 'start_tier' : monum['start_tier']}
    txt += '\n'
    txt += '    tier_0 = {\n        upgrade_time = {\n            months = 0\n        }\n        cost_to_upgrade = {\n            factor = %(cost)d\n        }\n        province_modifiers = {\n        }\n        area_modifier = {\n        }\n        country_modifiers = {\n        }\n        on_upgraded = {\n        }\n    }'
    txt += '\n%(tier1)s' % {'tier1' : tier_to_txt(monum['tier1'])}
    txt += '\n%(tier2)s' % {'tier2' : tier_to_txt(monum['tier2'])}
    txt += '\n%(tier3)s' % {'tier3' : tier_to_txt(monum['tier3'])}
    txt += '\n}\n'
    return txt

def gfx_text(monuments):
    txt = 'spriteTypes = {\n'
    for monum in monuments:
        txt += '    spriteType = {\n        name = "GFX_great_project_%(name)s"\n        texturefile = "gfx//interface//great_projects//great_project_%(name)s.dds"\n    }\n' % {'name' : monum['name']}
    txt += '}'
    return txt

def cap_name(name):
    words = name.split('_')
    cap = ' '
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    return cap.join(words)

def yml_txt(monuments):
    txt = 'l_english:\n'
    for monum in monuments:
        txt += ' %(name)s_title:0 "%(cap)s"\n %(name)s:0 "%(cap)s"\n great_project_%(name)s_title:0 "%(cap)s"\n' % {'name' : monum['name'], 'cap' : cap_name(monum['name'])}
    return txt