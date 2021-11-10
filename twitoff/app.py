from flask import Flask, render_template
from .models import DB, User, Tweet
from .twitter import add_or_update_user, get_all_usernames, vectorize_tweet


def create_app():
    # initializes our app
    app = Flask(__name__)

    # Database configurations
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite3'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Give our APP access to our database
    DB.init_app(app)

    # Listen to a "route"
    # '/' is the home page route
    @app.route('/')
    def root():
        # query the DB for all users
        users = User.query.all()
        # what I want to happen when somebody goes to home page
        return render_template('base.html', title="Home", users=users)

    @app.route('/update')
    def update():
        '''update all users'''
        usernames = get_all_usernames()
        for username in usernames:
            add_or_update_user(username)
        return "updated"

    @app.route('/populate')
    def populate():
        ryan = User(id=1, username='Ryan')
        DB.session.add(ryan)
        julian = User(id=2, username='Julian')
        DB.session.add(julian)
        tweet1 = Tweet(id=1, text='tweet text', user=ryan,
                       vect=vectorize_tweet('tweet text'))
        DB.session.add(tweet1)
        tweet2 = Tweet(id=2, text="julian's tweet", user=julian,
                       vect=vectorize_tweet("julian's tweet"))
        DB.session.add(tweet2)
        # save the database
        DB.session.commit()
        return '''Created some users. 
        <a href='/'>Go to Home</a>
        <a href='/reset'>Go to reset</a>
        <a href='/populate'>Go to populate</a>'''

    @app.route('/reset')
    def reset():
        # remove everything from the database
        DB.drop_all()
        # Creates the database file initially.
        DB.create_all()
        return '''The database has been reset. 
        <a href='/'>Go to Home</a>
        <a href='/reset'>Go to reset</a>
        <a href='/populate'>Go to populate</a>'''

    return app