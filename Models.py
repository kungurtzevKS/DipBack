from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Firstname = db.Column(db.String(50))
    Secondname = db.Column(db.String(50))

    login = db.Column(db.String(50))
    password = db.Column(db.String(50))

    mail = db.Column(db.String(50))
    avatar_name = db.Column(db.String(50))

    VKToken = db.Column(db.String(50))
    FBToken = db.Column(db.String(50))
    TGToken = db.Column(db.String(50))

    def toJson(self):
        return {
            "id": self.id,
            "Firstname": self.Firstname,
            "Secondname": self.Secondname,
            "login": self.login,
            "password": self.password,
            "mail": self.mail,
            "avatar_name": self.avatar_name,

            "VKToken": self.VKToken,
            "FBToken": self.FBToken,
            "TGToken": self.TGToken
        }