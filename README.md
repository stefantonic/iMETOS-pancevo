# Nezavisna analiza podataka uredjaja iMETOS 3.3 za klimatske i agroekoloske uslove u Pancevu

iMETOS 3.3 je napredni sistem za monitoring koji se koristi u razlicitim poljoprivrednim i agronomskim primenama, ukljucujuci upravljanje navodnjavanjem, kontrolu bolesti i stetocina,
optimizaciju upotrebe djubriva i pesticida i opste upravljanje useva zemljista.<br>

Stanica na Starom Tamisu svakodnevno analizira podatke i evidentira ih **automatski** prenosenjem informacija na server/cloud sto omogucava pristup podacima u realnom vremenu. Stanica se nalazi na lokaciji 44.868716 20.76308 (Istrazivacko-razvojni institut Tamis Pancevo)<br>

**Rezultate analize su izvedeni iz dataseta racunanjem frekvencije(ponavljanja) zabelezenih vrednosti na osnovu istih/priblizno slicnih pojava svakodnevno u periodu januar-decembar 2010-2024, skala prema kojoj je to uredjeno zavisi od senzora cije podatke pokusavamo da izracunamo**.<br>

Analiza je uradjena za temperaturu vazduha, relativnu vlaznost vazduha, padavine(kise,snega,susnezice,grada), deficita vodenog pritiska, temperaturu pritiska.<br>
 
<p align="center">
  <img src="https://github.com/stefantonic/iMETOS3.3-pancevo/blob/main/air_temp/test_comparison.png?raw=true" />
</p>

<p align="center">
  <img src="https://github.com/stefantonic/iMETOS3.3-pancevo/blob/main/relative_humidity/test_comparison_humidity.png" />
</p>

##Tabela koja sadrzi listu senzora koji se obicno koristi sa uredjajem iMETOS, senzori i njihova dostupnost zavisi od modela stanice

| **Senzor**                | **Opis**                                                                                   | **Funkcija i rad**                                                                                     |
|---------------------------|--------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Temperaturni senzor**  | Meri temperaturu vazduha.                                                                 | Senzor koristi termostatski element (obično termopar ili termistor) koji registruje promene u temperaturi i salje podatke.                          |
| **Vlažnost vazduha**      | Meri relativnu vlaznost vazduha.                                                           | Koristi higrometarski element (kao sto je kapacitivni ili otpornik senzor) koji osetljivo reaguje na promene u količini vodene pare u vazduhu.                |
| **Senzor padavina**       | Meri količinu padavina.                                                                     | Ponekad koristi princip padavina u kapacitivnoj ili infracrvenoj tehnologiji za merenje kolicine padavina u vremenskim periodima.                        |
| **Vetro-senzor**          | Meri brzinu i pravac vetra.                                                                 | Ukljucuje anemometar za brzinu vetra i više anemometara ili osciloskope za odredjivanje pravca vetra. Cesto koristi mehanicke ili elektronske komponente. |
| **Senzor radijacije**    | Meri intenzitet solarne radijacije.                                                        | Koristi fotoelektricne celije ili druge fotosenzorske komponente koje mere količinu sunceve svetlosti koja pada na senzor.                      |
| **Senzor vlažnosti tla** | Meri vlaznost u zemljistu.                                                                  | Koristi kapacitivni ili otpornik princip za merenje kolicine vode u tlu, sto utice na elektricne karakteristike senzora.                               |
| **Senzor temperature tla** | Meri temperaturu tla.                                                                      | Koristi termopar, termistor ili slicne tehnologije za merenje temperature u razlicitim slojevima tla.                                                     |
| **Senzor pritiska**      | Meri atmosferski pritisak.                                                                  | Koristi barometrijski senzor koji meri varijacije u atmosferskom pritisku, sto moze biti korisno za prognozu vremenskih uslova.                              |
| **Senzor ugljen-dioksida (CO2)** | Meri koncentraciju ugljen-dioksida u vazduhu.                                             | Koristi infracrvene tehnologije ili druge principe za detekciju koncentracije CO2 u atmosferi.                                                            |
| **Senzor za intenzitet svetlosti** | Meri intenzitet svetlosti u okruzenju.                                                      | Koristi fotodetektore koji pretvaraju svetlost u elektricni signal, omogucavajuci merenje intenziteta svetlosti.                                             |

## Resursi
`FieldClimate -> iMETOS 3.3, svi podaci su skinuti sa ovog sajta za dalju analizu`<br>
`Prognozno-izveštajna služba zaštite bilja (PIS)`<br>
`Istrazivacko-razvojni institut Tamis Pancevo`<br>
`google..`<br>

na masini koja pokrece<br>
`ubuntu 22.04.4 LTS`<br>
`python 3.10.12`<br>

## Instalacija
`git clone https://github.com/stefantonic/iMETOS-pancevo.git`<br>
`pipinstall csv pyexcel panda plotly.express`<br>
`chmod +x ./script.sh` zatim `./script.sh`<br> 

## Licenca
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-nd/4.0/)
