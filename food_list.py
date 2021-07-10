
    #Start a groccery list by adding food, describing food type, and why its your favorite

class Food_list:
    class Food:
        def __init__(self, food_name, food_type, favorite):
           #init
            self.food_name = food_name
            self.food_type = food_type
            self.favorite = favorite
        def __str__(self):
                #Return a string of the food items to print
            return self.food_name + " (" + self.food_type + ") : " + self.favorite

    def __init__(self, max_size):
        #Init for an empty queue using python
        self.queue = []
        if max_size <= 0:
            self.max_size = 10  
        else:
            self.max_size = max_size

    def add_food(self):
        #Prompt the user for food name, type and why its their favorite
        if len(self.queue) >= self.max_size:
            print("Max Number of foods in Queue.")
            return

        food_name = input(" What is the food_name: ")
        food_type = input(" Food type: ")
        favorite = input("favorite: ")

        food = Food_list.Food(food_name, food_type, favorite)
        self.queue.append(food)
    def favorite_list(self):
        #Dequeue the next food and display the information.
        if len(self.queue) == 0: 
            print("No food in Queue")
        else:
            food = self.queue[0]
            del self.queue[0]         
            print(food)


# Test Cases

# Test 1: Can I add one food and finish my food list?
print("Test 1")
Food = Food_list(6)
Food.add_food()
Food.favorite_list()  

print("=================")

# Test 2: Does the max queue size get enforced?
print("Test 2")
Food = Food_list(6)
Food.add_food()
Food.add_food()
Food.add_food()
Food.add_food()
Food.add_food()
Food.add_food()
Food.add_food()
print("Food Queue: ", Food)

print("=================")

# Test 3: Can I add two foods and have the food list in the correct order?
print("Test 3")
Food = Food_list(6)
Food.add_food()
Food.add_food()
print("Before serving foods: ",Food)
Food.favorite_list()
Food.favorite_list()
print("After serving foods: ",Food)

print("=================")

# Test 4: Can I food to the list if there is no food?

print("Test 4")
Food = Food_list(6)
Food.favorite_list()


