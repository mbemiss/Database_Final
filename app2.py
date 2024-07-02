# We are going to create a simple web application use Flask to connect our existing database and display the data in a web page.
# Import our required librariesthat we will use in this application
from flask import Flask, request, render_template_string 
# This is new to use, import the SQLAlchemy class from the flask_sqlalchemy module to connect our database
# This is the most important part of this application
from flask_sqlalchemy import SQLAlchemy
# Import the text class from the sqlalchemy module to use stored procedures in our database
from sqlalchemy import text


# Create a new Flask application
app = Flask(__name__)

# Configure the database connection
# My server name is DESKTOP-DREO3DI\SQLEXPRESS
# My database name is db_theplotspot
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://@DESKTOP-DREO3DI\SQLEXPRESS/db_theplotspot?driver=SQL+Server'

# Create an instance of the SQLAlchemy class.  An instance of this class will be our database object.
db = SQLAlchemy(app)

# Define a class that will represent our table in the database
# In our case we setup a user table to query from the database.
class User(db.Model):
    __tablename__ = 'table_users'  # Change the table name to 'users' or any other name
    # Now we need to use the EXACT name of the columns in the database table.
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    registration_date = db.Column(db.DateTime, nullable=False)

# Create a route to display the data from the database
@app.route('/get_all_users')
def get_all_users():
    # Query the database to get all the users from our user table
    users = User.query.all()
    # Print out the users to the console
    for user in users:
        print(user.username, user.email, user.password, user.first_name, user.last_name, user.registration_date)
    # Create a simple HTML string to display the user's information
    users_html = '''
    <h1>Full User List</h1>
    <h4>Links to Routes</h4>
    <ul>
        <li><a href="http://127.0.0.1:5000/get_book_by_id">Get Book by ID</a></li>
        <li><a href="http://127.0.0.1:5000/get_all_users">Get All Users</a></li>
        <li><a href="http://127.0.0.1:5000/get_all_authors">Get All Authors</a></li>
    </ul>
    <h2>User Information</h2>
    <table border="1">
        <tr>
            <th>Username</th>
            <th>Email</th>
            <th>Password</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Registration Date</th>
        </tr>
    '''
    # Add each user to the table
    for user in users:
        users_html += f'''
        <tr>
            <td>{user.username}</td>
            <td>{user.email}</td>
            <td>{user.password}</td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.registration_date}</td>
        </tr>
        '''
    # Notice this is not part of the for loop.  This is outside of the loop..  We finally close the unordered list.
    users_html += '</table>'
    # Return the HTML string that we DYNAMICALLY created on the fly using SERVER-SIDE python code.
    # All we did here was build our own html page and return it to the web client (user's browser).
    return render_template_string(users_html)

# Let's add a route to get a book from the database by its ID
@app.route('/get_book_by_id', methods=['GET', 'POST'])
def get_book_by_id():
    # Check if the request method is POST, this is used when the user submits a form.
    if request.method == 'POST':
        # Get our book ID from the form submission the user made.
        book_id = request.form.get('book_id')
        # Use a stored procedure that lives on our database server to get the book by its ID
        result = db.session.execute(text('EXEC get_book_by_id :book_id'), {'book_id': book_id})
        # Query the database to get the book by its ID
        book = result.fetchone()
        # Check if a book was returned from the database. Maybe the user entered an invalid book ID, or one we just don't have in the database.
        if book:
            # Create a variable to store the HTML string. Remember, this string is our dynamic HTML page we are creating on the fly.
            # This is server-side code. We are creating the HTML page on the server and sending it to the client using the return statement.
            book_html = f'''
            <h1>Book Details for Book ID: {book_id}</h1>
            <table border="1">
                <tr>
                    <th>Attribute</th>
                    <th>Value</th>
                </tr>
            '''
            # Loop through all the keys in the result object and add them to our HTML string on the fly one by one.
            for key in result.keys():
                book_html += f'<tr><td><strong>{key}</strong></td><td>{getattr(book, key)}</td></tr>'
            # Close the table tag. Notice we are now outside all for loops so this will only run one time.
            book_html += '</table>'
        # Else, if no book was returned from the database, let our user know in the webpage by displaying a message to the user.
        else:
            book_html = f'<h1>Book not found for ID: {book_id}</h1>'
        # Return the HTML string that we dynamically created on the fly to the client. Remember server-side code built this string and now the return statement sends it to the client.
        return render_template_string(book_html)
        

    # If the request method is not POST, then we are just displaying the form to the user.
    return '''
        <h1>Get Book by ID</h1>
        <p>
        <h6>Links to Routes</h6>
        <ul>
            <li><a href="http://127.0.0.1:5000/get_book_by_id">Get Book by ID</a></li>
            <li><a href="http://127.0.0.1:5000/get_all_users">Get All Users</a></li>
            <li><a href="http://127.0.0.1:5000/get_all_authors">Get All Authors</a></li>
        </ul>
        <p>
        <form method="post">
            <label for="book_id">Book ID:</label>
            <input type="text" id="book_id" name="book_id">
            <input type="submit" value="Get Book">
        </form>
    '''
# Let's add a route to get all authors from the database.
@app.route('/get_all_authors')
def get_all_authors():
    # Use a stored procedure to get all the authors from the database.
    result = db.session.execute(text("EXEC get_all_authors"))
    authors = result.fetchall()

    # Check if any authors were returned from the database.
    if authors:
        # Create a variable to store the HTML string. Remember, this string is our dynamic HTML page we are creating on the fly.
        # This is server-side code. We are creating the HTML page on the server and sending it to the client using the return statement.
        authors_html = '''
        <h1>Authors List</h1>
        <h6>Links to Routes</h6>
        <ul>
            <li><a href="http://127.0.0.1:5000/get_book_by_id">Get Book by ID</a></li>
            <li><a href="http://127.0.0.1:5000/get_all_users">Get All Users</a></li>
            <li><a href="http://127.0.0.1:5000/get_all_authors">Get All Authors</a></li>
        </ul>
        <table border="1">
            <tr>
                <th>Author ID</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Birthdate</th>
                <th>Nationality</th>
                <th>Biography</th>
            </tr>
        '''

        # Loop through all the authors in the authors list and add them to our HTML string on the fly one by one.
        for author in authors:
            authors_html += '<tr>'
            for key in result.keys():
                authors_html += f'<td>{getattr(author, key)}</td>'
            authors_html += '</tr>'
        
        # Close the table tag. Notice we are now outside all for loops so this will only run one time.
        authors_html += '</table>'
    # Else, if no authors were returned from the database, let our user know in the webpage by displaying a message to the user.
    else:
        authors_html = '<h1>No authors found</h1>'
    
    # Return the HTML string that we dynamically created on the fly to the client. Remember server-side code built this string and now the return statement sends it to the client.
    return render_template_string(authors_html)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)