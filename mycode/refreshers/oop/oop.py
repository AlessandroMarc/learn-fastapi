# Objects has behabiour and state. There are 4 pillars of OOP: Encapsulation, Abstraction, Inheritance, Polymorphism

# Abstraction: Hiding the implementation details and showing only the functionality to the user.
# There are three types of constructors in Python:
# 1. Default constructor: The default constructor is simple constructor which doesn’t accept any arguments. It’s definition has only one argument which is a reference to the instance being constructed.
# 2. Parameterized constructor: Constructor with parameters is known as parameterized constructor. The parameterized constructor take its first argument as a reference to the instance being constructed known as self and the rest of the arguments are provided by the programmer.
# 3. Constructor Overloading: Python does not support explicit constructor overloading. We may overload the methods but can only use the latest defined method.

# Encapsulation: Wrapping up of data and methods into a single unit called class. It is a way to restrict access to some parts of an object.
# In our example for instance we want to avoid the user to change the health_points of the enemy object. We can do this by making the health_points private and creating a method to access it.

# Inheritance: A mechanism where a new class inherits properties and behaviour from another class. It is used with self and super. Self is used to access the properties of the class and super is used to access the properties of the parent class. In our example we can create a new class called Boss that inherits from Enemy. The Boss class will have the same properties and methods as the Enemy class. We can also override the methods of the parent class.

# Polymorphism: The ability to present the same interface for different data types.
# changinig at runtime the behaviour of a method. In our example we can create a new class called Player that has a method called attack. If we decide that there's a battle where each enemy talk and attack, we can create a method called battle that receives a list of enemies and call the attack method of each enemy. The attack method of the enemy class will be different from the attack method of the player class.
# Composition creates relationships between object, it is an 'has a' relationship. Inheritance creates relationships between classes, it is an 'is a' relationship. If I have a vehicle class for instance, I may have a engine, a wheel, a door, etc. I can create a class for each of these components and create a relationship between the vehicle class and the component class. I can also create a relationship between the component class and the vehicle class. For instance, the engine class can have a method called start that receives a vehicle object and starts the vehicle. The vehicle class can have a method called start that calls the start method of the engine class. The engine. Difference with interface is
