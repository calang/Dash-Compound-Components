"""Color utilities"""

from typing import Union


def color_intensity_to_hex(color: str, intensity: Union[float, int]) -> str:
    intensity = int(intensity)
    multiplier = {'red': 0x010000, 'green': 0x000100, 'blue': 0x00001}.get(color, 0x010000)
    color_value = intensity * multiplier
    return f'#{color_value:06x}'


def hex_to_rgb(hex_color: str):
    h = hex_color.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgb_hex_color_add(r_hex, g_hex, b_hex) -> str:
    """Adds three red, green and blue hex colors into the resulting hex color."""
    mixed_color = (hex_to_rgb(r_hex)[0] * 0x010000
                   + hex_to_rgb(g_hex)[1] * 0x000100
                   + hex_to_rgb(b_hex)[2] * 0x000001
                   )
    hex_color = f'#{mixed_color:06x}'
    return hex_color


