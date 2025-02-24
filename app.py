from textblob import TextBlob
from flask import  Flask,render_template,request

app=Flask(__name__)
def analyze(text):
    blob=TextBlob(text)
    sentiment=blob.sentiment
    polarity=sentiment.polarity
    if polarity > 0:
        category="positive"
    elif polarity < 0:
        category="negative" 
    else:
        category="neutral" 
    return category

@app.route('/',methods=['GET', 'POST'])
def index():
    sentiment = None
    if request.method == "POST":
        text = request.form['text']
        sentiment = analyze(text)
        
    return render_template('index.html',sentiment=sentiment)    

if __name__=='__main__':
    app.run(debug=True)         
