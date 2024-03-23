from utils.validator_json import validator_all_json_schemas


def test_validate_resource_schema():
    validator_all_json_schemas('create', 'create_new_user_schema.json')