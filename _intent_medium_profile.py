import os

# Definizione delle combinazioni specifiche richieste
configurations = [
    {'nozzle': '0.6', 'profile': 'standard', 'layer': '0.3'},
    {'nozzle': '0.8', 'profile': 'draft', 'layer': '0.45'},
    {'nozzle': '1.0', 'profile': 'superdraft', 'layer': '0.6'},
    {'nozzle': '1.2', 'profile': 'fast', 'layer': '0.75'}
]

materials = ['PETG', 'PLA', 'GFF', 'CFF', 'TPU']
intents = ['fast', 'supporto_graduale', 'supporto', 'visual']

# Funzione per generare il contenuto del file di configurazione per gli intent
def generate_specific_intent_config_content(nozzle, material, profile, layer, intent):
    intent_category = intent.replace('_', ' ')
    content = f"""[general]
version = 4
name = {intent_category.capitalize()}
definition = fabbrix_elemento_tc

[metadata]
setting_version = 20
type = intent
intent_category = {intent_category}
quality_type = {profile}
material = fabbrix_{material.lower()}
variant = {nozzle}mm Nozzle

[values]
"""
    return content

# Creazione della directory per salvare i file
os.makedirs('specific_intent_config_files', exist_ok=True)

# Generazione dei file specifici
for config in configurations:
    nozzle = config['nozzle']
    profile = config['profile']
    layer = config['layer']
    for material in materials:
        for intent in intents:
            filename = f"fabbrix_elemento_tc_{nozzle}_tc_{material}_{profile}_{intent}.inst.cfg"
            content = generate_specific_intent_config_content(nozzle, material, profile, layer, intent)
            filepath = os.path.join('specific_intent_config_files', filename)
            with open(filepath, 'w') as file:
                file.write(content)

# Lista dei file generati
print(os.listdir('specific_intent_config_files'))
