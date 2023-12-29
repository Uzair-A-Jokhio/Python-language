class Dog:
    def __init__(self, name,bred,age):
        self.name = name
        self.bred = bred
        self.age = age
    def dog_age(self):
        return self.age * 7
    def __str__(self):
        return f"This is a dog {self.name} he is a {self.bred}, his age {self.age}. "



fox = Dog("hendrick","german sherpard", 3)

print(fox.dog_age())
print(fox.bred)
print(fox)





print("-----------------------------------------------------------------------------------------------------------")


class Apple:
    def __init__(self, color, taste):
        self.color = color
        self.taste = taste

    def __str__(self):
        return f"this is an apple {self.color} and it is {self.taste}"

print("-----------------------------------------------------------------------------------------------------------")



class Clothing:
    stock = {'name': [], 'material': [], 'amount': []}

    def __init__(self, name):
        material = ""
        self.name = name

    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)

    def Stock_by_Material(self, material):
        count = 0
        n = 0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n += 1
        return count


class shirt(Clothing):
    material = "Cotton"


class pants(Clothing):
    material = "Cotton"


polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)


print("-----------------------------------------------------------------------------------------------------------")


# Begin Portion 1#
import random


class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random() * 10 + 1
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id] = connection_load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        self.connections.pop(connection_id, None)

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        for load in self.connections.values():
            total += load
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())


print("-----------------------------------------------------------------------------------------------------------")



#Begin Portion 2#
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server
        # Add the connection to the server
        server = random.choice(self.servers)
        self.connections[connection_id] = server
        server.add_connection(connection_id)

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        # Close the connection on the server
        # Remove the connection from the load balancer
        server = self.connections[connection_id]
        server.close_connection(connection_id)
        self.connections.pop(connection_id, None)

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        total_load = 0
        for server in self.servers:
            total_load += server.load()
        return total_load/len(self.servers)


    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load() > 50:
            self.servers.append(Server())

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))