import json

def load_candidates(filename):
    """ Загружает данные из файла """
    with open(filename, 'r', encoding='utf-8') as f:
        candidates_list = json.load(f)
    return candidates_list


def get_all(candidates_list):
    """ Показывает всех кандидатов"""
    number = 0
    candidate_name = []
    for candidate in candidates_list:
        inf = f"\tИмя кандидата - {candidates_list[number]['name']}\n\t" \
              f"Позиция кандидата - {candidates_list[number]['position']}\n\t" \
              f"Навыки кандидата - {candidates_list[number]['skills']}\n\t"
        candidate_name.append(inf)
        number += 1
    return ' \n'.join(candidate_name)


def get_by_pk(pk, candidates_list):
    """ Вернет кандидатов по pk"""
    number = pk - 1
    inf = f"\t<img src={candidates_list[number]['picture']}>\n\t" \
          f"Имя кандидата - {candidates_list[number]['name']}\n\t" \
          f"Позиция кандидата - {candidates_list[number]['position']}\n\t" \
          f"Навыки кандидата - {candidates_list[number]['skills']}\n\t"
    return inf


def get_by_skill(skill_name, candidates_list):
    """ Вернет кандидатов по навыку"""
    skills_list = []
    number = 0
    for candidate in candidates_list:
        if skill_name in candidates_list[number]['skills']:
            skills_list.append(candidates_list[number]['name'])
            skills_list.append(candidates_list[number]['position'])
            skills_list.append(candidates_list[number]['skills'])
        number += 1

    return '\n'.join(skills_list)

