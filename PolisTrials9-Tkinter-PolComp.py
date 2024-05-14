import networkx as nx
import random
from itertools import combinations

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


"""
Programa e simulador visual em python que representa/executa a interação entre individuos que conta com as variáveis de interação AI de individuos (ADN, Personalidade, Experiencia, Ideologia, Opiniões, Cultura, Factores Externos, Saúde, Sabedoria e Mood) - sendo que cada variavel influenciam-se umas às outras - e que faz outputs nas ações, opiniões e nos resultados dos grupos e comunidades.
Os individuos poderão por vontade própria fundar grupos de variados viés, poderão formar governos, ideologias diferentes, lutar entre si, falar, interagir, e ter opiniões diferentes entre si.
"""
import tkinter as tk
import random
import time
from itertools import combinations

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
        self.ataque = random.uniform(0.1, 0.3)  # Ataque inicial entre 0.1 e 0.3
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

class Group:
    def __init__(self, id):
        self.id = id
        self.members = []
        self.defense = 0  # Inicializar o atributo defense
        self.group_opinion = (0, 0)  # Adiciona o atributo group_opinion como uma tupla (social, economico)

    def add_member(self, individual):
        if individual not in self.members:
            self.members.append(individual)
            individual.group = self.id

    def update_group_opinion(self):
        if self.members:
            self.group_opinion = (
                sum(member.ideology[0] for member in self.members) / len(self.members),
                sum(member.ideology[1] for member in self.members) / len(self.members)
            )
            self.defense = sum(member.vida for member in self.members) / len(self.members)  # Média da vida como defesa

    def perform_group_action(self, other_groups):
        action = "Manter"
        action_log = ""

        if self.members:
            average_mental_health = sum(member.mental_health for member in self.members) / len(self.members)
            average_anger = sum(member.anger for member in self.members) / len(self.members)
            average_vida = sum(member.vida for member in self.members) / len(self.members)
        else:
            average_mental_health = 1.0
            average_anger = 0.0
            average_vida = 1.0

        is_larger_group = all(len(self.members) > len(other.members) for other in other_groups)

        if random.random() < 0.5 and average_mental_health > 0.4 and average_anger < 0.9:  # Aumentar a probabilidade de expansão
            action = "Expandir"
            # Melhora o humor dos membros
            for member in self.members:
                member.mood = min(member.mood + 0.1, 1.0)
            # Aumenta a influência da opinião do grupo sobre seus membros
            for member in self.members:
                member.ideology = (
                    (member.ideology[0] + self.group_opinion[0]) / 2,
                    (member.ideology[1] + self.group_opinion[1]) / 2
                )
            # Pode atrair membros de outros grupos com ideologias próximas
            for other in other_groups:
                if other != self and len(other.members) > 0:
                    for member in other.members[:]:
                        if abs(member.ideology[0] - self.group_opinion[0]) < 0.1 and abs(member.ideology[1] - self.group_opinion[1]) < 0.1:
                            other.members.remove(member)
                            self.add_member(member)
                            action_log += f"Member {member.id} joined Group {self.id} from Group {other.id}\n"

        if random.random() < 0.4 and is_larger_group or random.random() < 0.5 and average_anger > 0.6 or random.random() < 0.3 and average_mental_health < 0.2:  # Aumentar a probabilidade de ataque
            for other in other_groups:
                if self != other and abs(self.group_opinion[0] - other.group_opinion[0]) > 0.3:
                    action = "Atacar"
                    damage = sum(member.ataque for member in self.members)
                    total_defense = (sum(member.vida for member in other.members) + self.defense) / 2 
                    
                    # Calcular a probabilidade de falha do ataque
                    defense_prob = min(total_defense * 0.9, 0.9)
                    attack_prob = 1 - defense_prob
                    attack_success_chance = 1 / (damage * attack_prob)  # Chance de sucesso (inversamente proporcional ao dano e à defesa)
                    action_log += f"Group {self.id} attacking Group {other.id} with {attack_success_chance:.2f} chance of success\n"

                    if random.random() > attack_success_chance:
                        for member in self.members:
                            member.mood = max(member.mood - 0.2, 0.0)  # Reduz o humor dos membros atacantes
                        action_log += f"Group {self.id} attacked Group {other.id} but failed, defense was too high\n"
                    else:
                        for member in other.members[:]:
                            member.vida -= damage / len(other.members)
                            if member.vida <= 0:
                                other.members.remove(member)
                                action_log += f"Member {member.id} from Group {other.id} died in attack\n"
                        # Mudanças na opinião do grupo atacado devido ao ataque
                        other.update_group_opinion()
                        # Aumentar a saúde mental e vida dos atacantes em caso de ataque bem-sucedido
                        for member in self.members:
                            member.mental_health = min(member.mental_health + 0.05, 1.0)
                            member.vida = min(member.vida + 0.1, 1.0)

        # Adicionar lógica para a ação "Isolar"
        if random.random() < 0.3 and (average_mental_health < 0.4 and average_anger > 0.5) or is_larger_group:
            action = "Isolar"
            self.defense *= 1.2  # Aumentar defesa em 20%
            # Reduz a chance de ataques, mas também pode reduzir o humor dos membros devido ao isolamento
            for member in self.members:
                member.mood = max(member.mood - 0.1, 0.0)
            action_log += f"Group {self.id} is isolating, defense increased to {self.defense:.2f}\n"

        return action, action_log


    def __str__(self):
        return f"Group {self.id} with members: {[member.id for member in self.members]}"

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



def create_political_compass_plot(groups):
    fig, ax = plt.subplots()
    for group in groups:
        if len(group.members) > 0:  # Apenas plote grupos com membros
            ax.scatter(group.group_opinion[0], group.group_opinion[1], label=f'Group {group.id}')
    
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(color='gray', linestyle='--', linewidth=0.5)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel('Eixo Social')
    ax.set_ylabel('Eixo Econômico')
    ax.set_title('Compasso Político 2D dos Grupos')
    ax.legend()
    
    return fig



def run_simulation_step(population, groups):
    for individual in population[:]:
        individual.update_variables()
        individual.update_mood()
        individual.perform_action(groups)
        if not individual.increment_age_and_check_lifespan():
            population.remove(individual)
            group = next((group for group in groups if group.id == individual.group), None)
            if group:
                group.members.remove(individual)
    for group in groups:
        group.update_group_opinion()
    birth_new_individuals(population, max_individuals=15)

def extinguish_empty_groups(groups):
    for group in groups[:]:
        if len(group.members) == 0:
            groups.remove(group)

def resolve_group_actions(groups):
    actions_log = []
    for group in groups:
        action, action_log = group.perform_group_action(groups)
        actions_log.append(f"Group {group.id} action: {action}")
        actions_log.append(action_log)
    return actions_log


def move_individuals(population, groups):
    max_groups = len(population) // 2
    for individual in population:
        if individual.group is None:
            for group in groups:
                if abs(individual.ideology[0] - group.group_opinion[0]) < 0.2 and abs(individual.ideology[1] - group.group_opinion[1]) < 0.2:
                    group.add_member(individual)
                    break
            else:
                if len(groups) < max_groups:
                    similar_individuals = [ind for ind in population if ind.group is None and abs(ind.ideology[0] - individual.ideology[0]) < 0.2 and abs(ind.ideology[1] - individual.ideology[1]) < 0.2]
                    if len(similar_individuals) >= 2:
                        new_group = Group(len(groups) + 1)
                        for ind in similar_individuals[:2]:  # Adiciona os dois primeiros indivíduos semelhantes
                            new_group.add_member(ind)
                            population.remove(ind)
                        groups.append(new_group)


def print_simulation_state(population, groups, actions_log):
    text_output = "\nIndivíduos:\n"
    for individual in population:
        group_str = individual.group if individual.group != "MentalBrake" else "MentalBrake"
        text_output += (f"Individual {individual.id} - Mood: {individual.mood:.2f}, Ideology: {individual.ideology}, "
                        f"Group: {group_str} - HP: {individual.vida:.2f}, ATK: {individual.ataque:.2f}, "
                        f"Mental Health: {individual.mental_health:.2f}, Anger: {individual.anger:.2f}, "
                        f"Age: {individual.age}, Lifespan: {individual.lifespan}\n")

    text_output += "\nGrupos:\n"
    for group in groups:
        if len(group.members) > 0:  # Mostrar apenas grupos com membros
            text_output += f"Group {group.id}: Opinião {group.group_opinion}\n"
            text_output += f"Membros: {[member.id for member in group.members]}\n"
            text_output += f"HP Total: {sum(member.vida for member in group.members):.2f}, Defesa: {group.defense:.2f}, Ataque Total: {sum(member.ataque for member in group.members):.2f}\n"

    avg_mood = sum(ind.mood for ind in population) / len(population)
    avg_mental_health = sum(ind.mental_health for ind in population) / len(population)
    avg_anger = sum(ind.anger for ind in population) / len(population)
    avg_ideology_social = sum(ind.ideology[0] for ind in population) / len(population)
    avg_ideology_economic = sum(ind.ideology[1] for ind in population) / len(population)
    text_output += "\nEstatísticas Gerais:\n"
    text_output += f"Média de Humor: {avg_mood:.2f}\n"
    text_output += f"Média de Saúde Mental: {avg_mental_health:.2f}\n"
    text_output += f"Média de Raiva: {avg_anger:.2f}\n"
    text_output += f"Média de Ideologia (Social): {avg_ideology_social:.2f}\n"
    text_output += f"Média de Ideologia (Econômico): {avg_ideology_economic:.2f}\n"

    text_output += "\nAções dos Grupos:\n"
    for action in actions_log:
        text_output += action + "\n"
    
    return text_output









# Inicializar a população com 6 indivíduos
population = []
initial_population = 6
max_individuals = 15

for i in range(initial_population):
    individual = Individual(
        id=i,
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
    population.append(individual)

# Simular interações
for ind1, ind2 in combinations(population, 2):
    ind1.interact(ind2)

# Formar grupos baseados na similaridade de ideologias
group_id = 1
groups = []
group_membership = {}

for ind in population:
    assigned_to_group = False
    for group in groups:
        if abs(ind.ideology[0] - group.group_opinion[0]) < 0.2 and abs(ind.ideology[1] - group.group_opinion[1]) < 0.2:
            group.add_member(ind)
            group_membership[ind.id] = group.id
            assigned_to_group = True
            break
    if not assigned_to_group:
        new_group = Group(group_id)
        new_group.add_member(ind)
        group_membership[ind.id] = group_id
        groups.append(new_group)
        group_id += 1


# Função de atualização para a interface gráfica
def update_simulation():
    run_simulation_step(population, groups)
    
    # Nascimento de novos indivíduos
    birth_new_individuals(population, max_individuals=15)

    # Avaliar a pertinência dos indivíduos em seus grupos atuais
    for individual in population:
        individual.evaluate_membership(groups)
    
    # Mover indivíduos entre grupos
    move_individuals(population, groups)

    # Extinguir grupos vazios
    extinguish_empty_groups(groups)

    actions_log = resolve_group_actions(groups)
    simulation_state = print_simulation_state(population, groups, actions_log)
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, simulation_state)
    
    # Atualizar o gráfico do compasso político
    fig = create_political_compass_plot(groups)
    canvas.figure = fig
    canvas.draw()
    
    # Atualizar novamente após 1 segundo
    root.after(1000, update_simulation)

# Configurar a interface gráfica
root = tk.Tk()
root.title("Simulação de Individuos e Grupos")

text_widget = tk.Text(root, wrap="word", height=40, width=100)
text_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Iniciar a simulação
fig = create_political_compass_plot(groups)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

update_simulation()

# Iniciar a interface gráfica
root.mainloop()

