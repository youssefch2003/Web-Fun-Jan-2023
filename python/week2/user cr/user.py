from mysqlconnection import connectToMySQL

class User:
    def __init__(self,data_dict):
        self.id = data_dict['id'] 
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    @classmethod
    def get_all(cls):
        query= "SELECT * FROM users"
        result = connectToMySQL('users_shema').query_db(query)
        strings=[]
        for row in result:
            user = cls(row)
            strings.append(user)
        return strings
    @classmethod
    def create(cls,data):
        query= """INSERT INTO users (first_name,last_name,email)
        VALUES (%(first_name)s,%(last_name)s,%(email)s);
        """
        results=connectToMySQL('users_shema').query_db(query,data)
        return results
