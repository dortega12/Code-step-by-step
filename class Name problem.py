class Name():
    def __init__(self, first_name, middle_initial, last_name):
        self.first_name = first_name
        self.middle_initial = middle_initial
        self.last_name = last_name
        
    def get_normal_order(self):
        return self.first_name + " " + self.middle_initial + ". " + self.last_name
        
    def get_reverse_order(self):
        return self.last_name + ", " + self.first_name + " " + self.middle_initial + "."
        
    def __str__(self):
        return self.first_name + " " + self.middle_initial + ". " + self.last_name
        
def main():
    p1 = Name("Abigail", "R", "Hall")
    
    print(p1.first_name)
    print(p1.middle_initial)
    print(p1.last_name)
    print(p1.get_normal_order())
    print(p1.get_reverse_order())
    print(str(p1))
    
main()