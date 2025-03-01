from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == 'POST':
    #     username = request.form['username']
    #     password = request.form['password']
    #     # הוספת קוד לבדוק את שם המשתמש והסיסמה
    #     return "ברוך הבא, {}".format(username)  # או מעבר לעמוד אחר
    return render_template('login.html')


@app.route('/contact-us', methods=['GET', 'POST'])
def contact():
    return render_template('contact-us.html')


@app.route('/profile', methods=['GET'])
def profile():
    return render_template('profile.html')


@app.route('/add-product', methods=['GET'])
def add_product():
    return render_template('add-product.html')


@app.route('/product-gallery', methods=['GET'])
def product_gallery():
    return render_template('product-gallery.html')

@app.route('/product-info', methods=['GET'])
def product_info():
    return render_template('product-info.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
