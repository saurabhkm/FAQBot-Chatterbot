from flask import Flask, render_template, request, redirect

from chatterbot import ChatBot
from chatterbot.training.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot("Virtual RA", logic_adapters=["chatterbot.adapters.logic.ClosestMatchAdapter", "chatterbot.adapters.logic.TimeLogicAdapter", "chatterbot.adapters.logic.MathematicalEvaluation"])
chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("chatterbot.corpus.english")

app = Flask(__name__)

query = "question goes here"
reply = "bot reply goes here!"

@app.route('/')
def hello_world():
    return render_template('index.html', questionAsked=query, response=reply)

@app.route('/signup', methods = ['POST'])
def signup():
	global query
	global reply
	query = request.form['question']
	response = chatbot.get_response(query)
	print(response)
	reply = response
	return redirect('/')

if __name__ == "__main__":
    app.run()
