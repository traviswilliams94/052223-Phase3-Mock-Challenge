class Restaurant:

    def __init__(self, name):
        self.name = name
        
    def reviews(self, new_review=None):
        from classes.review import Review
        pass
    
    def customers(self, new_customer=None):
        from classes.review import Review
        pass

    def average_star_rating(self):
        pass

    @classmethod
    def get_all_restaurants(cls):
        pass