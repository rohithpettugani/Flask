from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class InputForm(FlaskForm):
    Category = SelectField('Category',validators=[DataRequired()], choices=[('Hats', 'Hats'), ('Shirts', 'Shirts'), ('Pants', 'Pants'),('Shoes','Shoes')])
    Item_Title = StringField('Item Title',validators=[DataRequired(),Length(max=30)])
    Item_Description = StringField('Item_Description',validators=[DataRequired(),Length(max=100)])
    Item_Price = IntegerField('Item_Price',validators=[DataRequired('price must be in integer only')])
    Item_icon = FileField('icon',validators = [FileAllowed(['jpg', 'png'], 'supported formats for icon are jpg and png only!')])
    Save = SubmitField('Save')