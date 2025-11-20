import random

class Boss:
    def __init__(self, name, health, attack_power, defense, special_move):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.special_move = special_move

    def attack(self, target):
        damage = max(0, self.attack_power - target.defense)
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")

    def use_special(self, target):
        # Special move deals random boosted damage
        damage = random.randint(self.attack_power, self.attack_power * 2)
        target.health -= damage
        print(f"{self.name} uses {self.special_move} on {target.name} for {damage} damage!")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} (HP: {self.health}, ATK: {self.attack_power}, DEF: {self.defense})"


class Hero:
    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense

    def attack(self, target):
        damage = max(0, self.attack_power - target.defense)
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} (HP: {self.health}, ATK: {self.attack_power}, DEF: {self.defense})"


def battle(hero, boss):
    print("\n⚔️ Battle Start ⚔️")
    print(hero)
    print(boss)

    while hero.is_alive() and boss.is_alive():
        # Hero turn
        if random.random() < 0.2:  # 20% chance hero crits
            damage = hero.attack_power * 2
            boss.health -= damage
            print(f"{hero.name} lands a CRITICAL HIT for {damage} damage!")
        else:
            hero.attack(boss)

        if not boss.is_alive():
            print(f"{boss.name} has been defeated!")
            break

        # Boss turn
        if random.random() < 0.3:  # 30% chance boss uses special
            boss.use_special(hero)
        else:
            boss.attack(hero)

        if not hero.is_alive():
            print(f"{hero.name} has fallen... Game Over.")
            break

        print(f"\nStatus: {hero} | {boss}\n")


def main():
    # Create hero
    hero = Hero("Knight Arion", 350, 50, 25)

    # Create bosses
    bosses = [
        Boss("Dragon King", 500, 75, 30, "Inferno Breath"),
        Boss("Shadow Queen", 400, 60, 20, "Dark Curse"),
        Boss("Iron Titan", 600, 90, 40, "Earthquake Slam")
    ]

    # Fight each boss in sequence
    for boss in bosses:
        if hero.is_alive():
            battle(hero, boss)
        else:
            print("The hero cannot continue the journey...")
            break


if __name__ == "__main__":
    main()
