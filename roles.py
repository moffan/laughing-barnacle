import file_system
import base_roles

_known_roles = file_system.get_all_files_in_folder("settings/roles")

if not _known_roles:
    player_roles = base_roles.weights
else:
    player_roles = {}
    for role in _known_roles:
        player_roles[role.stem] = file_system.read_json_file(role)
