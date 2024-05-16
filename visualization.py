
## ESTA É UMA VERSÃO SIMPLIFICADA DO VISUALIZADOR DE SIMULAÇÃO

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


