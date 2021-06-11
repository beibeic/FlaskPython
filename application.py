from flask import Flask, render_template
import os
app=Flask(__name__)
@app.route('/')
def index():
    image_names = os.listdir('static')
    print(image_names[0])
    return render_template("gallery.html", user_image = image_names)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)