from .ValidationStrategy import ValidationStrategy


class PhoneValidation(ValidationStrategy):
    def validate(self, value: str) -> str:
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits")
        return value
