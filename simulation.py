from individual import Individual
from individual import birth_new_individuals
from group import Group
import matplotlib.pyplot as plt




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
