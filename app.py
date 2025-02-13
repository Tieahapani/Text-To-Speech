# These lines import the necessary libraries
from flask import Flask, render_template, request  # Flask web framework components
from gtts import gTTS  # Google Text-to-Speech library
import os  # For file/directory operations

# Create a Flask web application instance
app = Flask(__name__)

# This decorator tells Flask what URL should trigger our function
# methods=['GET', 'POST'] means this route handles both GET requests (viewing page) 
# and POST requests (submitting form)
@app.route('/', methods=['GET', 'POST'])
def home():
    # Check if the request is POST (form submission)
    if request.method == 'POST':
        # Get the text from the form field named 'text'
        # If no text is found, return empty string as default
        text = request.form.get('text', '')
        
        # Create a gTTS (Google Text-to-Speech) object
        # text = the text to convert, lang = language to use
        tts = gTTS(text=text, lang='en')
        
        # Save the audio file to the static/audio folder as speech.mp3
        tts.save('static/audio/speech.mp3')
        
        # Show the page again, but with audio_created=True to display the audio player
        return render_template('index.html', audio_created=True)
    
    # If it's a GET request (normal page visit), show the page without audio player
    return render_template('index.html', audio_created=False)

# This runs the application if this file is run directly
if __name__ == '__main__':
    # Run the app in debug mode (shows errors and auto-reloads on code changes)
    app.run(debug=True)