class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    
    def __init__(self,name):
        self.name=name
        self.friends=[]

    def add_friend(self,friend):
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    
    def __init__(self):
        self.people={}

    def add_person(self,name):
        if name not in self.people:
            self.people[name]=Person(name)

    def add_friendship(self,person1_name,person2_name):
        if person1_name in self.people and person2_name in self.people:
            person1=self.people[person1_name]
            person2=self.people[person2_name]
            person1.add_friend(person2)
            person2.add_friend(person1)
        else:
            print("Error: One or both people don't exist!")

    def print_network(self):
        for person_name,person_friends in self.people.items():
            people_names=[p.name for p in person_friends.friends]
            friended_people=", ".join(people_names)
            print(f"{person_name} is friends with: {friended_people}")


# Test your code here
network=SocialNetwork()
network.add_person("Alex")
network.add_person("Jordan")
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")
#print(network.people)
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")
#network.print_network()