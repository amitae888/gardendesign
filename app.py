import os
import logging
from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the base class for models
class Base(DeclarativeBase):
    pass

# Initialize SQLAlchemy with custom base class
db = SQLAlchemy(model_class=Base)

# Create the Flask application
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Configure database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///gardening.db")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

# Initialize database with app
db.init_app(app)

# Import models
with app.app_context():
    from models import Contact, BlogPost
    db.create_all()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/blog')
def blog():
    # Get all published blog posts, ordered by publish date (newest first)
    posts = BlogPost.query.filter_by(is_published=True).order_by(BlogPost.published_at.desc()).all()
    
    # Get unique seasons for filtering
    seasons = db.session.query(BlogPost.season).distinct().all()
    seasons = [season[0] for season in seasons]
    
    # Get unique categories for filtering
    categories = db.session.query(BlogPost.category).distinct().all()
    categories = [category[0] for category in categories]
    
    return render_template('blog/index.html', posts=posts, seasons=seasons, categories=categories)

@app.route('/blog/<string:slug>')
def blog_post(slug):
    # Get the specific blog post by slug
    post = BlogPost.query.filter_by(slug=slug, is_published=True).first_or_404()
    
    # Get related posts (same season or category, but not the current post)
    related_posts = BlogPost.query.filter(
        (BlogPost.season == post.season) | (BlogPost.category == post.category),
        BlogPost.id != post.id,
        BlogPost.is_published == True
    ).order_by(BlogPost.published_at.desc()).limit(3).all()
    
    return render_template('blog/post.html', post=post, related_posts=related_posts)

@app.route('/blog/season/<string:season>')
def blog_by_season(season):
    # Get posts filtered by season
    posts = BlogPost.query.filter_by(season=season, is_published=True).order_by(BlogPost.published_at.desc()).all()
    
    # Get all seasons for the filter navigation
    seasons = db.session.query(BlogPost.season).distinct().all()
    seasons = [s[0] for s in seasons]
    
    # Get all categories for the filter navigation
    categories = db.session.query(BlogPost.category).distinct().all()
    categories = [c[0] for c in categories]
    
    return render_template('blog/index.html', posts=posts, seasons=seasons, categories=categories, current_filter=season, filter_type='season')

@app.route('/blog/category/<string:category>')
def blog_by_category(category):
    # Get posts filtered by category
    posts = BlogPost.query.filter_by(category=category, is_published=True).order_by(BlogPost.published_at.desc()).all()
    
    # Get all seasons for the filter navigation
    seasons = db.session.query(BlogPost.season).distinct().all()
    seasons = [s[0] for s in seasons]
    
    # Get all categories for the filter navigation
    categories = db.session.query(BlogPost.category).distinct().all()
    categories = [c[0] for c in categories]
    
    return render_template('blog/index.html', posts=posts, seasons=seasons, categories=categories, current_filter=category, filter_type='category')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        service_type = request.form.get('service_type')

        # Validate form data
        if not name or not email or not message:
            flash('Please fill out all required fields.', 'danger')
            return render_template('contact.html')

        try:
            # Create new contact entry
            new_contact = Contact(
                name=name,
                email=email,
                phone=phone,
                message=message,
                service_type=service_type,
                created_at=datetime.now()
            )
            
            # Add to database
            db.session.add(new_contact)
            db.session.commit()
            
            # Show success message and redirect
            flash('Your message has been sent! We will get back to you soon.', 'success')
            return redirect(url_for('contact'))
        
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error saving contact: {str(e)}")
            flash('There was an error sending your message. Please try again.', 'danger')
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
