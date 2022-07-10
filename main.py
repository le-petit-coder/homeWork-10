from functions import *
from flask import Flask


def main():
    data = load_candidates('candidates.json')
    app = Flask(__name__)

    @app.route("/")
    def page_main():
        str_out = ""
        for i in data:
            str_out += f'<pre>\n \
            Имя кандидата - {i["name"]}\n \
            Позиция кандидата: {i["position"]}\n \
            Навыки через запятую: {i["skills"]}\n \
            \n \
            </pre>'
        return str_out

    @app.route("/candidates/<int:candidate_id>")
    def page_candidates(candidate_id):
        item = get_by_pk(candidate_id)
        return f"<img src={item['picture']}>\n \
        <pre>\n \
        Имя кандидата - {item['name']}\n \
        Позиция кандидата: {item['position']}\n \
        Навыки через запятую: {item['skills']}\n \
        </pre>"

    @app.route("/skills/<skill>")
    def page_skills(skill):
        return get_by_skill(skill, data)

    app.run(host='127.0.0.1', port=8000)


if __name__ == '__main__':
    main()
