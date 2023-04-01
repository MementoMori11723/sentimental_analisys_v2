from flask import Flask,render_template,request
from newspaper import Article
from textblob import TextBlob
import nltk

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/result",methods = ['POST',"GET"])
def result():
    if request.method=='POST':
        url = request.form['url']
        nltk.download('punkt')
        artical = Article(url)
        artical.download()
        artical.parse()
        artical.nlp()
        text = artical.summary
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        if sentiment >= 0:
            return render_template("result.html",text = text, review = "Good")
        else:
            return render_template("result.html",text = text, review = "Bad")


if __name__ == "__main__":
    app.run(debug=True,port=5000)