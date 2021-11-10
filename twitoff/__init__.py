from .app import create_app, DB

APP = create_app()
#
# # remove everything from the database
# DB.drop_all(app=APP)
# # Creates the database file initially.
# DB.create_all(app=APP)
