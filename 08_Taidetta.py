# Tehtävä 8
# Tässä on ohjelmapohja, joka piirtää kuviota kuvaruudulle. Kokeile ensin miten se toimii.
# Ei haittaa, vaikka et ymmärrä ihan kaikkea koodia. Kokeile sitten mitä tapahtuu jos laitat 
# muuttujan 'odotus' arvoksi 0.5. Entä jos odotus on 0.02? Muokkaa sitten ohjelmaa siten, että 
# piirrettävä kuvio muuttuu jotenkin.

# Otetaan käyttöön komento odottamiselle
from time import sleep

odotus = 0.02

i = 1
while i <= 10:
  print('*')
  # Odotetaan jokaisen tulostuksen jälkeen 0
  sleep(odotus)
  print(' *')
  sleep(odotus)
  print('  *')
  sleep(odotus)
  print('   *')
  sleep(odotus)
  print('    *')
  sleep(odotus)
  print('     *')
  sleep(odotus)
  print('      *')
  sleep(odotus)
  print('       *')
  sleep(odotus)
  print('        *')
  sleep(odotus)
  print('       *')
  sleep(odotus)
  print('      *')
  sleep(odotus)
  print('     *')
  sleep(odotus)
  print('    *')
  sleep(odotus)
  print('   *')
  sleep(odotus)
  print('  *')
  sleep(odotus)
  print(' *')
  sleep(odotus)
  print('*')

  i = i + 1
