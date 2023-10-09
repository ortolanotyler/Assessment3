### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
 
 Python is a high-level, interpreted, and dynamically typed language, while JavaScript is a high-level, interpreted, and weakly typed language.Python is often used for backend development, data analysis, machine learning, and scripting. JavaScript is primarily used for web development, both on the client-side (in browsers) and server-side (with Node.js).Python uses indentation for code blocks and has a clean and readable syntax. JavaScript uses curly braces for code blocks and has a more flexible syntax.Python code is typically run on the server or locally, while JavaScript code runs in web browsers (client-side) or on servers (Node.js).Python traditionally has limited support for concurrent programming, while JavaScript can handle asynchronous operations more efficiently, making it suitable for web applications.


- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

1. You can use the get() method of a dictionary to retrieve a value for a given key. If the key is missing, it won't raise an error, and you can specify a default value to return
2. You can use a try-except block to catch the KeyError exception and handle it gracefully

- What is a unit test?
A unit test is a type of software testing where individual components or functions of a software application are tested in isolation to ensure that they work as intended. Unit tests are typically written by developers and focus on verifying the correctness of small, isolated parts of the code.
- What is an integration test?
An integration test is a type of software testing where different components or modules of an application are tested together to ensure that they interact correctly. Integration tests verify that the integrated parts of the system work as expected when combined.

- What is the role of web application framework, like Flask?

A web application framework, like Flask, provides a structured way to build web applications. Its role includes:

Routing: Defining URLs and handling HTTP requests.
Templating: Generating dynamic HTML content.
Database Integration: Interacting with databases.
Middleware: Handling common tasks like authentication and security.
Error Handling: Managing errors and exceptions.
Simplifying Development: Providing abstractions and tools to streamline web development.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

Route URL Parameter: Use route URL parameters when the data in the URL is essential for the application's core functionality or when you want to create clean and semantic URLs. For example, '/products/laptop' to view laptop details.

Query Parameter: Use query parameters when the data is optional, used for filtering, or doesn't significantly affect the core functionality. Query parameters are often used for search and filtering. For example, '/products?category=laptop' to filter products by category.

- How do you collect data from a URL placeholder parameter using Flask
In Flask, you can collect data from a URL placeholder parameter by defining a route with a variable in the URL pattern. For example:
@app.route('/products/<product_id>')
def product_detail(product_id):
    # product_id is collected from the URL
    return f"Product ID: {product_id}"

- How do you collect data from the query string using Flask?


you use request.args: 

@app.route('/search')
def search():
    query = request.args.get('query')
    return f"Search Query: {query}"

- How do you collect data from the body of the request using Flask?

To collect data from the body of the request in Flask, we can use the request.json attribute when dealing with JSON data or request.form when dealing with form data

- What is a cookie and what kinds of things are they commonly used for?
A cookie is a small piece of data that is stored on the user's computer by a web server. Cookies are stored for session management, user authentication, etc. 

- What is the session object in Flask?

The session object is a dictionary-like object that allows you to store user-specific data that persists across multiple HTTP requests

- What does Flask's `jsonify()` do?
takes a python object and converts it into a json formatted response.
