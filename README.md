# Nezavisna analiza podataka uredjaja iMETOS 3.3 za klimatske i agroekoloske uslove u Pancevu

iMETOS 3.3 je napredni sistem za monitoring koji se koristi u razlicitim poljoprivrednim i agronomskim primenama, ukljucujuci upravljanje navodnjavanjem, kontrolu bolesti i stetocina,
optimizaciju upotrebe djubriva i pesticida i opste upravljanje useva zemljista.<br>

Stanica na Starom Tamisu svakodnevno analizira podatke i evidentira ih **automatski** prenosenjem informacija na server/cloud sto omogucava pristup podacima u realnom vremenu. Stanica se nalazi na lokaciji 44.868716 20.76308 (Istrazivacko-razvojni institut Tamis Pancevo)<br>

Rezultate analize su izvedeni iz dataseta racunanjem frekvencije(ponavljanja) zabelezenih vrednosti na osnovu istih/priblizno slicnih pojava svakodnevno u periodu januar-decembar 2010-2024, skala prema kojoj je to uredjeno zavisi od senzora cije podatke pokusavamo da izracunamo.<br>

Analiza je uradjena za temperaturu vazduha, relativnu vlaznost vazduha, padavine(kise,snega,susnezice,grada), deficita vodenog pritiska, temperaturu pritiska.<br>
 
<p align="center">
  <img src="https://github.com/stefantonic/iMETOS3.3-pancevo/blob/main/air_temp/test_comparison.png?raw=true" />
</p>

<p align="center">
  <img src="https://github.com/stefantonic/iMETOS3.3-pancevo/blob/main/relative_humidity/test_comparison_humidity.png" />
</p>

|Suspendovane cestice | Princip uzorkovanja i merenja | Granicna gornja vrednost koja ne bi trebala biti predjena za kal. godinu           
|----------------|----------------|----------------| 
|SO2                |Uzorkovanje u toku 24h. analiza uzorka u laboratoriji metoda sa tetrahlormerkuratom i pararosanilinom. | 50µg/m3
ČAĐ				|	Uzorkovanje u toku 24h. analiza uzorka u laboratoriji, reflektometrija.| 50µg/m3
NO2				| Uzorkovanje u toku 24h. analiza uzorka u laboratoriji, Griess-Saltzmann-ov metod(spektrofotometrija)| 40µg/m3
NH3				| Uzorkovanje u toku 24h. analiza uzorka u laboratoriji, spektrofotometrija, "indofenol plavo"| Nedefinisano
Benzen			| Nedefinisano | 5µg/m3
PM10          | Jedno uzorkovanje u toku 24h u laboratoriji, druga cetiri se vrse automatski| 40µg/m3

## Resursi
`FieldClimate -> iMETOS 3.3, svi podaci su skinuti sa ovog sajta za dalju analizu`<br>
`Prognozno-izveštajna služba zaštite bilja (PIS)`<br>
`Istrazivacko-razvojni institut Tamis Pancevo`<br>
`google..`<br>

na masini koja pokrece<br>
`ubuntu 22.04.4 LTS`<br>
`python 3.10.12`<br>

## Instalacija
`git clone https://github.com/6c756e6172/zjzpa-analiza.git`<br>
`pipinstall pypdf pandas numpy`<br>
`chmod +x ./script.sh` zatim `./script.sh`<br> 

## Licenca
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-nd/4.0/)
