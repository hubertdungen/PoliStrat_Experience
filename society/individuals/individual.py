import random
from society.groups.group import groups


class Individual:
    def __init__(self, id, basic_needs, culture, health, personality, experience, wisdom, personal_views, ideology, mood):
        self.id = id
        self.basic_needs = basic_needs
        self.culture = culture
        self.health = health
        self.personality = personality
        self.experience = experience
        self.wisdom = wisdom
        self.personal_views = personal_views
        self.ideology = ideology  # Agora é uma tupla (eixo_social, eixo_economico)
        self.mood = mood
        self.connections = []
        self.vida = random.uniform(0.5, 1.0)  # Vida inicial entre 0.5 e 1.0
        self.ataque = random.uniform(0.1, 0.5)  # Ataque inicial entre 0.1 e 0.3
        self.group = None
        self.mental_health = random.uniform(0, 1)  # Saúde mental inicial entre 0 e 1
        self.anger = random.uniform(0, 1)  # Raiva inicial entre 0 e 1
        self.age = 0  # Idade inicial
        self.lifespan = random.randint(20, 40)  # Tempo de vida entre 20 a 40 frames


    def interact(self, other):
        self.basic_needs = (self.basic_needs + other.basic_needs) / 2
        self.culture = (self.culture + other.culture) / 2
        self.health = (self.health + other.health) / 2
        self.personality = (self.personality + other.personality) / 2
        self.experience = (self.experience + other.experience) / 2
        self.wisdom = (self.wisdom + other.wisdom) / 2
        self.personal_views = (self.personal_views + other.personal_views) / 2
        self.ideology = ((self.ideology[0] + other.ideology[0]) / 2, (self.ideology[1] + other.ideology[1]) / 2)
        self.mood = (self.mood + other.mood) / 2

        if other not in self.connections:
            self.connections.append(other)
        if self not in other.connections:
            other.connections.append(self)

    def increment_age_and_check_lifespan(self):
        self.age += 1
        if self.age >= self.lifespan:
            return False  # O indivíduo morreu
        return True  # O indivíduo continua vivo

    def update_variables(self):
        self.update_mood()
        self.limit_mood()
        self.update_basic_needs()
        self.update_culture()
        self.update_health()
        self.update_personality()
        self.update_experience()
        self.update_wisdom()
        self.update_personal_views()
        self.update_ideology()

        # Ajustar a saúde mental e verificar "Mental Break"
        if self.group:
            current_group = next((group for group in groups if group.id == self.group), None)
            if current_group:
                current_group_size = len(current_group.members)
                max_group_size = max(len(group.members) for group in groups)
                if max_group_size > current_group_size * 2:  # Grupo muito maior
                    self.mental_health -= 0.05
                    if self.mental_health < 0.2:  # Saúde mental muito baixa
                        self.group = "MentalBrake"
                else:
                    self.mental_health = min(self.mental_health + 0.01, 1.0)  # Recuperar um pouco

        # Ajustar a raiva
        if self.mental_health < 0.4:
            self.anger = min(self.anger + 0.05, 1.0)  # Saúde mental baixa aumenta a raiva moderadamente
        elif self.mental_health > 0.7:
            self.anger = max(self.anger - 0.03, 0)  # Saúde mental alta diminui pouco a raiva

        # Ajustar a saúde mental com base na saúde (HP)
        if self.vida < 0.5:
            self.mental_health = max(self.health - 0.02, 0)
        elif self.vida > 0.85:
            self.mental_health = max(self.health + 0.015, 1.0)
            

        if self.group:
            current_group = next((group for group in groups if group.id == self.group), None)
            if current_group:
                group_members = current_group.members
                different_ideologies = sum(1 for member in group_members if abs(member.ideology[0] - self.ideology[0]) > 0.2 or abs(member.ideology[1] - self.ideology[1]) > 0.2)
                small_groups_count = sum(1 for group in groups if len(group.members) < 3)
                self.anger += 0.005 * different_ideologies + 0.01 * small_groups_count
                self.anger = min(self.anger, 1.0)

    def limit_mood(self):
        if self.mood < 0:
            self.mood = 0
        elif self.mood > 1:
            self.mood = 1


    def update_mood(self):
        # Pesos para cada variável
        weight_health = 0.3
        weight_experience = 0.2
        weight_wisdom = 0.2
        weight_basic_needs = 0.2
        weight_random = 0.1

        self.mood = (
            self.health * weight_health +
            self.experience * weight_experience +
            self.wisdom * weight_wisdom +
            self.basic_needs * weight_basic_needs +
            random.uniform(-0.1, 0.1) * weight_random
        )
        self.mood = max(0, min(self.mood, 1))  # Limitar o valor de mood entre 0 e 1


    def limit_mood(self):
            if self.mood < 0:
                self.mood = 0
            elif self.mood > 1:
                self.mood = 1

    def update_basic_needs(self):
        self.basic_needs = (self.health + self.experience + random.uniform(-0.1, 0.1)) / 3

    def update_culture(self):
        self.culture = (self.experience + self.wisdom + random.uniform(-0.1, 0.1)) / 3

    def update_health(self):
        self.health = (self.basic_needs + self.mood + random.uniform(-0.1, 0.1)) / 3

    def update_personality(self):
        self.personality = (self.wisdom + self.personal_views + random.uniform(-0.1, 0.1)) / 3

    def update_experience(self):
        self.experience += random.uniform(0, 0.1)

    def update_wisdom(self):
        self.wisdom = (self.experience + self.health + random.uniform(-0.1, 0.1)) / 3

    def update_personal_views(self):
        self.personal_views = (self.ideology[0] + self.ideology[1] + self.culture + random.uniform(-0.1, 0.1)) / 4

    def update_ideology(self):
        self.ideology = ((self.personality + self.personal_views + random.uniform(-0.1, 0.1)) / 2, 
                         (self.personality + self.personal_views + random.uniform(-0.1, 0.1)) / 2)
        
    def perform_action(self, groups):
        action = "Neutral"
        detailed_action = ""

        if self.mood > 0.7:
            if self.mental_health > 0.6 and self.anger < 0.4:
                action = "Colaborar"
                detailed_action = "Ajuda os outros no grupo e tenta melhorar a situação coletiva."
            elif self.mental_health <= 0.6:
                action = "Isolar"
                detailed_action = "Prefere ficar sozinho devido à baixa saúde mental."
        elif self.mood < 0.3:
            if self.anger > 0.6:
                action = "Conflitar"
                detailed_action = "Provoca conflitos com outros devido à alta raiva."
            elif self.mental_health < 0.4:
                action = "Isolar"
                detailed_action = "Se isola devido à baixa saúde mental."
            else:
                action = "Conflitar"
                detailed_action = "Causa discórdias mesmo com raiva moderada."
        else:
            if self.mental_health > 0.7 and self.anger < 0.3:
                action = "Colaborar"
                detailed_action = "Ajuda os outros, mantendo um comportamento positivo."
            elif self.anger > 0.5:
                action = "Conflitar"
                detailed_action = "Cria pequenas disputas devido à alta raiva."

        if self.group:
            for group in groups:
                if group.id == self.group:
                    if action == "Colaborar":
                        group.group_opinion = (group.group_opinion[0] + 0.1, group.group_opinion[1] + 0.1)
                    elif action == "Conflitar":
                        group.group_opinion = (group.group_opinion[0] - 0.1, group.group_opinion[1] - 0.1)

        return action, detailed_action

    def update_variables(self):
        self.update_mood()
        self.limit_mood()
        self.update_basic_needs()
        self.update_culture()
        self.update_health()
        self.update_personality()
        self.update_experience()
        self.update_wisdom()
        self.update_personal_views()
        self.update_ideology()

        # Ajustar a saúde mental e verificar "Mental Break"
        if self.group:
            current_group = next((group for group in groups if group.id == self.group), None)
            if current_group:
                current_group_size = len(current_group.members)
                max_group_size = max(len(group.members) for group in groups)
                if max_group_size > current_group_size * 2:  # Grupo muito maior
                    self.mental_health -= 0.05
                    if self.mental_health < 0.2:  # Saúde mental muito baixa
                        self.group = "MentalBrake"
                else:
                    self.mental_health = min(self.mental_health + 0.01, 1.0)  # Recuperar um pouco

        # Ajustar a raiva
        if self.mental_health < 0.4:
            self.anger = min(self.anger + 0.1, 1.0)  # Saúde mental baixa aumenta bastante a raiva
        elif self.mental_health > 0.7:
            self.anger = max(self.anger - 0.02, 0)  # Saúde mental alta diminui pouco a raiva

        # Ajustar a saúde mental com base na saúde (HP)
        if self.vida < 0.5:
            self.mental_health = max(self.mental_health - 0.05, 0)

        if self.group:
            current_group = next((group for group in groups if group.id == self.group), None)
            if current_group:
                group_members = current_group.members
                different_ideologies = sum(1 for member in group_members if abs(member.ideology[0] - self.ideology[0]) > 0.2 or abs(member.ideology[1] - self.ideology[1]) > 0.2)
                small_groups_count = sum(1 for group in groups if len(group.members) < 3)
                self.anger += 0.01 * different_ideologies + 0.02 * small_groups_count
                self.anger = min(self.anger, 1.0)

    def evaluate_membership(self, groups):
        if self.group is not None:
            current_group = next((group for group in groups if group.id == self.group), None)
            if current_group:
                if abs(self.ideology[0] - current_group.group_opinion[0]) > 0.2 or abs(self.ideology[1] - current_group.group_opinion[1]) > 0.2:
                    self.group = None  # Sair do grupo atual
                    if self in current_group.members:
                        current_group.members.remove(self)




    def limit_mood(self):
        if self.mood < 0:
            self.mood = 0
        elif self.mood > 1:
            self.mood = 1

    def update_basic_needs(self):
        self.basic_needs = (self.health + self.experience + random.uniform(-0.1, 0.1)) / 3

    def update_culture(self):
        self.culture = (self.experience + self.wisdom + random.uniform(-0.1, 0.1)) / 3

    def update_health(self):
        self.health = (self.basic_needs + self.mood + random.uniform(-0.1, 0.1)) / 3

    def update_personality(self):
        self.personality = (self.wisdom + self.personal_views + random.uniform(-0.1, 0.1)) / 3

    def update_experience(self):
        self.experience += random.uniform(0, 0.1)

    def update_wisdom(self):
        self.wisdom = (self.experience + self.health + random.uniform(-0.1, 0.1)) / 3

    def update_personal_views(self):
        self.personal_views = (self.ideology[0] + self.ideology[1] + self.culture + random.uniform(-0.1, 0.1)) / 4

    def update_ideology(self):
        self.ideology = ((self.personality + self.personal_views + random.uniform(-0.1, 0.1)) / 2, 
                         (self.personality + self.personal_views + random.uniform(-0.1, 0.1)) / 2)


    def __str__(self):
        group_str = self.group if self.group != "MentalBrake" else "MentalBrake"
        return (f"Individual {self.id} - Mood: {self.mood:.2f}, Ideology: {self.ideology}, Group: {group_str}, "
               f"HP: {self.vida:.2f}, ATK: {self.ataque:.2f}, Mental Health: {self.mental_health:.2f}, Anger: {self.anger:.2f}")



def birth_new_individuals(population, max_individuals):
    if len(population) < max_individuals:
        if random.random() < 0.1:  # Adicionar controle de taxa (10% de chance de nascer um novo indivíduo por frame)
            new_id = max(ind.id for ind in population) + 1 if population else 0
            new_individual = Individual(
                id=new_id,
                basic_needs=random.uniform(0, 1),
                culture=random.uniform(0, 1),
                health=random.uniform(0, 1),
                personality=random.uniform(0, 1),
                experience=random.uniform(0, 1),
                wisdom=random.uniform(0, 1),
                personal_views=random.uniform(0, 1),
                ideology=(random.uniform(0, 1), random.uniform(0, 1)),
                mood=random.uniform(0, 1)
            )
            new_individual.mental_health = random.uniform(0, 1)
            new_individual.anger = random.uniform(0, 1)
            new_individual.age = 0  # Idade inicial
            new_individual.lifespan = random.randint(20, 60)  # Tempo de vida entre 20 a 40 frames
            population.append(new_individual)

