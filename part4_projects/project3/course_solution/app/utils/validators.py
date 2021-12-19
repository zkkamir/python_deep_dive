"""Various validators"""


def validate_integer(
    arg_name, arg_value, min_value=None, max_value=None,
    custom_min_message=None, custom_max_message=None
):
    """Validates that `arg_value` is an integer, and optionally falls
       within specified bounds. A custom override error message can be
       provided when min/max  bounds are exceeded.
    """
    if not isinstance(arg_value, int):
        raise TypeError(f'{arg_name} must be an integer.')

    if min_value is not None and arg_value < min_value:
        if custom_min_message is not None:
            raise ValueError(custom_min_message)
        raise ValueError(f'{arg_name} must be greater than {min_value}.')
    if max_value is not None and arg_value > max_value:
        if custom_max_message is not None:
            raise ValueError(custom_max_message)
        raise ValueError(f'{arg_name} must be less than {max_value}.')
