import random


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




