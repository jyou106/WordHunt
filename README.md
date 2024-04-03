# Word Hunt

## Install dependencies

`pip install -r requirements.txt`

## Run

`python -m wordhunt`

## How to play

To select a word, enter a semicolon-delimited list of indices of letters (e.g., 2,1;2,2;1,2).

```text
$ python -m wordhunt
X F O U
O T C U
Q H I I
V A G A
>> 2,1;2,2;1,2
Valid word HIC
X F O U
O T C U
Q H I I
V A G A
>> 2,1;2,2;1,1
Valid word HIT
X F O U
O T C U
Q H I I
V A G A
>> 1,2;2,1;2,2;1,1
Valid word CHIT
X F O U
O T C U
Q H I I
V A G A
>>

{
    "CHIT": 400,
    "HIC": 100,
    "HIT": 100
}
Score: 600
Words: 3
```
