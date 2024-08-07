from flask import Flask, redirect, url_for, request, session, jsonify
from flask_oauthlib.client import OAuth
from flask_cors import CORS, cross_origin
from config import SECRET_KEY, CLIENT_ID, CLIENT_SECRET
import copy

app = Flask(__name__)
app.secret_key = SECRET_KEY

cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = ['Content- Type','Authorization']

oauth = OAuth(app)
google = oauth.remote_app(
    'google',
    consumer_key=CLIENT_ID,
    consumer_secret=CLIENT_SECRET,
    request_token_params={
        'scope': 'https://www.googleapis.com/auth/gmail.readonly https://www.googleapis.com/auth/calendar.events https://www.googleapis.com/auth/userinfo.profile'
    },
    base_url='https://www.googleapis.com/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

#this tokengetter allows us to call google.get (it tells it where to get the access token)
@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')
google.tokengetter(get_google_oauth_token)

@app.route('/')
def index():
    if 'google_token' in session:
        return redirect(url_for('welcome'))#'Logged in as: ' + session['google_token'][0]
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))

@app.route('/logout')
def logout():
    session.pop('google_token', None)
    return redirect(url_for('index'))

@app.route('/google/callback')
def authorized():
    resp = google.authorized_response()
    if resp is None or resp.get('access_token') is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['google_token'] = (resp['access_token'], '')
    return redirect(url_for('welcome'))

@app.route('/welcome')
#@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def welcome():
    user_info = google.get('oauth2/v1/userinfo').data
    return jsonify({'data': user_info.get("name")})
    #user_info = google.get('oauth2/v1/userinfo').data
    #hello = copy.deepcopy(user_info.get("name"))
    #return {"name" : str(hello)[0]}

if __name__ == '__main__':
    app.run(debug=True)