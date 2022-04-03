class User ():
    f_name = ""
    l_name = ""
    email = ""
    phone_nos =""
    nationality = ""
    allergies = []
    dietary_requirement = ""

    def get_username (self):
        return "{}{}" .format(self.f_name, self.l_name)

class Meal ():
    meal_title = ""
    ingredients =""
    meal_description = ""
    serving_size = ""
    allergens = []

class Order (Meal):
     order_id = ""
     meal_ordered = Meal.meal_title
     order_description = Meal.meal_description
     ingredients = Meal.ingredients
     user_quantity = Meal.serving_size

class UserMenu (User,Order):
    date =""
    time = ""
    UserName = User.get_username
    UserEmail = User.email
    menu_item = Order.order_id , Order.meal_ordered 
    menu_desc =Order.order_description
    qty = Order.user_quantity
    additional_req = ""