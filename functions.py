import json


def load_candidates(filename):
    """Загружает личные данные студентов из файла в список python"""
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_all(filename):
    """Функция показывает всех кандидатов"""
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_by_pk(pk):
    """Функция возвращает имя кандидата по его pk"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            if pk == item["pk"]:
                return item


def get_by_skill(skill_name, filename):
    """Функция возвращает имена кандидатов по наличию навыков"""
    write_out = ""
    for item in filename:
        if skill_name in item['skills'].lower().split(', '):
            write_out += f"<pre>\n \
            Имя кандидата - {item['name']}\n \
            Позиция кандидата: {item['position']}\n \
            Навыки через запятую: {item['skills']}\n \
            </pre>"
    return write_out


def get_position(pk):
    """Функция возвращает позицию кандидата по его pk"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            if pk == item["pk"]:
                return item["position"]


def get_skills(pk):
    """Функция возвращает skills кандидата по его pk"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            if pk == item["pk"]:
                return item["skills"]


def show_candidates(data):
    for i in data:
        return f'<pre>\n \
            Имя кандидата - {i["name"]}\n \
            Позиция кандидата: {i["position"]}\n \
            Навыки через запятую: {i["skills"]}\n \
            \n \
            </pre>'
