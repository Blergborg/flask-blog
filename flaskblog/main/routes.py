from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home():
    # get page number for posts, default page 1,
    # errors will be thrown if page is not an int
    page = request.args.get("page", 1, type=int)

    # show given page with certain number of posts on page
    # posts is a pagination object with various methods
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("home.html", posts=posts)


@main.route("/about")
def about():
    return render_template("about.html", title="About")
