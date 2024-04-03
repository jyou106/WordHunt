# Word Hunt

## Install dependencies

`pip install -r requirements.txt`

## Run

`python -m wordhunt`

## How to play

To select a word, enter a semicolon-delimited list of indices of letters (e.g., `2,1;2,2;1,2`).

```text
$ python -m wordhunt

F H O O
S P A Y
M I I I
Z L L M
60 seconds left
>> 1,0;1,1;1,2;1,3
Valid word SPAY

F H O O
S P A Y
M I I I
Z L L M
52 seconds left
>> 1,0;1,1;1,2
Valid word SPA

F H O O
S P A Y
M I I I
Z L L M
45 seconds left
>> 0,1;1,2;1,3
Valid word HAY

F H O O
S P A Y
M I I I
Z L L M
35 seconds left
>> 1,3;1,2;1,3
Index pair (1, 3) is repeated

F H O O
S P A Y
M I I I
Z L L M
20 seconds left
>> 0,1;0,2;0,3
Invalid word HOO

F H O O
S P A Y
M I I I
Z L L M
9 seconds left
>> 3,0;

Time's up

{
    "SPAY": 400,
    "HAY": 100,
    "SPA": 100
}
Score: 600
Words: 3
```
