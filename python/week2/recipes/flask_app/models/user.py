from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

from flask_app.models import recipe
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls,data):
        query= """INSERT INTO users (first_name, last_name, email, password) 
        VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    # def __repr__(self) -> str:
    #     return f"{self.first_name} {self.last_name}"
    @classmethod
    def get_by_id(cls,data):
        query=""" SELECT * FROM users WHERE id =%(id)s
        """
        result = connectToMySQL(DATABASE).query_db(query,data)
        print(result)
        if (result):
            return cls(result[0])
        
    
    @classmethod
    def get_by_email(cls,data):
        query=""" SELECT * FROM users WHERE email =%(email)s
        """
        result = connectToMySQL(DATABASE).query_db(query,data)
        if (result):
            return cls(result[0])
        return False






    # * validation
    @staticmethod
    def validate(data):
        is_valid=True
        if len(data['first_name'])<2:
            flash("Invalid first name!")
            is_valid=False
        if len(data['last_name'])<2:
            flash("Invalid last name!")
            is_valid=False
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email !")
            is_valid=False
        elif User.get_by_email({'email':data['email']}) :
            flash(" already used email adress!")
            is_valid=False
        if len(data['password'])<6 :
            flash("Invalid password!")
            is_valid=False
        elif data['password'] != data['confirm'] :
            flash(" password must  match!")
            is_valid=False

        return is_valid


