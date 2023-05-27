from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

from flask_app.models import ninja





class Dojo :
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.myninjas = []
    
    @classmethod
    def get_all(cls):
        query1 = "SELECT * FROM dojos;"
        # query2 = "SELECT * FROM dojos  JOIN ninjas ON dojos.id = ninjas.dojo_id;"
        results = connectToMySQL(DATABASE).query_db(query1)
        dojos = []
        for row in results:
            dojo = cls(row)
            dojo.myninjas = ninja.Ninja.get_dojo_ninjas({'dojo_id':dojo.id})
            dojos.append(dojo)
        # print(f"You Have {len(users)} users ")
        return dojos
    @classmethod
    def create_dojo(cls,data):
        query = """INSERT INTO dojos  (name) VALUES (%(name)s) ;    
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    
    @classmethod
    def get_one(cls,data):
        query = """
        SELECT * FROM dojos WHERE id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])    


