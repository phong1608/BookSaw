from flask import render_template, redirect, url_for, flash, request
from __init__ import db, app, photos
from flask_login import login_required,current_user,logout_user,login_user
from shop.products.models import Product
@app.route('/')
def index(): 
    featured_books=Product.query.limit(4).all()
    popular_books=Product.query.filter(Product.category_id==12).limit(4).all()
    romance_novels = Product.query.filter(Product.category_id==11).limit(4).all()
    fictional_novels = Product.query.filter(Product.category_id==10).limit(4).all()
    historical_novels = Product.query.filter(Product.category_id==15).all()
    detective_novel = Product.query.filter(Product.category_id==14).all()
    return render_template('index.html',featured_books=featured_books,popular_books=popular_books,romance_novels=romance_novels,historical_novels=historical_novels,fictional_novels=fictional_novels,detective_novel=detective_novel)

@app.route('/profile',methods=['POST','GET'])
@login_required
def profile():
    if request.method=='POST':
        current_user.name=request.form.get('name')
        current_user.email=request.form.get('email')
        current_user.contact=request.form.get('contact')
        current_user.address=request.form.get('address')
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('/customer/profile.html')