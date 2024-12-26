from validation.ValidationStrategy import ValidationStrategy


class Field:
    def __init__(self, value: str, validator: ValidationStrategy) -> None:
        self.value = validator.validate(value)

    def __str__(self) -> str:
        return str(self.value)
