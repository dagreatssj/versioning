import json


def crx_manifest(version_type, filepath, increment, indent):
    if (version_type):
        with open(filepath, "r") as manifest_json_file:
            data = json.load(manifest_json_file)
            manifest_json_file.close()

        curr_ver = data['version']
        indiv_ver = curr_ver.split(".")

        if version_type == "major":
            major = int(indiv_ver[0]) + increment
            ver_str = str(major) + "." + str(indiv_ver[1]) + "." + str(indiv_ver[2])
        elif version_type == "minor":
            minor = int(indiv_ver[1]) + increment
            ver_str = str(indiv_ver[0]) + "." + str(minor) + "." + str(indiv_ver[2])
        elif version_type == "patch":
            patch = int(indiv_ver[2]) + increment
            ver_str = str(indiv_ver[0]) + "." + str(indiv_ver[1]) + "." + str(patch)
        else:
            ver_str = version_type

        data['version'] = ver_str

        with open(filepath, "w") as manifest_json_file:
            json.dump(data, manifest_json_file, indent=2, sort_keys=False)
            manifest_json_file.close()
