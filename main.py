from webappfiles import create_app
app = create_app()
#run your server and allow errors to be shown on the page
#after publishing the app, you can remove the debug=true
#everytime you make a change in the main.py file, the webserver will automatically rerun
if __name__ == "__main__":
    app.run()