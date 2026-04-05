content = open('README.md').read()
content = content.replace(
    '<p align="center">\n  <img src="results/sample_aircraft.jpg" width="400"/>\n  <img src="results/sample_tank.jpg" width="400"/>\n</p>',
    '<p align="center">\n  <img src="results/tank.jpg" width="400"/>\n  <img src="results/helicopter.jpg" width="400"/>\n</p>\n<p align="center">\n  <img src="results/apc.jpg" width="400"/>\n</p>'
)
open('README.md', 'w').write(content)
print('README guncellendi!')
