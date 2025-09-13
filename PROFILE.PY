class Profile:
    def __init__(self):
        self.name = "Anna-Swift"
        self.favorite_language = "Python and French"
        self.hobby = "reading"
        self.tech_stack = ["Python", "JavaScript", "HTML", "CSS"]
        self.github_username = "anntech54"
        self.fun_fact = "I once hiked to the top of a volcano!"
    
    def introduce(self):
        print("Hi, I'm " + self.name + ". I love " + self.favorite_language + " and my hobby is " + self.hobby + ".")
    
    def show_stack(self):
        print("My Tech Stack:")
        for item in self.tech_stack:
            print("* " + item)
    
    def github_link(self):
        return "https://github.com/" + self.github_username

# Create and display profile
my_profile = Profile()
my_profile.introduce()
print()
my_profile.show_stack()
print()
print("GitHub: " + my_profile.github_link())
print("Fun fact: " + my_profile.fun_fact)