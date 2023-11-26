from flask import Flask, request, render_template
from openai import OpenAI
from graphs import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world(name='dashboard'):
    if request.method == 'POST':
        api = request.form['api_key']
        query = request.form['query']
        client = OpenAI(
            api_key=str(api),
        )
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": query + str(" . Always answer in html friendly format. \
                                           You would be asked either in english or spanish so answer accordingly. "),
                }
            ],
            model="gpt-3.5-turbo",
        )
        output = chat_completion.choices[0].message.content
        return render_template('dashboard.html', name=name, output=output, chart=chart)
    else:
        return render_template('dashboard.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)