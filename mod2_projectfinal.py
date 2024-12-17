import random
'''
Thank you for checking out my take on the OOP assignment. Thank you for the
extra time given to catch up! I am almost caught up completely, luckily the material
for the week will allow me to get back on track, as I know the content already
The only resources used were stack overflow and the python documentation

- H White.
'''
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health 

    def attack(self, opponent):
        damage = random.randint(1, self.attack_power)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self, amount=10):
        if self.health < self.max_health:
            self.health = min(self.health + amount, self.max_health)
            print(f"{self.name} gets respite, healing {amount} HP, current health: {self.health}")
        else:
            print(f"{self.name} is already at full health!")


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=145, attack_power=43)  

    def warriors_blessing(self, opponent):
        self.attack_power += 9
        damage = random.randint(5, 26)
        opponent.health -= damage
        print(f"{self.name} uses Warrior's Blessing! Attack power increased to {self.attack_power}")
        print(f"The evil wizard is hit by {self.name}' enchanced fists of fury, doing {damage} damage, opponent has {opponent.health} HP left")

    def rage(self, boost=10):
        self.attack_power += boost
        self.health += random.randint(1, 11)
        print(f"{self.name} goes into a rage, boosting attack power by {boost} and health by {self.health}")

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=46)  

    def elemental(self, opponent):
        ele_damage = random.randint(15, 34)
        opponent.health -= (10 + ele_damage)
        print(f"{self.name} uses Elemental attack on {opponent.name} for {10 + ele_damage} damage!")
        print(f"{opponent.name} has {opponent.health} health remaining")

    def lightning_bolt(self, opponent):
        opponent.health -= 20
        print(f"{self.name} wields lightning to hit {opponent.name} for 20 damage!")
        print(f"{opponent.name} has {opponent.health} health remaining")


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=125, attack_power=43) 

    def critical_damage(self, opponent):
        critical = random.uniform(1.5, 2.5)
        damage = self.attack_power * critical
        opponent.health -= damage
        print(f"{self.name} lands a critical hit on {opponent.name} for {damage:.2f} damage!")
        print(f"{opponent.name} has {opponent.health} health remaining")

    def fire_arrow(self, opponent):
        damage = random.randint(10, 20)
        opponent.health -= damage
        print(f"{self.name} fires a flaming arrow at {opponent.name} for {damage} damage!")
        print(f"{opponent.name} has {opponent.health} health remaining")

class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=35)  

    def holy_aura(self):
        heal_amount = random.randint(10, 35)
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} uses Holy Aura to heal for {heal_amount} health, new health {self.health}")

    def smite(self, opponent):
        opponent.health -= 20
        opponent.attack_power -= 15
        self.health += 10
        print(f"{self.name} smites {opponent.name}, dealing 20 damage and reducing their attack power by 15!")
        print(f"{opponent.name} has {opponent.health} health remaining and {opponent.attack_power} attack power")

class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15) 
    
    def regenerate(self):
        heal_amount = random.randint(5, 15)
        self.health = min(self.health + heal_amount, self.max_health)
        self.health == int(self.health)
        print(f"\n{self.name} regenerates {heal_amount} health, wizard's health is now {self.health}")

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")
    print()
    class_choice = input("Enter the number for class selection: ")
    print()
    name = input("Enter your character's name: ")
    print()

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        print()
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
            print()
        elif choice == '2':
            if isinstance(player, Warrior):
                print("1. Warrior's Blessing")
                print("2. Rage")
                ability_choice = input("Choose a special: ")
                print()
                if ability_choice == '1':
                    player.warriors_blessing()
                elif ability_choice == '2':
                    player.rage()
            elif isinstance(player, Mage):
                print("1. Elemental")
                print("2. Lightning Bolt")
                ability_choice = input("Choose an ability: ")
                if ability_choice == '1':
                    player.elemental(wizard)
                elif ability_choice == '2':
                    player.lightning_bolt(wizard)
            elif isinstance(player, Archer):
                print("1. Critical Damage")
                print("2. Fire Arrow")
                ability_choice = input("Choose an ability: ")
                if ability_choice == '1':
                    player.critical_damage(wizard)
                elif ability_choice == '2':
                    player.fire_arrow(wizard)
            elif isinstance(player, Paladin):
                print("1. Holy Aura")
                print("2. Smite")
                ability_choice = input("Choose an ability: ")
                if ability_choice == '1':
                    player.holy_aura()
                elif ability_choice == '2':
                    player.smite(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"Better luck next time, {player.name}... {wizard.name} has defeated you!")
            break

    if wizard.health <= 0:
        print(f"Congratulations, {player.name}! You have defeated {wizard.name}!")
        print("\n--- Game Over ---")


def main():
   
    player = create_character()

 
    wizard = EvilWizard("The Dark Wizard")

  
    battle(player, wizard)

if __name__ == "__main__":
    main()