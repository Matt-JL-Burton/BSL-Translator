from flask import Flask, render_template, request

app = Flask(__name__)
import markovify
from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function

@app.route('/')
def home():
    return render_template('index.html')


# retrievs the comment from web app and renders predicted value in web page
@app.route('/success', methods=['POST'])
def print_data():
    msg = request.form['message']
    # text = msg
    text = "Aladdin is young boy living with his mother in poverty in a town in China. His father died recently, having tried unsuccessfully to persuade his son to knuckle down and learn a trade. Aladdin, however, prefers to go off and play with the other boys in the street.  One day, a sorcerer approaches Aladdin, claiming to be his uncle. He convinces Aladdin to work with him, telling Aladdin that if he does what he tells him, the boy will grow up to be rich. Aladdin’s mother, who has never met the sorcerer before, is initially suspicious of his claim to be a long-lost relative but she becomes convinced that the man is genuine.  The man shows Aladdin gardens full of beautiful riches, before leading Aladdin down into a cave, telling the boy to fetch an oil lamp found inside. He gives Aladdin a magic ring that will protect him while he searches for it. But when he finds the lamp, Aladdin refuses to pass it up to the sorcerer before he is out of the cave, so the sorcerer seals Aladdin inside the cave with the lamp!  But A"
    # Train model
    text_model = markovify.Text(text)
    res = ""
    # Generate sentences
    for i in range(20):
        lisadd = str((text_model.make_sentence()))
        res = res + lisadd

    print(res)
    return render_template('result.html', prediction=res)


if __name__ == '__main__':
    app.run()