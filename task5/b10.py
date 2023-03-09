import re
css = ''.join([input() for _ in range(int(input()))])
hex_colors = re.findall(r'(#[A-Fa-f0-9]{6}|#[A-Fa-f0-9]{3})', ''.join(re.findall(r'{([^}]+)}', css)))
print(*hex_colors, sep='\n')