import file_system
import base_roles

known_roles = file_system.get_all_files_in_folder("settings")
if not known_roles:
    player_roles = base_roles.weights
else:
    player_roles = {}
    for role in known_roles:
        player_roles[role.stem] = file_system.read_json_file(role)

