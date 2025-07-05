import os
import math

# Definizione delle combinazioni specifiche richieste
configurations = [
    {'nozzle': '0.6', 'profile': 'standard', 'layer': '0.3'},
    {'nozzle': '0.8', 'profile': 'draft', 'layer': '0.45'},
    {'nozzle': '1.0', 'profile': 'superdraft', 'layer': '0.6'},
    {'nozzle': '1.2', 'profile': 'fast', 'layer': '0.75'}
]

materials = ['PETG', 'PLA', 'GFF', 'CFF', 'TPU']
intents = ['fast', 'supporto_graduale', 'supporto', 'visual']

# Valori specifici per ogni intento
intent_values = {
    'fast': {
        'line_width': '0.55',
        'skin_line_width': '0.5',
        'bottom_layers': '6',
        'top_bottom_pattern': 'zigzag',
        'top_layers': '6',
        'initial_layer_line_width_factor': '100',
        'cool_fan_speed': '25',
        'fill_perimeter_gaps': 'nowhere',
        'retract_at_layer_change': 'True',
        'retraction_extrusion_window': '0.6',
        'retraction_min_travel': '1.2',
        'retraction_prime_speed': '15',
        'retraction_retract_speed': '15',
        'meshfix_fluid_motion_enabled': 'False',
        'wall_line_count': '2',
        'wall_0_wipe_dist': '0',
        'skin_outline_count': '0',
        'skin_overlap': '50',
        'skin_preshrink': '2.2',
        'skirt_line_count': '0',
        'z_seam_corner': 'z_seam_corner_outer',
        'speed_print': '250',
        'speed_layer_0': '35',
        'speed_topbottom': '=math.ceil(speed_print * 30 / 60)',
        'speed_wall': '=math.ceil(speed_print * 30 / 60)',
        'speed_wall_x': '=math.ceil(speed_print * 42 / 60)',
        'speed_travel': '300',
        'speed_travel_layer_0': '100',
        'switch_extruder_retraction_amount': '3',
        'switch_extruder_retraction_speeds': '25',
        'prime_tower_min_volume': '12',
        'zig_zaggify_infill': 'True',
        'zig_zaggify_support': 'True',
        'jerk_print': '10',
        'jerk_travel': '20',
        'jerk_wall_x': '10',
        'acceleration_print': '10000',
        'acceleration_topbottom': '10000',
        'acceleration_travel': '12000',
        'acceleration_wall_0': '10000',
        'acceleration_wall_x': '10000',
        'infill_material_flow': '100',
        'infill_overlap': '-10',
        'infill_pattern': 'cubic',
        'infill_randomize_start_location': 'True',
        'infill_sparse_density': '10',
        'infill_wipe_dist': '0.0',
        'inset_direction': 'inside_in',
        'meshfix_maximum_deviation': '0.025',
        'meshfix_maximum_resolution': '0.916',
        'meshfix_maximum_travel_resolution': '1.2',
        'material_pressure_advance_factor': '0.06',
        'material_print_temperature': '240',
        'cool_min_layer_time': '10',
        'cool_min_temperature': '220',
        'support_bottom_enable': 'False',
        'support_fan_enable': 'True',
        'support_structure': 'normal',
        'support_interface_density': '40',
        'support_interface_enable': 'True',
        'support_interface_material_flow': '90',
        'support_interface_offset': '2',
        'support_infill_rate': '10',
        'support_offset': '3',
        'support_interface_pattern': 'zigzag',
        'support_tree_rest_preference': 'buildplate',
        'bridge_settings_enabled': 'True'
    },
    'supporto_graduale': {
        'support_enable': 'True',
        'speed_support': '150',
        'support_bottom_enable': 'False',
        'support_interface_density': '80',
        'support_interface_enable': 'True',
        'support_interface_offset': '2',
        'support_interface_pattern': 'zigzag',
        'support_offset': '3',
        'support_bottom_wall_count': '0',
        'support_fan_enable': 'True',
        'support_interface_material_flow': '80',
        'support_pattern': 'triangles',
        'support_roof_wall_count': '1',
        'switch_extruder_extra_prime_amount': '2',
        'switch_extruder_retraction_amount': '1.5',
        'prime_tower_flow': '130',
        'prime_tower_max_bridging_distance': '0.6',
        'prime_tower_min_volume': '60',
        'interlocking_enable': 'True',
        'prime_tower_enable': 'True',
        'prime_tower_mode': 'interleaved',
        'prime_tower_size': '50',
        'retraction_hop': '0.9',
        'retraction_hop_enabled': 'True',
        'support_infill_rate': '20',
        'support_roof_material_flow': '100',
        'support_roof_wall_count': '0',
        'support_tree_rest_preference': 'buildplate',
        'support_z_distance': '=layer_height',
        'gradual_support_infill_step_height': '3',
        'gradual_support_infill_steps': '4'
    },
    'supporto': {
        'support_enable': 'True',
        'speed_support': '180',
        'support_bottom_enable': 'False',
        'support_interface_density': '80',
        'support_interface_enable': 'True',
        'support_interface_offset': '2',
        'support_interface_pattern': 'zigzag',
        'support_offset': '3',
        'support_bottom_wall_count': '0',
        'support_fan_enable': 'True',
        'support_interface_material_flow': '80',
        'support_pattern': 'zigzag',
        'support_roof_wall_count': '1',
        'switch_extruder_extra_prime_amount': '2',
        'switch_extruder_retraction_amount': '1.5',
        'prime_tower_flow': '130',
        'prime_tower_max_bridging_distance': '0.6',
        'prime_tower_min_volume': '60',
        'interlocking_enable': 'True',
        'prime_tower_enable': 'True',
        'prime_tower_mode': 'interleaved',
        'prime_tower_size': '50',
        'retraction_hop': '0.9',
        'retraction_hop_enabled': 'True',
        'support_infill_rate': '10',
        'support_roof_material_flow': '80',
        'support_roof_wall_count': '0',
        'support_tree_rest_preference': 'buildplate',
        'support_z_distance': '=layer_height'
    },
    'visual': {
        'line_width': '0.55',
        'skin_line_width': '0.5',
        'bottom_layers': '6',
        'top_bottom_pattern': 'zigzag',
        'top_layers': '6',
        'initial_layer_line_width_factor': '100',
        'cool_fan_speed': '25',
        'fill_perimeter_gaps': 'nowhere',
        'retract_at_layer_change': 'True',
        'retraction_extrusion_window': '0.6',
        'retraction_min_travel': '1.2',
        'retraction_prime_speed': '15',
        'retraction_retract_speed': '15',
        'meshfix_fluid_motion_enabled': 'False',
        'wall_line_count': '2',
        'wall_0_wipe_dist': '0',
        'skin_outline_count': '0',
        'skin_overlap': '50',
        'skin_preshrink': '2.2',
        'skirt_line_count': '0',
        'z_seam_corner': 'z_seam_corner_outer',
        'speed_travel': '300',
        'speed_travel_layer_0': '100',
        'switch_extruder_retraction_amount': '3',
        'switch_extruder_retraction_speeds': '25',
        'prime_tower_min_volume': '12',
        'zig_zaggify_infill': 'True',
        'zig_zaggify_support': 'True',
        'jerk_print': '10',
        'jerk_travel': '20',
        'jerk_wall_x': '10',
        'acceleration_print': '10000',
        'acceleration_topbottom': '10000',
        'acceleration_travel': '12000',
        'acceleration_wall_0': '10000',
        'acceleration_wall_x': '10000',
        'infill_material_flow': '100',
        'infill_overlap': '-10',
        'infill_pattern': 'cubic',
        'infill_randomize_start_location': 'True',
        'infill_sparse_density': '10',
        'infill_wipe_dist': '0.0',
        'inset_direction': 'inside_in',
        'meshfix_maximum_deviation': '0.025',
        'meshfix_maximum_resolution': '0.916',
        'meshfix_maximum_travel_resolution': '1.2',
        'material_pressure_advance_factor': '0.06',
        'material_print_temperature': '230',
        'cool_min_layer_time': '10',
        'cool_min_temperature': '220',
        'support_bottom_enable': 'False',
        'support_fan_enable': 'True',
        'support_structure': 'normal',
        'support_interface_density': '40',
        'support_interface_enable': 'True',
        'support_interface_material_flow': '90',
        'support_interface_offset': '2',
        'support_interface_pattern': 'zigzag',
        'support_tree_rest_preference': 'buildplate',
        'arcwelder_enable': 'True',
        'bridge_settings_enabled': 'True'
    }
}

# Funzione per generare il contenuto del file di configurazione per gli intent
def generate_specific_intent_config_content(nozzle, material, profile, layer, intent):
    intent_category = intent.replace('_', ' ')
    values_content = "\n".join([f"{key} = {value}" for key, value in intent_values[intent].items()])
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
{values_content}
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
