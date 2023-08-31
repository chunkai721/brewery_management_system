## main.py
from flask_admin.contrib.sqla import ModelView
from .forms import UserForm, InventoryForm, ProductionForm, SalesForm, KegForm

def create_app(test_config=None):
    """Create and configure the Flask app."""
    app = Flask(__name__)
    if test_config is None:
        app.config.from_object(Config)
    else:
        app.config.from_object(TestConfig)

    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    admin = Admin(app, name='Brewery Management System', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Inventory, db.session))
    admin.add_view(ModelView(Production, db.session))
    admin.add_view(ModelView(Sales, db.session))
    admin.add_view(ModelView(Keg, db.session))

    from . import views
    app.register_blueprint(views.bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
