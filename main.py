from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['GET', 'POST'])
def download():
    return send_from_directory('static', path="files/TicTacToe.zip", filename="files/TicTacToe.zip")

if __name__ == '__main__':
    app.run(debug=True)