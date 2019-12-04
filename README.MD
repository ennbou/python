# Automate in Python

>Code source du package Automate.

## un exemple d'un automate

>Ci-dessus une presentation d'un automate et la relation entre les donnees et les variables dans la class Automate.
>Cette Automate que j'ai utilise pour tester la classe Automate(unitest).

### presentation graphique

![image](Automate/img/automate1.png)

### traduction du donnees

1. les alphabets

    ``` python
    alphabet = ["a", "b", "c"]
    ```

2. les etats

    ``` python
    etats = ["q0", "q1", "q2"]
    ```

3. les transactions

    ``` python
    transaction = {
            'q0': {
                'a': 'q0',
                'b': 'q1'
            },
            'q1': {
                'a': 'q1',
                'c': 'q2'
            }
    ```

4. etat initial et etat finale

    ``` python
        start = 'q0'
        end = ['q1']
    ```

