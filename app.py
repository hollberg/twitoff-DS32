from flask import Flask

# Initialize our app
app = Flask(__name__)

app_title = 'Twitoff DS32'


# Listen to a 'route'
# "/" is the home page route
@app.route('/')
def root():  # put application's code here
    return f'<p>Another {app_title} page</p>'


@app.route('/foo')
def myfoo():
    return f'<p>This is the foo page!</p>'


if __name__ == '__main__':
    app.run()
