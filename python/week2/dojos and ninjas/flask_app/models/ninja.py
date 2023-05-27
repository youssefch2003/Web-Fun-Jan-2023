from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

from flask_app.models import dojo



class Ninja :
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.age = data_dict['age']
        self.dojo_id = data_dict['dojo_id']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.team = dojo.Dojo.get_one( {'id': self.dojo_id} ).name

    @classmethod
    def create_ninja(cls,data):
        query = """
        INSERT INTO ninjas (first_name, last_name,age,dojo_id)
        VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
    
    @classmethod
    def get_all(cls):
        query = "SELECT * from ninjas;"
        results  = connectToMySQL(DATABASE).query_db(query)
        all_ninjas = []
        for row in results:
            ninja = cls(row)
            all_ninjas.append(ninja) 
        return all_ninjas

    @classmethod
    def get_dojo_ninjas(cls,data):
        query = "SELECT * from ninjas WHERE dojo_id=%(dojo_id)s;"
        results  = connectToMySQL(DATABASE).query_db(query,data)
        ninjas=[]
        if(results):
            for row in results:
                ninjas.append(cls(row))
            return ninjas
        else:
            return []