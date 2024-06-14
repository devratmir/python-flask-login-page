# python-flask-login-page
A project I have successfully finished - a login page made with Python (Flask), HTML and JS.

## Prerequisites
- [Flask](https://github.com/pallets/flask)
```
pip install flask
```

## Running
```
python main.py
```

## How does it work?
Users are stored in users.json, which is constantly updated during account modification. Flask is used only to serve the website files and to handle the requests sent by the HTML forms. Now yes, that does mean that if you just open the files in your browser it will not work, since the directories don't actually exist and the files exist as templates. Flask handles the different data sent by the forms, and returns HTML or redirects. JS was also used to receive and handle information from Flask, using window.location.search, which I found useful.

CSS would probably be the hardest part (since I am not amazing at it) if not for flexbox. It is actually very simple to do such a layout:
```
form {
  display: flex;
  flex-direction: column;
  width: 30%; /* Customisable */
}

button {
  width: 50%; /* Of the form */
}
```

## License
Feel free to use any part of this code for any of your projects or as inspiration. This was a very fun project for me to do and in my opinion the best one I did so far.
