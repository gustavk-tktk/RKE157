# Python kursus

Kokkuvõtlikud märkmed asjadest, mis olid minu jaoks sellel kursusel uued.

Kursuse jooksul proovisin Giti ja bashi kasutada käsurealt. Tavaliselt olen valinud mugavama tee ja kasutanud Giti graafilist liidest (Sourcetree), mistõttu on suur osa mu Giti käsurea oskustest ununenud.

## Nädal 1

Midagi uut ei olnud.

## Nädal 2

**Koodi samm-sammult läbimine (debugger).** Olen varem kogemata breakpointe lisanud, aga polnud neid kunagi teadlikult kasutanud ega koodi sammhaaval läbinud.

## Nädal 3

- **`match` / `case`** – sarnaneb SQL-i `CASE` funktsionaalsusega. Sobib hästi, kui üht väärtust on vaja võrrelda mitme kindla variandiga. Seni olin kasutanud ainult `if` / `elif` / `else`.
- **`Fore` ja `Style` (colorama)** – võimaldavad terminalis teksti värvida ja vormindada. Ma ei teadnud, et Pythonis on see võimalik.
- **venv** – virtuaalkeskkonnaga töötades on lihtsam hoida avatuna kaks eraldi terminali.

## Nädal 4

Midagi uut ei olnud.

## Nädal 5

`for`-tsükkel koos `range()`-i ja f-stringiga:

```python
for i in range(10):
    print(f"{i + 1} I will not skateboard in the halls.")
```

## Nädal 6

Kui listile lisada teine list meetodiga `append()`, lisatakse see ühe elemendina (list listi sees). Kui on vaja lisada teise listi elemendid ükshaaval, tuleb kasutada `extend()`-i:

```python
a = [1, 2]
a.append([3, 4])  # [1, 2, [3, 4]]

b = [1, 2]
b.extend([3, 4])  # [1, 2, 3, 4]
```

## Nädal 7

Midagi uut ei olnud.

## Nädal 8–9

Failidega töötamine.
