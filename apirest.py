from api import app
import os

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run('0.0.0.0', port=port)
