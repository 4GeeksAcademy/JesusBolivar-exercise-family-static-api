class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

  
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        member["last_name"] = self.last_name
        if "id" not in member:
            member["id"] = self._generate_id()
        self._members.append(member)
        return member

    def delete_member(self, id):
       self._members = [member for member in self._members if member["id"] != id]
       return None
       
            

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
            
        return None

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members