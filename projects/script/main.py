import random

class PresidentOrganizer:
    def __init__(self, presidents):
        self.presidents = presidents
        self.president_terms = {}  # We'll store the term in office for each president
    
    def add_term(self, president, term):
        self.president_terms[president] = term
    
    def organize_alphabetical(self):
        return sorted(self.presidents)
    
    def organize_reverse_alphabetical(self):
        return sorted(self.presidents, reverse=True)
    
    def organize_by_length(self):
        return sorted(self.presidents, key=len)
    
    def organize_by_term(self):
        sorted_presidents = sorted(self.presidents, key=lambda president: self.president_terms.get(president, 0))
        return sorted_presidents
    
    def organize_randomly(self):
        random.shuffle(self.presidents)
        return self.presidents


def main():
    # List of U.S. presidents
    presidents_list = [
        "George Washington",
        "John Adams",
        "Thomas Jefferson",
        "James Madison",
        "James Monroe",
        "John Quincy Adams",
        "Andrew Jackson",
        "Martin Van Buren",
        "William Henry Harrison",
        "John Tyler",
        "James K. Polk",
        "Zachary Taylor",
        "Millard Fillmore",
        "Franklin Pierce",
        "James Buchanan",
        "Abraham Lincoln",
        "Andrew Johnson",
        "Ulysses S. Grant",
        "Rutherford B. Hayes",
        "James Garfield",
        "Chester A. Arthur",
        "Grover Cleveland",
        "Benjamin Harrison",
        "William McKinley",
        "Theodore Roosevelt",
        "William Howard Taft",
        "Woodrow Wilson",
        "Warren G. Harding",
        "Calvin Coolidge",
        "Herbert Hoover",
        "Franklin D. Roosevelt",
        "Harry S. Truman",
        "Dwight D. Eisenhower",
        "John F. Kennedy",
        "Lyndon B. Johnson",
        "Richard M. Nixon",
        "Gerald R. Ford",
        "James Carter",
        "Ronald Reagan",
        "George H. W. Bush",
        "William J. Clinton",
        "George W. Bush",
        "Barack Obama",
        "Donald Trump",
        "Joseph R. Biden Jr."
    ]

    # Create an instance of PresidentOrganizer
    president_organizer = PresidentOrganizer(presidents_list)

    # Add the correct terms for each President
    president_organizer.add_term("George Washington", "1st President")
    president_organizer.add_term("John Adams", "2nd President")
    president_organizer.add_term("Thomas Jefferson", "3rd President")
    president_organizer.add_term("James Madison", "4th President")
    president_organizer.add_term("James Monroe", "5th President")
    president_organizer.add_term("John Quincy Adams", "6th President")
    president_organizer.add_term("Andrew Jackson", "7th President")
    president_organizer.add_term("Martin Van Buren", "8th President")
    president_organizer.add_term("William Henry Harrison", "9th President")
    president_organizer.add_term("John Tyler", "10th President")
    president_organizer.add_term("James K. Polk", "11th President")
    president_organizer.add_term("Zachary Taylor", "12th President")
    president_organizer.add_term("Millard Fillmore", "13th President")
    president_organizer.add_term("Franklin Pierce", "14th President")
    president_organizer.add_term("James Buchanan", "15th President")
    president_organizer.add_term("Abraham Lincoln", "16th President")
    president_organizer.add_term("Andrew Johnson", "17th President")
    president_organizer.add_term("Ulysses S. Grant", "18th President")
    president_organizer.add_term("Rutherford B. Hayes", "19th President")
    president_organizer.add_term("James Garfield", "20th President")
    president_organizer.add_term("Chester A. Arthur", "21st President")
    president_organizer.add_term("Grover Cleveland", "22nd & 24th President")
    president_organizer.add_term("Benjamin Harrison", "23rd President")
    president_organizer.add_term("William McKinley", "25th President")
    president_organizer.add_term("Theodore Roosevelt", "26th President")
    president_organizer.add_term("William Howard Taft", "27th President")
    president_organizer.add_term("Woodrow Wilson", "28th President")
    president_organizer.add_term("Warren G. Harding", "29th President")
    president_organizer.add_term("Calvin Coolidge", "30th President")
    president_organizer.add_term("Herbert Hoover", "31st President")
    president_organizer.add_term("Franklin D. Roosevelt", "32nd & 33rd President")
    president_organizer.add_term("Harry S. Truman", "33rd President")
    president_organizer.add_term("Dwight D. Eisenhower", "34th President")
    president_organizer.add_term("John F. Kennedy", "35th President")
    president_organizer.add_term("Lyndon B. Johnson", "36th President")
    president_organizer.add_term("Richard M. Nixon", "37th President")
    president_organizer.add_term("Gerald R. Ford", "38th President")
    president_organizer.add_term("James Carter", "39th President")
    president_organizer.add_term("Ronald Reagan", "40th President")
    president_organizer.add_term("George H. W. Bush", "41st President")
    president_organizer.add_term("William J. Clinton", "42nd President")
    president_organizer.add_term("George W. Bush", "43rd President")
    president_organizer.add_term("Barack Obama", "44th President")
    president_organizer.add_term("Donald Trump", "45th President")
    president_organizer.add_term("Joseph R. Biden Jr.", "46th President")

    # User menu
    print("How would you like to organize the list of Presidents?")
    print("Valid options: alphabetical, reverse-alpha, length, term, randomly")
    choice = input().strip().lower()

    if choice == "alphabetical":
        organized_list = president_organizer.organize_alphabetical()
    elif choice == "reverse-alpha":
        organized_list = president_organizer.organize_reverse_alphabetical()
    elif choice == "length":
        organized_list = president_organizer.organize_by_length()
    elif choice == "term":
        organized_list = president_organizer.organize_by_term()
    elif choice == "randomly":
        organized_list = president_organizer.organize_randomly()
    else:
        print("Invalid choice.")
        return
    
    print("Organized list of Presidents:")
    for president in organized_list:
        print(president)

if __name__ == "__main__":
    main()
