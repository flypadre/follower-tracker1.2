from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
import os
from x_api import get_mutual_followers, get_five_followers
from models import db, Follower

load_dotenv()
app = Flask(__name__)

app.config.from_object('config.Config')
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_followers', methods=['GET'])
def check_followers():
    # Fetch new mutual followers
    mutual_followers = get_mutual_followers()
    # Get previous followers from database
    previous_followers = {f.username for f in Follower.query.all()}
    #Find unfollowed users
    new_followers = {f['username'] for f in mutual_followers}
    unfollowed = previous_followers - new_followers
    # Update database
    db.drop_all()
    db.create_all()
    for follower in mutual_followers:
        db.session.add(Follower(username=follower['username']))
    db.session.commit()
    # Prepare response
    result = {'unfollowed': list(unfollowed), 'no_change': len(unfollowed) == 0}
    return jsonify(result)

@app.route('/followers', methods=['GET'])
def followers():
    return jsonify(get_five_followers())

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Create database tables
    app.run(debug=True)

