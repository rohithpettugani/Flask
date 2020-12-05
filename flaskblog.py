import os

from flask import Flask, render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename

from forms import InputForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567890123456'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Category = db.Column(db.String(20), nullable=False)
    Item_Title = db.Column(db.String(20), nullable=False)
    Item_Description = db.Column(db.String(100), nullable=False)
    Item_Price = db.Column(db.Integer, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __str__(self):
        return f'{self.Item_Title} and id is {self.id}'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/listing-Hats')
def listing_hats():
    posts = Item.query.filter_by(Category='Hats').all()
    return render_template('listing.html', posts=posts)


@app.route('/listing-Shirts')
def listing_shirts():
    posts = Item.query.filter_by(Category='Shirts').all()
    return render_template('listing.html', posts=posts)


@app.route('/listing-Shoes')
def listing_shoes():
    posts = Item.query.filter_by(Category='Shoes').all()
    return render_template('listing.html', posts=posts)


@app.route('/listing-Pants')
def listing_pants():
    posts = Item.query.filter_by(Category='Pants').all()
    return render_template('listing.html', posts=posts)


@app.route('/input-item', methods=['GET', 'POST'])
def input_item():
    form = InputForm()
    if form.validate_on_submit():
        filename = 'default.jpg'
        f = form.Item_icon.data
        if f :
            filename = secure_filename(f.filename)
            f.save(os.path.join('static\icons', filename))

        item = Item(
            Category=form.Category.data,
            Item_Title=form.Item_Title.data,
            Item_Description=form.Item_Description.data,
            Item_Price=form.Item_Price.data,
            image_file=url_for('static', filename='icons/'+filename)
        )
        print(url_for('static', filename='icons/'+filename))
        print(item.image_file)
        db.session.add(item)
        db.session.commit()
        flash(f'you have added your last item with product id {item.id} successfully', 'success')
        return redirect(url_for('home'))
    Errors = []
    fields = []
    if form.errors :
        fields = form.errors.keys()
        Errors = form.errors.values()
    return render_template('input_item.html', form=form, errors = Errors)


if __name__ == '__main__':
    app.run(debug=True)
