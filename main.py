# main.py
from user.user import app

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 Starting Pest Detection System...")
    print("🔗 Server: http://localhost:5000")
    print("=" * 60)
    app.run(debug=True, port=5000)