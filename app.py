from flask import Flask,request

# Create a Flask application instance
app = Flask(__name__)
port=8000
# Define a route for the root URL
@app.route('/',methods=['GET','POST'])
def home():
        if request.method =='POST':
            pass
        return "Hello, World!"

# Define a route for another URL
@app.route('/about')
def about():
    return "This is the about page."
#define a route for a user URL

@app.route('/user/<id>',methods=['GET','POST','UPDATE','DELETE'])
def user():
    return 'hii user name '
# Run the server
if __name__ == '__main__':
    # Specify host and port
    app.run(host='0.0.0.0', port=port, debug=True)
