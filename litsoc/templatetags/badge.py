from django import template

register = template.Library()

@register.simple_tag
def approval_count(slot_list):
    ret=0
    print slot_list
    for slot in slot_list:
        print slot
        if slot: 
            if not slot.approved_team:
                ret+=len(slot.teams.all())
    return ret