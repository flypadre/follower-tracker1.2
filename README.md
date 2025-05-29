Follower Tracker (Will not work with the FREE developer tier on X.com)
Overview
Follower Tracker is a Flask-based web application designed to monitor changes in your mutual followers on X.com (formerly Twitter). It helps you track who has unfollowed you and retrieve a list of your recent followers.

Features
✅ Track Mutual Followers – Identify users who unfollowed you. ✅ Fetch Recent Followers – Display the five most recent followers. ✅ Simple Web Interface – View results dynamically on a webpage. ✅ API Integration – Connects to X.com API for real-time data retrieval.

Setup & Installation
1. Clone the Repository
bash
git clone https://github.com/your-username/follower-tracker.git
cd follower-tracker
2. Set Up Virtual Environment
bash
python -m venv .venv
source .venv/bin/activate   # On Windows, use .venv\Scripts\activate
3. Install Dependencies
bash
pip install -r requirements.txt
4. Configure API Keys
Create a .env file in the root directory:

plaintext
X_API_KEY=your-api-key
X_API_SECRET=your-api-secret
X_ACCESS_TOKEN=your-access-token
X_ACCESS_TOKEN_SECRET=your-access-token-secret
5. Run the Flask App
bash
python app.py
Open http://127.0.0.1:5000 in your browser.

Usage
Check Followers
Visit /check_followers to retrieve users who have unfollowed you.

Get Recent Followers
Visit /get_five_followers to display the five most recent followers.

Troubleshooting
403 Forbidden Error? Ensure your X.com app is attached to a Project in the Developer Portal.

401 Unauthorized? Check if your API tokens are valid and match your registered callback URI.

Still not working? Check X.com API Documentation for updated requirements.

License
This project is open-source under the MIT License.
