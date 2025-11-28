from jsonschema import validators

def custom_properties(validator, properties, instance, schema):
    if not validator.is_type(instance, "object"):
        return

    for property, subschema in properties.items():
        if property in instance:
            if property in ["start", "end"] and "oneOf" in subschema:
                subschema = subschema.copy()
                subschema["anyOf"] = subschema.pop("oneOf")
            
            yield from validator.descend(
                instance[property],
                subschema,
                path=property,
                schema_path=property,
            )

def validate_with_custom_logic(dataset, schema):
    ValidatorClass = validators.validator_for(schema)
    all_validators = dict(ValidatorClass.VALIDATORS)
    all_validators['properties'] = custom_properties

    CustomValidator = validators.create(
        meta_schema=ValidatorClass.META_SCHEMA,
        validators=all_validators
    )
    
    CustomValidator(schema).validate(dataset)
