import os

# Definizione dei parametri
nozzles = ['0.6', '0.8', '1.0', '1.2']
materials = ['PETG', 'PLA', 'GFF', 'CFF', 'TPU']
profiles = [('standard', '0.3'), ('draft', '0.45'), ('superdraft', '0.6'), ('fast', '0.75')]
intents = ['fast', 'supporto_graduale', 'supporto', 'visual']

# Funzione per generare il contenuto del file di configurazione per gli intent
def generate_intent_config_content(nozzle, material, profile_name, profile_layer_height, intent):
    intent_category = intent.replace('_', ' ')
    content = f"""[general]
version = 4
name = {intent_category.capitalize()}
definition = fabbrix_elemento_tc

[metadata]
setting_version = 20
type = intent
intent_category = {intent_category}
quality_type = {profile_name}
material = fabbrix_{material.lower()}
variant = {nozzle}mm Nozzle

[values]
"""
    return content

# Creazione della directory per salvare i file
os.makedirs('intent_config_files', exist_ok=True)

# Generazione dei file
for nozzle in nozzles:
    for material in materials:
        for profile_name, profile_layer_height in profiles:
            for intent in intents:
                filename = f"fabbrix_elemento_tc_{nozzle}_tc_{material}_{profile_name}_{intent}.inst.cfg"
                content = generate_intent_config_content(nozzle, material, profile_name, profile_layer_height, intent)
                filepath = os.path.join('intent_config_files', filename)
                with open(filepath, 'w') as file:
                    file.write(content)

# Lista dei file generati
print(os.listdir('intent_config_files')[:10])  # Mostra solo i primi 10 per brevità
