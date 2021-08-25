# BetterFuck

A useful language to generate working brainfk code.

to use: write the code in 'input.btf' and run 'betterfuck.py'

'betterfuck.py' is just for generate brainfuck code, 
but 'betterfuck_compiler.py' generates brainfuck code and runs it through online site.

You need 'selenium' python module to run 'betterfuck_compiler.py'.

betterfuck guide:
```
betterfuck has 9 keywords.

input: gets an input to the selected variable (same as ',')

output: prints a selected variable's value (same as '.')
output [char]: prints the char
output %[number]: prints the ascii char of the number

select [pointer]: selects the target pointer
select $[pointer]: selects the target pointer
select +/-[number]: moves the pointer right(+)/left(-)

add [number]: adds the number to the selected variable
add %[number]: adds the number to the selected variable
add $[pointer]: adds the written pointer's value to the selected one

sub [number]: subs the number from the selected variable
sub %[number]: subs the number from the selected variable
sub $[pointer]: subs the written pointer's value from the selected one

set [char]: sets the selected variable with written char's ascii code
set %[number]: sets the selected variable with written number
set $[pointer]: sets the selected variable with written pointer's value

while, end: same as '[', ']'

exit: makes the compiler exit (and makes it generate the brainfk code)

parameter type:
[char]: a character, like A, [, @
[number], [pointer]: a number
```
