from flask_login import LoginManager, UserMixin
from ...models import User as UserModel

class LoginUser(UserModel, UserMixin):
    def get_id(self):
        return self.id

login_manager = LoginManager()

login_manager.login_view = 'admin.login'

login_manager.login_message_category = "danger"

@login_manager.user_loader
def load_user(user_id):
    return LoginUser.query.get(user_id)

def init_login_manager(app):
    login_manager.init_app(app)
