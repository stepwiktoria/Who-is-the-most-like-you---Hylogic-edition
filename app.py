from flask import Flask, render_template, request
import csv
from models.database import compare_answers

app = Flask(__name__)

def load_questions_from_csv(file_path):
    questions = []
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            question = {
                'question': row[0],
                'category': row[1],
                'is_stimulant': row[2] == 'stimulant'
            }
            questions.append(question)
    return questions

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        questions = load_questions_from_csv('data/questions.csv')
        return render_template('index.html', questions=questions)
    elif request.method == 'POST':
        answers = {key: int(value) for key, value in request.form.items()}
        result = compare_answers(answers)  # Przetwarzanie odpowiedzi
        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
