# Tomiho skriptik

Mala pomocka pri generovani excelu z virtualnych behov

## Predtym jak s tym budes robic

1. spusti `pip install -r requirements.txt`

## Jak s tym robic

1. Ta otvor `script.py`
2. uprav `current` na dnesny datum
3. pridaj dnesny datum do `cols`
4. zmen cestu k priecinku s fotkami v `dirname`
5. ak sa vstupny excel vola inak, premenuj ho v `infile`
6. ak sa cielovy excel ma volat inak, premenuj ho v `outfile`

## Jak to funguje?!?!?!

Ta aby sa mi lahsie robilo, ta robim to cez dajaku heš mapu (zlato na nej nenajdes), kde si pre kazde meno ulozim jednotlive datumy behov, pricom najprv nacitam stare hodnoty z excelu, potom nacitam hodnoty z novych fotiek a potom ulozim

## Prve spustenie

Kedze prvy krat este nemas excel, tak nahrad na riadku 70

```
hashmap = read_to_hashmap()
```

za

```
hashmap = {}
```