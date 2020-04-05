import random


class Pokemon:
    possible_pokemon = {'Glaceon': ['Glaceon', 'Ice', None, 240, 240, 112, 202, 238, 175, 121],
                        'Togepi': ['Togepi', 'Fairy', None, 180, 180, 40, 121, 76, 121, 40],
                        'Beedrill': ['Beedrill', 'Bug', 'Poison', 240, 240, 166, 76, 85, 148, 139],
                        'Raichu': ['Raichu', 'Electric', None, 230, 230, 166, 103, 166, 148, 202],
                        'Magikarp': ['Magikarp', 'Water', None, 150, 150, 22, 103, 31, 40, 148],
                        'Rhyhorn': ['Rhyhorn', 'Ground', 'Rock', 270, 270, 157, 175, 58, 58, 49]}

    @staticmethod
    def type_advantage(Move_Type, *Enemy_Type):
        type_advantage = 1

        for Type in Enemy_Type:
            if Enemy_Type == 'Normal':
                if Move_Type == "Fighting":
                    type_advantage *= 2
                if Move_Type == "Ghost":
                    type_advantage *= 0

            if Type == 'Bug':
                if Move_Type == "Fire" or Move_Type == 'Flying' or Move_Type == 'Rock':
                    type_advantage *= 2
                if Move_Type == "Grass" or Move_Type == 'Fighting' or Move_Type == 'Ground':
                    type_advantage *= 1 / 2

            if Type == 'Fighting':
                if Move_Type == 'Bug' or Move_Type == 'Rock' or Move_Type == 'Dark':
                    type_advantage *= 1 / 2
                if Move_Type == 'Flying' or Move_Type == 'Psychic' or Move_Type == 'Fairy':
                    type_advantage *= 2

            if Type == 'Fire':
                if Move_Type == 'Fire' or Move_Type == 'Grass' or Move_Type == 'Ice' or Move_Type == 'Bug' \
                        or Move_Type == 'Steel' or Move_Type == 'Fairy':
                    type_advantage *= 1 / 2
                if Move_Type == 'Water' or Move_Type == 'Rock' or Move_Type == 'Ground':
                    type_advantage *= 2

            if Type == 'Water':
                if Move_Type == 'Fire' or Move_Type == 'Water' or Move_Type == 'Ice' or Move_Type == 'Steel':
                    type_advantage *= 1 / 2
                if Move_Type == 'Electric' or Move_Type == 'Grass':
                    type_advantage *= 2

            if Type == 'Electric':
                if Move_Type == 'Electric' or Move_Type == 'Flying' or Move_Type == 'Steel':
                    type_advantage *= 1 / 2
                if Move_Type == 'Ground':
                    type_advantage *= 2

            if Type == 'Grass':
                if Move_Type == 'Water' or Move_Type == 'Electric' or Move_Type == 'Grass' or Move_Type == 'Ground':
                    type_advantage *= 1 / 2
                if Move_Type == 'Fire' or Move_Type == 'Ice' or Move_Type == 'Poison' or Move_Type == 'Flying' \
                        or Move_Type == 'Bug':
                    type_advantage *= 2

            if Type == 'Ice':
                if Move_Type == 'Ice':
                    type_advantage *= 1 / 2
                if Move_Type == 'Fire' or Move_Type == 'Fighting' or Move_Type == 'Rock' or Move_Type == 'Steel':
                    type_advantage *= 2

            if Type == 'Poison':
                if Move_Type == 'Grass' or Move_Type == 'Fighting' or Move_Type == 'Poison' \
                        or Move_Type == 'Bug' or Move_Type == 'Fairy':
                    type_advantage *= 1 / 2
                if Move_Type == 'Ground' or Move_Type == 'Psychic':
                    type_advantage *= 2

            if Type == 'Ground':
                if Move_Type == 'Electric':
                    type_advantage *= 0
                if Move_Type == 'Poison' or Move_Type == 'Rock':
                    type_advantage *= 1 / 2
                if Move_Type == 'Water' or Move_Type == 'Grass' or Move_Type == 'Ice':
                    type_advantage *= 2

            if Type == 'Flying':
                if Move_Type == 'Ground':
                    type_advantage *= 0
                if Move_Type == 'Grass' or Move_Type == 'Fighting' or Move_Type == 'Bug':
                    type_advantage *= 1 / 2
                if Move_Type == 'Electric' or Move_Type == 'Ice' or Move_Type == 'Rock':
                    type_advantage *= 2

            if Type == 'Psychic':
                if Move_Type == 'Fighting' or Move_Type == 'Psychic':
                    type_advantage *= 1 / 2
                if Move_Type == 'Bug' or Move_Type == 'Ghost' or Move_Type == 'Dark':
                    type_advantage *= 2

            if Type == 'Rock':
                if Move_Type == 'Normal' or Move_Type == 'Fire' or Move_Type == 'Poison' or Move_Type == 'Flying':
                    type_advantage *= 1 / 2
                if Move_Type == 'Water' or Move_Type == 'Grass' or Move_Type == 'Fighting' or \
                        Move_Type == 'Ground' or Move_Type == 'Steel':
                    type_advantage *= 2

            if Type == 'Ghost':
                if Move_Type == 'Normal' or Move_Type == 'Fighting':
                    type_advantage *= 0
                if Move_Type == 'Poison' or Move_Type == 'Bug':
                    type_advantage *= 1 / 2
                if Move_Type == 'Ghost' or Move_Type == 'Dark':
                    type_advantage *= 2

            if Type == 'Dragon':
                if Move_Type == 'Fire' or Move_Type == 'Water' or Move_Type == 'Electric' or Move_Type == 'Grass':
                    type_advantage *= 1 / 2
                if Move_Type == 'Ice' or Move_Type == 'Dragon' or Move_Type == 'Fairy':
                    type_advantage *= 2

            if Type == 'Dark':
                if Move_Type == 'Psychic':
                    type_advantage *= 0
                if Move_Type == 'Ghost' or Move_Type == 'Dark':
                    type_advantage *= 1 / 2
                if Move_Type == 'Fighting' or Move_Type == 'Bug' or Move_Type == 'Fairy':
                    type_advantage *= 2

            if Type == 'Steel':
                if Move_Type == 'Poison':
                    type_advantage *= 0
                if Move_Type == 'Fire' or Move_Type == 'Fighting' or Move_Type == 'Ground':
                    type_advantage *= 2
                if Move_Type == 'Normal' or Move_Type == 'Grass' or Move_Type == 'Ice' or Move_Type == 'Flying' or \
                        Move_Type == 'Psychic' or Move_Type == 'Bug' or \
                        Move_Type == 'Rock' or Move_Type == 'Dragon' or \
                        Move_Type == 'Steel' or Move_Type == 'Fairy':
                    type_advantage *= 1 / 2

            if Type == 'Fairy':
                if Move_Type == 'Dragon':
                    type_advantage *= 0
                if Move_Type == 'Fighting' or Move_Type == 'Bug' or Move_Type == 'Dark':
                    type_advantage *= 1 / 2
                if Move_Type == 'Poison' or Move_Type == 'Steel':
                    type_advantage *= 2

        return type_advantage


class Damage(Pokemon):
    @staticmethod
    def damage_dealing(Pokemon_name, Target, Move_Type, Move_Power, Attack_Type, *Type):
        Attack_Type_Stat = Pokemon.possible_pokemon[Pokemon_name][5]
        if Attack_Type == 'Special':
            Defense = Pokemon.possible_pokemon[Target][8]
        else:
            Defense = Pokemon.possible_pokemon[Target][6]
        Enemy_type = [Pokemon.possible_pokemon[Target][1], Pokemon.possible_pokemon[Target][2]]
        if Type == Move_Type:
            X = 1.5
        else:
            X = 1
        Z = random.randint(217, 255)
        Type_Modifier = Pokemon.type_advantage(Move_Type, *Enemy_type)
        damage = round(2 * 100 / 5 + 2)
        damage = round(damage * Attack_Type_Stat * Move_Power)
        damage = round(damage / Defense)
        damage = round(damage / 50)
        damage = round(damage + 2)
        damage = round(damage * X)
        damage = round(damage * Type_Modifier / 10)
        damage = round(damage * Z)
        damage = round(damage / 255)
        return damage


# Glaceon
freeze_dry = ['Ice', 70, 'Special']
blizzard = ['Ice', 110, 'Special']
ice_shard = ['Ice', 40, 'Physical']
glaceon_moves = {'Glaceon': ['Freeze Dry', 'Blizzard', 'Ice Shard']}

# Togepi
dazzling_gleam = ['Fairy', 80, 'Special']
hidden_power_togepi = ['Fire', 60, 'Special']
psyshock = ['Psychic', 80, 'Special']
togepi_moves = {'Togepi': ['Dazzling Gleam', 'Hidden Power', 'Psyshock']}

# Beedrill
u_turn = ['Bug', 70, 'Physical']
poison_jab = ['Poison', 80, 'Physical']
drill_run = ['Ground', 80, 'Physical']
beedrill_moves = {'Beedrill': ['U-Turn', 'Poison Jab', 'Drill Run']}

# Magikarp
splash = ['Normal', 0, 'Status']
tackle = ['Normal', 40, 'Physical']
flail = ['Normal', 60, 'Physical']
magikarp_moves = {'Magikarp': ['Splash', 'Tackle', 'Flail']}

# Raichu
thunderbolt = ['Electric', 90, 'Special']
hidden_power_raichu = ['Ice', 60, 'Special']
grass_knot = ['Grass', 70, 'Special']
raichu_moves = {'Raichu': ['Thunderbolt', 'Hidden Power', 'Grass Knot']}

# Rhyhorn
earthquake = ['Ground', 100, 'Physical']
rock_blast = ['Rock', 25, 'Physical']
fire_fang = ['Fire', 65, 'Physical']
rhyhorn_moves = {'Rhyhorn': ['Earthquake', 'Rock Blast', 'Fire Fang']}

pokemon_team_chooser = input('Do you want team 1 or team 2?')
team = []
enemy_team = []
if pokemon_team_chooser == 'team 1':
    # noinspection PyTypeChecker
    team = [Pokemon.possible_pokemon['Glaceon'], Pokemon.possible_pokemon['Togepi'],
            Pokemon.possible_pokemon['Beedrill']]
    # noinspection PyTypeChecker
    enemy_team = [Pokemon.possible_pokemon['Magikarp'], Pokemon.possible_pokemon['Raichu'],
                  Pokemon.possible_pokemon['Rhyhorn']]
if pokemon_team_chooser == 'team 2':
    # noinspection PyTypeChecker
    team = [Pokemon.possible_pokemon['Magikarp'], Pokemon.possible_pokemon['Raichu'],
            Pokemon.possible_pokemon['Rhyhorn']]
    # noinspection PyTypeChecker
    enemy_team = [Pokemon.possible_pokemon['Glaceon'], Pokemon.possible_pokemon['Togepi'],
                  Pokemon.possible_pokemon['Beedrill']]

p1_chosen = input('Player 1 Choose a pokemon: \n{}\n{}\n{}'.format(team[0][0], team[1][0], team[2][0]))
p2_chosen = input('Player 2 Choose a pokemon: \n{}\n{}\n{}'.format(enemy_team[0][0],
                                                                   enemy_team[1][0], enemy_team[2][0]))
healing_items_p1 = {"Potion": 50}
healing_items_p2 = {"Potion": 50}
while len(team) > 0 and len(enemy_team) > 0:
    attack_chosen = ''
    print("Player 1's current Pokemon is at {} health.".format(Pokemon.possible_pokemon[p1_chosen][3]))
    print("Player 2's current Pokemon is at {} health.".format(Pokemon.possible_pokemon[p2_chosen][3]))
    turn_action = input('Player 1 Would you like to:\n 1. Attack\n 2. Switch Pokemon\n 3. Bag')

    if turn_action == "Attack":
        if p1_chosen == 'Glaceon':
            attack_chosen = input('Would you like to use: \n{}\n{}\n{}'.format(glaceon_moves['Glaceon'][0],
                                                                               glaceon_moves['Glaceon'][1],
                                                                               glaceon_moves['Glaceon'][2]))
            if attack_chosen == 'Freeze Dry':
                round_damage = Damage.damage_dealing(p1_chosen, p2_chosen, freeze_dry[0], freeze_dry[1], freeze_dry[2],
                                                     Pokemon.possible_pokemon[p2_chosen][1],
                                                     Pokemon.possible_pokemon[p2_chosen][2])
                Pokemon.possible_pokemon[p2_chosen][3] = Pokemon.possible_pokemon[p2_chosen][3] - round_damage
            if attack_chosen == 'Blizzard':
                round_damage = Damage.damage_dealing(p1_chosen, p2_chosen, blizzard[0], blizzard[1], blizzard[2],
                                                     Pokemon.possible_pokemon[p2_chosen][1],
                                                     Pokemon.possible_pokemon[p2_chosen][2])
                Pokemon.possible_pokemon[p2_chosen][3] = Pokemon.possible_pokemon[p2_chosen][3] - round_damage
            if attack_chosen == 'Ice Shard':
                round_damage = Damage.damage_dealing(p1_chosen, p2_chosen, ice_shard[0], ice_shard[1], ice_shard[2],
                                                     Pokemon.possible_pokemon[p2_chosen][1],
                                                     Pokemon.possible_pokemon[p2_chosen][2])
                Pokemon.possible_pokemon[p2_chosen][3] = Pokemon.possible_pokemon[p2_chosen][3] - round_damage
        if p1_chosen == 'Togepi':
            attack_chosen = input('Would you like to use: \n{}\n{}\n{}'.format(togepi_moves['Togepi'][0],
                                                                               togepi_moves['Togepi'][1],
                                                                               togepi_moves['Togepi'][2]))
            if attack_chosen == 'Dazzling Gleam':
                round_damage = Damage.damage_dealing(p1_chosen, p2_chosen, dazzling_gleam[0], dazzling_gleam[1],
                                                     dazzling_gleam[2],
                                                     Pokemon.possible_pokemon[p2_chosen][1],
                                                     Pokemon.possible_pokemon[p2_chosen][2])
                Pokemon.possible_pokemon[p2_chosen][3] = Pokemon.possible_pokemon[p2_chosen][3] - round_damage
            if attack_chosen == 'Hidden Power':
                round_damage = Damage.damage_dealing(p1_chosen, p2_chosen, hidden_power_togepi[0],
                                                     hidden_power_togepi[1], hidden_power_togepi[2],
                                                     Pokemon.possible_pokemon[p2_chosen][1],
                                                     Pokemon.possible_pokemon[p2_chosen][2])
                Pokemon.possible_pokemon[p2_chosen][3] = Pokemon.possible_pokemon[p2_chosen][3] - round_damage
            if attack_chosen == 'Psyshock':
                round_damage = Damage.damage_dealing(p1_chosen, p2_chosen, psyshock[0], psyshock[1], psyshock[2],
                                                     Pokemon.possible_pokemon[p2_chosen][1],
                                                     Pokemon.possible_pokemon[p2_chosen][2])
                Pokemon.possible_pokemon[p2_chosen][3] = Pokemon.possible_pokemon[p2_chosen][3] - round_damage
        if p1_chosen == 'Beedrill':
            attack_chosen = input('Would you like to use: \n{}\n{}\n{}'.format(beedrill_moves['Beedrill'][0],
                                                                               beedrill_moves['Beedrill'][1],
                                                                               beedrill_moves['Beedrill'][2]))
            if attack_chosen == 'U-Turn':
                round_damage = Damage.damage_dealing(p1_chosen, p2_chosen, u_turn[0], u_turn[1], u_turn[2],
                                                     Pokemon.possible_pokemon[p2_chosen][1],
                                                     Pokemon.possible_pokemon[p2_chosen][2])
                Pokemon.possible_pokemon[p2_chosen][3] = Pokemon.possible_pokemon[p2_chosen][3] - round_damage
            if attack_chosen == 'Poison Jab':
                round_damage = Damage.damage_dealing(p1_chosen, p2_chosen, poison_jab[0], poison_jab[1], poison_jab[2],
                                                     Pokemon.possible_pokemon[p2_chosen][1],
                                                     Pokemon.possible_pokemon[p2_chosen][2])
                Pokemon.possible_pokemon[p2_chosen][3] = Pokemon.possible_pokemon[p2_chosen][3] - round_damage
            if attack_chosen == 'Drill Run':
                round_damage = Damage.damage_dealing(p1_chosen, p2_chosen, drill_run[0], drill_run[1], drill_run[2],
                                                     Pokemon.possible_pokemon[p2_chosen][1],
                                                     Pokemon.possible_pokemon[p2_chosen][2])
                Pokemon.possible_pokemon[p2_chosen][3] = Pokemon.possible_pokemon[p2_chosen][3] - round_damage
        if p1_chosen == 'Magikarp':
            attack_chosen = input('Would you like to use: \n{}\n{}\n{}'.format(magikarp_moves['Magikarp'][0],
                                                                               magikarp_moves['Magikarp'][1],
                                                                               magikarp_moves['Magikarp'][2]))
            if attack_chosen == 'Splash':
                pass
            if attack_chosen == 'Tackle':
                round_damage = Damage.damage_dealing(p1_chosen, p2_chosen, tackle[0], tackle[1], tackle[2],
                                                     Pokemon.possible_pokemon[p2_chosen][1],
                                                     Pokemon.possible_pokemon[p2_chosen][2])
                Pokemon.possible_pokemon[p2_chosen][3] = Pokemon.possible_pokemon[p2_chosen][3] - round_damage
            if attack_chosen == 'Flail':
                round_damage = Damage.damage_dealing(p1_chosen, p2_chosen, flail[0], flail[1], flail[2],
                                                     Pokemon.possible_pokemon[p2_chosen][1],
                                                     Pokemon.possible_pokemon[p2_chosen][2])
                Pokemon.possible_pokemon[p2_chosen][3] = Pokemon.possible_pokemon[p2_chosen][3] - round_damage
        if p1_chosen == 'Raichu':
            attack_chosen = input('Would you like to use: \n{}\n{}\n{}'.format(raichu_moves['Raichu'][0],
                                                                               raichu_moves['Raichu'][1],
                                                                               raichu_moves['Raichu'][2]))
            if attack_chosen == 'Thunderbolt':
                round_damage = Damage.damage_dealing(p1_chosen, p2_chosen, thunderbolt[0], thunderbolt[1],
                                                     thunderbolt[2],
                                                     Pokemon.possible_pokemon[p2_chosen][1],
                                                     Pokemon.possible_pokemon[p2_chosen][2])
            if attack_chosen == 'Hidden Power':
                round_damage = Damage.damage_dealing(p1_chosen, p2_chosen, hidden_power_raichu[0],
                                                     hidden_power_raichu[1], hidden_power_raichu[2],
                                                     Pokemon.possible_pokemon[p2_chosen][1],
                                                     Pokemon.possible_pokemon[p2_chosen][2])
                Pokemon.possible_pokemon[p2_chosen][3] = Pokemon.possible_pokemon[p2_chosen][3] - round_damage
            if attack_chosen == 'Grass Knot':
                round_damage = Damage.damage_dealing(p1_chosen, p2_chosen, grass_knot[0], grass_knot[1], grass_knot[2],
                                                     Pokemon.possible_pokemon[p2_chosen][1],
                                                     Pokemon.possible_pokemon[p2_chosen][2])
                Pokemon.possible_pokemon[p2_chosen][3] = Pokemon.possible_pokemon[p2_chosen][3] - round_damage
        if p1_chosen == 'Rhyhorn':
            attack_chosen = input('Would you like to use: \n{}\n{}\n{}'.format(rhyhorn_moves['Rhyhorn'][0],
                                                                               rhyhorn_moves['Rhyhorn'][1],
                                                                               rhyhorn_moves['Rhyhorn'][2]))
            if attack_chosen == 'Earthquake':
                round_damage = Damage.damage_dealing(p1_chosen, p2_chosen, earthquake[0], earthquake[1], earthquake[2],
                                                     Pokemon.possible_pokemon[p2_chosen][1],
                                                     Pokemon.possible_pokemon[p2_chosen][2])
                Pokemon.possible_pokemon[p2_chosen][3] = Pokemon.possible_pokemon[p2_chosen][3] - round_damage
            if attack_chosen == 'Rock Blast':
                round_damage = Damage.damage_dealing(p1_chosen, p2_chosen, rock_blast[0], rock_blast[1], rock_blast[2],
                                                     Pokemon.possible_pokemon[p2_chosen][1],
                                                     Pokemon.possible_pokemon[p2_chosen][2])
                Pokemon.possible_pokemon[p2_chosen][3] = Pokemon.possible_pokemon[p2_chosen][3] - round_damage
            if attack_chosen == 'Fire Fang':
                round_damage = Damage.damage_dealing(p1_chosen, p2_chosen, fire_fang[0], fire_fang[1], fire_fang[2],
                                                     Pokemon.possible_pokemon[p2_chosen][1],
                                                     Pokemon.possible_pokemon[p2_chosen][2])
                Pokemon.possible_pokemon[p2_chosen][3] = Pokemon.possible_pokemon[p2_chosen][3] - round_damage
    if turn_action == "Switch Pokemon":
        p1_chosen = input('Player 1 Choose a pokemon: \n{}\n{}\n{}'.format(team[0][0], team[1][0], team[2][0]))

    if Pokemon.possible_pokemon[p2_chosen][3] <= 0:
        print("Player 2's {} has fainted in battle due to a fatal injury!!!".format(p2_chosen))
        # noinspection PyTypeChecker
        enemy_team.remove(Pokemon.possible_pokemon[p2_chosen])
        if len(enemy_team) == 2:
            p2_chosen = input('Player 2 Choose a pokemon: \n{}\n{}'.format(enemy_team[0][0], enemy_team[1][0]))
        if len(enemy_team) == 1:
            p2_chosen = input('Player 2 Choose a pokemon: {}'.format(enemy_team[0][0]))

    if turn_action == 'Bag':
        healing_used = input('Would you like to use a potion.')
        if len(healing_items_p1) == 0:
            print("Your have no potions available.")
        elif healing_used == 'Yes':
            Pokemon.possible_pokemon[p1_chosen][3] = Pokemon.possible_pokemon[p1_chosen][3] + healing_items_p1["Potion"]
            del healing_items_p1["Potion"]
            if Pokemon.possible_pokemon[p1_chosen][3] > Pokemon.possible_pokemon[p1_chosen][4]:
                Pokemon.possible_pokemon[p1_chosen][3] = Pokemon.possible_pokemon[p1_chosen][4]

    turn_action = input('Player 2 Would you like to:\n 1. Attack\n 2. Switch Pokemon\n 3. Bag')
    if turn_action == "Attack":
        if p2_chosen == 'Glaceon':
            attack_chosen = input('Would you like to use: \n{}\n{}\n{}'.format(glaceon_moves['Glaceon'][0],
                                                                               glaceon_moves['Glaceon'][1],
                                                                               glaceon_moves['Glaceon'][2]))
            if attack_chosen == 'Freeze Dry':
                round_damage = Damage.damage_dealing(p2_chosen, p1_chosen, freeze_dry[0], freeze_dry[1], freeze_dry[2],
                                                     Pokemon.possible_pokemon[p1_chosen][1],
                                                     Pokemon.possible_pokemon[p1_chosen][2])
                Pokemon.possible_pokemon[p1_chosen][3] = Pokemon.possible_pokemon[p1_chosen][3] - round_damage
            if attack_chosen == 'Blizzard':
                round_damage = Damage.damage_dealing(p2_chosen, p1_chosen, blizzard[0], blizzard[1], blizzard[2],
                                                     Pokemon.possible_pokemon[p1_chosen][1],
                                                     Pokemon.possible_pokemon[p1_chosen][2])
                Pokemon.possible_pokemon[p1_chosen][3] = Pokemon.possible_pokemon[p1_chosen][3] - round_damage
            if attack_chosen == 'Ice Shard':
                round_damage = Damage.damage_dealing(p2_chosen, p1_chosen, ice_shard[0], ice_shard[1], ice_shard[2],
                                                     Pokemon.possible_pokemon[p1_chosen][1],
                                                     Pokemon.possible_pokemon[p1_chosen][2])
                Pokemon.possible_pokemon[p1_chosen][3] = Pokemon.possible_pokemon[p1_chosen][3] - round_damage
        if p2_chosen == 'Togepi':
            attack_chosen = input('Would you like to use: \n{}\n{}\n{}'.format(togepi_moves['Togepi'][0],
                                                                               togepi_moves['Togepi'][1],
                                                                               togepi_moves['Togepi'][2]))
            if attack_chosen == 'Dazzling Gleam':
                round_damage = Damage.damage_dealing(p2_chosen, p1_chosen, dazzling_gleam[0], dazzling_gleam[1],
                                                     dazzling_gleam[2],
                                                     Pokemon.possible_pokemon[p1_chosen][1],
                                                     Pokemon.possible_pokemon[p1_chosen][2])
                Pokemon.possible_pokemon[p1_chosen][3] = Pokemon.possible_pokemon[p1_chosen][3] - round_damage
            if attack_chosen == 'Hidden Power':
                round_damage = Damage.damage_dealing(p2_chosen, p1_chosen, hidden_power_togepi[0],
                                                     hidden_power_togepi[1], hidden_power_togepi[2],
                                                     Pokemon.possible_pokemon[p1_chosen][1],
                                                     Pokemon.possible_pokemon[p1_chosen][2])
                Pokemon.possible_pokemon[p1_chosen][3] = Pokemon.possible_pokemon[p1_chosen][3] - round_damage
            if attack_chosen == 'Psyshock':
                round_damage = Damage.damage_dealing(p2_chosen, p1_chosen, psyshock[0], psyshock[1], psyshock[2],
                                                     Pokemon.possible_pokemon[p1_chosen][1],
                                                     Pokemon.possible_pokemon[p1_chosen][2])
                Pokemon.possible_pokemon[p1_chosen][3] = Pokemon.possible_pokemon[p1_chosen][3] - round_damage
        if p2_chosen == 'Beedrill':
            attack_chosen = input('Would you like to use: \n{}\n{}\n{}'.format(beedrill_moves['Beedrill'][0],
                                                                               beedrill_moves['Beedrill'][1],
                                                                               beedrill_moves['Beedrill'][2]))
            if attack_chosen == 'U-Turn':
                round_damage = Damage.damage_dealing(p2_chosen, p1_chosen, u_turn[0], u_turn[1], u_turn[2],
                                                     Pokemon.possible_pokemon[p1_chosen][1],
                                                     Pokemon.possible_pokemon[p1_chosen][2])
                Pokemon.possible_pokemon[p1_chosen][3] = Pokemon.possible_pokemon[p1_chosen][3] - round_damage
            if attack_chosen == 'Poison Jab':
                round_damage = Damage.damage_dealing(p2_chosen, p1_chosen, poison_jab[0], poison_jab[1], poison_jab[2],
                                                     Pokemon.possible_pokemon[p1_chosen][1],
                                                     Pokemon.possible_pokemon[p1_chosen][2])
                Pokemon.possible_pokemon[p1_chosen][3] = Pokemon.possible_pokemon[p1_chosen][3] - round_damage
            if attack_chosen == 'Drill Run':
                round_damage = Damage.damage_dealing(p2_chosen, p1_chosen, drill_run[0], drill_run[1], drill_run[2],
                                                     Pokemon.possible_pokemon[p1_chosen][1],
                                                     Pokemon.possible_pokemon[p1_chosen][2])
                Pokemon.possible_pokemon[p1_chosen][3] = Pokemon.possible_pokemon[p1_chosen][3] - round_damage
        if p2_chosen == 'Magikarp':
            attack_chosen = input('Would you like to use: \n{}\n{}\n{}'.format(magikarp_moves['Magikarp'][0],
                                                                               magikarp_moves['Magikarp'][1],
                                                                               magikarp_moves['Magikarp'][2]))
            if attack_chosen == 'Splash':
                pass
            if attack_chosen == 'Tackle':
                round_damage = Damage.damage_dealing(p2_chosen, p1_chosen, tackle[0], tackle[1], tackle[2],
                                                     Pokemon.possible_pokemon[p1_chosen][1],
                                                     Pokemon.possible_pokemon[p1_chosen][2])
                Pokemon.possible_pokemon[p1_chosen][3] = Pokemon.possible_pokemon[p1_chosen][3] - round_damage
            if attack_chosen == 'Flail':
                round_damage = Damage.damage_dealing(p2_chosen, p1_chosen, flail[0], flail[1], flail[2],
                                                     Pokemon.possible_pokemon[p1_chosen][1],
                                                     Pokemon.possible_pokemon[p1_chosen][2])
                Pokemon.possible_pokemon[p1_chosen][3] = Pokemon.possible_pokemon[p1_chosen][3] - round_damage
        if p2_chosen == 'Raichu':
            attack_chosen = input('Would you like to use: \n{}\n{}\n{}'.format(raichu_moves['Raichu'][0],
                                                                               raichu_moves['Raichu'][1],
                                                                               raichu_moves['Raichu'][2]))
            if attack_chosen == 'Thunderbolt':
                round_damage = Damage.damage_dealing(p2_chosen, p1_chosen, thunderbolt[0], thunderbolt[1],
                                                     thunderbolt[2],
                                                     Pokemon.possible_pokemon[p1_chosen][1],
                                                     Pokemon.possible_pokemon[p1_chosen][2])
                Pokemon.possible_pokemon[p1_chosen][3] = Pokemon.possible_pokemon[p1_chosen][3] - round_damage
            if attack_chosen == 'Hidden Power':
                round_damage = Damage.damage_dealing(p2_chosen, p1_chosen, hidden_power_raichu[0],
                                                     hidden_power_raichu[1], hidden_power_raichu[2],
                                                     Pokemon.possible_pokemon[p1_chosen][1],
                                                     Pokemon.possible_pokemon[p1_chosen][2])
                Pokemon.possible_pokemon[p1_chosen][3] = Pokemon.possible_pokemon[p1_chosen][3] - round_damage
            if attack_chosen == 'Grass Knot':
                round_damage = Damage.damage_dealing(p2_chosen, p1_chosen, grass_knot[0], grass_knot[1], grass_knot[2],
                                                     Pokemon.possible_pokemon[p1_chosen][1],
                                                     Pokemon.possible_pokemon[p1_chosen][2])
                Pokemon.possible_pokemon[p1_chosen][3] = Pokemon.possible_pokemon[p1_chosen][3] - round_damage
        if p2_chosen == 'Rhyhorn':
            attack_chosen = input('Would you like to use: \n{}\n{}\n{}'.format(rhyhorn_moves['Rhyhorn'][0],
                                                                               rhyhorn_moves['Rhyhorn'][1],
                                                                               rhyhorn_moves['Rhyhorn'][2]))
            if attack_chosen == 'Earthquake':
                round_damage = Damage.damage_dealing(p2_chosen, p1_chosen, earthquake[0], earthquake[1], earthquake[2],
                                                     Pokemon.possible_pokemon[p1_chosen][1],
                                                     Pokemon.possible_pokemon[p1_chosen][2])
                Pokemon.possible_pokemon[p1_chosen][3] = Pokemon.possible_pokemon[p1_chosen][3] - round_damage
            if attack_chosen == 'Rock Blast':
                round_damage = Damage.damage_dealing(p1_chosen, p2_chosen, rock_blast[0], rock_blast[1], rock_blast[2],
                                                     Pokemon.possible_pokemon[p2_chosen][1],
                                                     Pokemon.possible_pokemon[p2_chosen][2])
                Pokemon.possible_pokemon[p1_chosen][3] = Pokemon.possible_pokemon[p1_chosen][3] - round_damage
            if attack_chosen == 'Fire Fang':
                round_damage = Damage.damage_dealing(p2_chosen, p1_chosen, fire_fang[0], fire_fang[1], fire_fang[2],
                                                     Pokemon.possible_pokemon[p1_chosen][1],
                                                     Pokemon.possible_pokemon[p1_chosen][2])
                Pokemon.possible_pokemon[p1_chosen][3] = Pokemon.possible_pokemon[p1_chosen][3] - round_damage

    if turn_action == "Switch Pokemon":
        p2_chosen = input('Player 2 Choose a pokemon: \n{}\n{}\n{}'.format(enemy_team[0][0], enemy_team[1][0],
                                                                           enemy_team[2][0]))

    if Pokemon.possible_pokemon[p1_chosen][3] <= 0:
        print("Player 1's {} has fainted in battle due to a fatal injury!!!".format(p2_chosen))
        # noinspection PyTypeChecker
        team.remove(Pokemon.possible_pokemon[p1_chosen])
        if len(team) == 2:
            p2_chosen = input('Player 2 Choose a pokemon: \n{}\n{}'.format(team[0][0], team[1][0]))
        if len(team) == 1:
            p2_chosen = input('Player 2 Choose a pokemon: {}'.format(team[0][0]))

    if turn_action == 'Bag':
        healing_used = input('Would you like to use a potion.')
        if len(healing_items_p2) == 0:
            print("Your have no potions available.")
        elif healing_used == 'Yes':
            Pokemon.possible_pokemon[p2_chosen][3] = Pokemon.possible_pokemon[p2_chosen][3] + healing_items_p2["Potion"]
            del healing_items_p2["Potion"]
            if Pokemon.possible_pokemon[p2_chosen][3] > Pokemon.possible_pokemon[p2_chosen][4]:
                Pokemon.possible_pokemon[p2_chosen][3] = Pokemon.possible_pokemon[p2_chosen][4]
