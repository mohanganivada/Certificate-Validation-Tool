import helper

mapping = helper.read_certificate_mapping_config()
mappings = {}

for i in mapping['Mappings']:
    mappings[i] = {
        "Value": ''
    }
for i in mappings:
    mappings[i] = {
        'Value': mapping['Mappings'][i]
    }

cname_mappings = mappings.keys()