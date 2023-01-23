from marshmallow import fields, Schema, ValidationError, validates_schema


class RequestParamSchema(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema
    def validate_cmd_params(selfself, values, *args, **kwargs):
        valid_cmd_commands = {'filter', 'sort', 'map', 'limit', 'unique'}

        if values['cmd'] not in valid_cmd_commands:
            raise ValidationError({'cmd': f'contains invalid command={values["cmd"]}'})

        return values


class RequestParamsListSchema(Schema):
    qureies = fields.Nested(RequestParamSchema, many=True)
    filename = fields.Str(required=True)
