
class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size 
        self.array = [None for i in range(self.array_size)]
    
    def hash(sefl, key, collisions=0):
        key_bytes = str(key).encode()
        hash_code = sum(key_bytes)
        return hash_code + collisions 

    def compressor(self, hash_code):
        return hash_code % self.array_size
    
    def setter(self, key, value):
        current_array_index = self.compressor(self.hash(key))
        current_array_value = self.array[current_array_index]

        if current_array_value == None:
            self.array[current_array_index] = [key, value]
            return 
        elif current_array_value[0] == key:
            self.array[current_array_index] = [key, value]
            return 
        else:
            number_collisions = 1
            while current_array_value[0] != key:
                new_hash_code = self.hash(key, number_collisions)
                new_array_index = self.compressor(new_hash_code)
                new_array_value = self.array[new_array_index]

                if new_array_value == None:
                    self.array[new_array_index] = [key, value]
                    return 
                elif new_array_value[0] == key:
                    self.array[new_array_index] = [key, value]
                    return 
                else:
                    number_collisions += 1
                    return 
        
    def retrieve(self, key):
        current_array_index = self.compressor(self.hash(key))
        current_array_value = self.array[current_array_index]
        
        if current_array_value == None:
            return None 
        elif current_array_value[0] == key:
            return current_array_value[1]
        else:
            retrieve_collisions = 1 
            while current_array_value[0] != None:
                new_hash_code = self.hash(key, retrieve_collisions)
                new_array_index = self.compressor(new_hash_code)
                new_array_value = self.array[new_array_index]
                
                if new_array_value == None:
                    return None 
                elif new_array_value[0] == key:
                    return new_array_value[1]
                else:
                    retrieve_collisions += 1
                    return 
    
    def delete(self, key):
        current_array_index = self.compressor(self.hash(key))
        current_array_value = self.array[current_array_index]

        if current_array_value == None:
            pass 
        elif current_array_value[0] == key:
            self.array[current_array_index] = None 
            return 
        else:
            del_collisions = 1 
            while current_array_value[0] != key:
                new_hash_code = self.hash(key, del_collisions)
                new_array_index = self.compressor(new_hash_code)
                new_array_value = self.array[new_array_index]

                if new_array_value == None:
                    pass 
                elif new_array_value[0] == key:
                    self.array[new_array_index] = None 
                    return 
                else:
                    del_collisions += 1
                    return 





