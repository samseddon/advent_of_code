    #for key in vars(fight).keys():
    #    if key != "spells":
    #        print(key, vars(fight)[key])
import random
import copy

class Fight():
    def __init__(self, o_hp, o_mana, b_hp, b_damage, spells):
        self.mana_spent = 0 
        self.o_hp = o_hp
        self.armor = 0 
        self.o_mana = o_mana
        self.b_hp = b_hp
        self.b_damage = b_damage
        self.spells = spells
        self.active_spells = []
        self.available_spells = [key for key in spells.keys()]
        self.effects = dict()


        #print([spell for spell in self.spells], self.effects.keys())
        
    def fight_print(self):
        print("Player has", self.o_hp, "hp", self.armor, "armor", self.o_mana, "mana")
        print("Boss has", self.b_hp, "hp")
        print("Available spells", self.available_spells)

    def cast_spell(self, key):
        cast_spell = copy.deepcopy(self.spells[key])
        #print(self.effects)
        if cast_spell["effect"] == 0:
            self.mana_spent += cast_spell["cost"]
            self.o_mana -= cast_spell["cost"]
            self.b_hp -= cast_spell["damage"]
            self.o_hp += cast_spell["heal"]
        elif key not in self.effects.keys():
            self.available_spells.remove(key)
            self.active_spells.append(key)
            self.mana_spent += cast_spell["cost"]
            self.o_mana -= cast_spell["cost"]
            self.effects[key] = cast_spell

    def effect_spell(self):
    #    print([key for key in self.effects.keys()], self.active_spells, self.available_spells)
    
        for key in self.effects.keys():
            spell = self.spells[key]
            if key == "shield":
                self.armor = spell["armor"]
                self.effects[key]["effect"] -= 1
            else:
                self.b_hp -= spell["damage"]
                self.o_hp += spell["heal"]
                self.o_mana += spell["mana"]
                self.effects[key]["effect"] -= 1 
        self.remove_effect()

    def remove_effect(self):
        keys = [key for key in self.effects.keys()]
        for key in keys:
            if key == "shield" and self.effects[key]["effect"] == 0:
                self.effects.pop(key)
                self.available_spells.append(key)
                self.active_spells.remove(key)
                self.armor = 0
                pass
            elif self.effects[key]["effect"] == 0:
                self.effects.pop(key)
                self.available_spells.append(key)
                self.active_spells.remove(key)


    def boss_turn(self):
        #print("\n--Boss turn--")
        #self.fight_print()
        self.effect_spell()
        if self.b_hp <= 0:
            
         #   print(battle.mana_spent)
          #  print("Boss defeated!")
            return True
        else:
            self.o_hp -= max(self.b_damage - self.armor, 1)
            return False

    def player_turn(self, test_key):
       # print("\n--players turn--")
        #self.fight_print()        
        self.effect_spell()
        if self.b_hp <= 0: 
            return True
        self.cast_spell(test_key)
        return False
        

def fight_sim(battle, next_spell):
    boss_alive = False
    while boss_alive == False:
        if boss_alive == True:
            break
        boss_alive = battle.player_turn(next_spell)
        if boss_alive == True:
            break
        else:
            boss_alive = battle.boss_turn()
        next_spell = random.choice(battle.available_spells)
        #print("next spell", next_spell)
         
    if battle.o_hp > 0 and battle.o_mana > 0:
        return battle.mana_spent
    else:
        return 10000



spells = dict()
spells["magic_missile"] = {"cost":53,
                           "damage":4,
                           "heal":0,
                           "effect":0,
                           "armor":0,
                           "mana":0}
spells["drain"]         = {"cost":73,
                           "damage":2,
                           "heal":2,
                           "effect":0,
                           "armor":0,
                           "mana":0}
spells["shield"]        = {"cost":113,
                           "damage":0,
                           "heal":0,
                           "effect":6,
                           "armor":7,
                           "mana":0}
spells["poison"]        = {"cost":173,
                           "damage":3,
                           "heal":0,
                           "effect":6,
                           "armor":0,
                           "mana":0}
spells["recharge"]      = {"cost":229,
                           "damage":0,
                           "heal":0,
                           "effect":5,
                           "armor":0,
                           "mana":101}


battle = Fight(10, 250, 14, 8, spells)

test_keys = ["poison", "recharge", "shield", "poison", "magic_missile"]
test_keys = ["recharge", "shield", "drain", "poison", "magic_missile"]
#Poison -> Recharge -> Shield -> Drain -> MM spam
min_mana = []
c = 0 
while c < 1000000:
    battle = Fight(50, # Own HP
                   500, # Own Mana
                   58, # Boss_HP
                   9, # Boss_damage
                   spells)
    next_spell = random.choice([key for key in spells.keys()])
    mana_spent = fight_sim(battle, next_spell)    
    min_mana.append(mana_spent)
    c += 1
    
print(min(min_mana))


