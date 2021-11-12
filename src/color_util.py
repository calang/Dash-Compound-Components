"""Color utilities"""

from typing import Union, Tuple


def color_value_to_hex(color: str, value: Union[float, int]) -> str:
    """Convert a color and an value"""
    value = int(value)
    multiplier = {'red': 0x010000, 'green': 0x000100, 'blue': 0x00001}.get(color, 0x010000)
    color_value = value * multiplier
    return f'#{color_value:06x}'


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """Return the int color components indicated in a hex color string."""
    hex_string = hex_color.lstrip('#')
    return tuple(int(hex_string[i:i + 2], 16) for i in (0, 2, 4))


def rgb_hex_color_add(r_hex, g_hex, b_hex) -> str:
    """Adds three red, green and blue hex colors into the resulting hex color."""
    mixed_color = (hex_to_rgb(r_hex)[0] * 0x010000
                   + hex_to_rgb(g_hex)[1] * 0x000100
                   + hex_to_rgb(b_hex)[2] * 0x000001
                   )
    hex_color = f'#{mixed_color:06x}'
    return hex_color
