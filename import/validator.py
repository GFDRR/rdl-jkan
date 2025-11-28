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


def custom_required(validator, required, instance, schema):
    """Custom required validator that removes 'occurrence' from required fields for Event objects."""
    if not validator.is_type(instance, "object"):
        return
    
    # If this is an Event schema and occurrence is required, remove it from validation
    if schema.get("title") == "Event" and "occurrence" in required:
        required = [r for r in required if r != "occurrence"]
    
    # Use the default required validator with potentially modified required list
    for property in required:
        if property not in instance:
            yield validators.ValidationError(f"{property!r} is a required property")

def validate_with_custom_logic(dataset, schema):
    ValidatorClass = validators.validator_for(schema)
    all_validators = dict(ValidatorClass.VALIDATORS)
    all_validators['properties'] = custom_properties
    all_validators['required'] = custom_required

    CustomValidator = validators.create(
        meta_schema=ValidatorClass.META_SCHEMA,
        validators=all_validators
    )
    
    CustomValidator(schema).validate(dataset)
