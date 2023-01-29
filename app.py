from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    images = ["/static/images/image1.jpg", "/static/images/image2.jpg", "/static/images/image3.jpg",
              "/static/images/image4.jpg", "/static/images/image5.jpg", "/static/images/image6.jpg",
              "/static/images/image7.jpg", "/static/images/image8.jpg"]
    return render_template('index.html', images=images)

if __name__ == '__main__':
    app.run()