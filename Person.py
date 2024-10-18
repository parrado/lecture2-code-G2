class Person:    

    def __init__(self):
        self.name= []

    def set_name(self, user_name):
        self.name.append(user_name)
        # Retorna un id que inicia en cero
        return len(self.name) -1

    def get_name(self, user_id):
        if user_id >= len(self.name):
            return 'El usuario no existe'
        else:
            return self.name[user_id]
