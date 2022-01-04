from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Congratulations, it's a web app!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)


@app.route('/githubIssue', methods=['POST'])
def githubIssue():
    data = request.json
    print(f'Issue {data["issue"]["title"]} {data["action"]}')
    print(f'{data["issue"]["body"]}')
    print(f'{data["issue"]["url"]}')
    return data