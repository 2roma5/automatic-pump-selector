import pint
from pint.facets.plain.quantity import PlainQuantity

ureg = pint.UnitRegistry()

Q_ = ureg.Quantity

def convert_units(value: PlainQuantity, to_unit: str) -> PlainQuantity:
    """ Convert a value from one unit to another.

    Args:
        value (PlainQuantity): The value to convert.
        to_unit (str): The unit to convert to.

    Returns:
        PlainQuantity: The converted value.
    """
    try:
        return value.to(to_unit)
    except pint.DimensionalityError as e:
        raise ValueError(f"Invalid conversion: {e}")
