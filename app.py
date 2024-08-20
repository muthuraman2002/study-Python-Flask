from flask import Flask,request
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a Flask application instance
app = Flask(__name__)
port=8000
# Define a route for the root URL

# Define the database URL and create the engine
DATABASE_URL = 'sqlite:///newdatabase.db'
engine = create_engine(DATABASE_URL)

# Define the base class
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

# Create the tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add a new user
new_user = User(name='Alice', age=30)
session.add(new_user)
session.commit()

# Query the database
users = session.query(User).all()
for user in users:
    print(f'ID: {user.id}, Name: {user.name}, Age: {user.age}')

# Update a user
user_to_update = session.query(User).filter_by(name='Alice').first()
if user_to_update:
    user_to_update.age = 31
    session.commit()

# Delete a user
user_to_delete = session.query(User).filter_by(name='Alice').first()
if user_to_delete:
    session.delete(user_to_delete)
    session.commit()

# Close the session
session.close()

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
