from .. import app


class User(app.db.Model):
    """Data model for user accounts."""

    __tablename__ = 'banners'
    id = app.db.Column(app.db.Integer,
                   primary_key=True)
    username = app.db.Column(app.db.String(64),
                         index=False,
                         unique=True,
                         nullable=False)
    email = app.db.Column(app.db.String(80),
                      index=True,
                      unique=True,
                      nullable=False)
    created = app.db.Column(app.db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
    bio = app.db.Column(app.db.Text,
                    index=False,
                    unique=False,
                    nullable=True)
    admin = app.db.Column(app.db.Boolean,
                      index=False,
                      unique=False,
                      nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)
