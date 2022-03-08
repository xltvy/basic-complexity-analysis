# basic-complexity-analysis

Bogazici University

Computer Engineering Department

Fall 2021

CMPE 300 - Analysis of Algorithms

Project 1

Altay Acar & Engin Oguzhan Senol

***

A short experimental research on a given algorithm's complexity analysis.

There is a given pseudocode of the algorithm shown below:
function Example (X[0:n-1])
Input : X[0 : n−1] (a list of size n) Output : y (an integer)
y←0
for i ← 0 to n − 1 do
if X[i] = 0 then
for j ← i to n − 1 do
for k ← n downto 1 by k ← ⌊𝑘/2⌋ do y ← y+1
endfor endfor
else
for m ← i to n-1 do
for t ← 1 to n do x ←n
while x > 0 do x ← x-t
y ← y+1 endwhile
endfor endfor
endif endfor
return (y) end Example

Using this pseudocode as the base of the actual code, we have run tests by choosing different operations as basic operation and measured the results regarding the complexity analysis of this code.

The project description is provided via the pdf file cmpe300-project1-description.pdf and the results of our analysis is provided via cmpe300-project1-solution.pdf file.

How to run the code?

The code of our project designed to run for:
	- 1 input file for the best-case execution
	- 1 input file for the worst-case execution
	- 5 input files for the average-case execution

The naming convention of the input files follows:
input<number>.txt	where number is the index of the input file.

Our program executes with the command of

python AltayAcar_EnginOguzhanSenol.py

and after this command, the algorithm is executed for each input file and the result will be printed to the CLI one by one. To properly run with this command, all input files in correct naming convention should be under the same directory with the Python script AltayAcar_EnginOguzhanSenol.py

In order to correctly run our code the input files should be in order of "best case input - worst case input - average case inputs" for each size of input. If we denote the number of input files for the average case execution as "n," then these "n+2" input files should contain same size of input. To give an example to clarify:

Considering 5 average case inputs for each input sizes:
input01.txt - best case for input size of 1
input02.txt - worst case for input size of 1
input03.txt - average case 1 for input size of 1
input04.txt - average case 2 for input size of 1
input05.txt - average case 3 for input size of 1
input06.txt - average case 4 for input size of 1
input07.txt - average case 5 for input size of 1
input08.txt - best case for input size of 10
input09.txt - worst case for input size of 10
input10.txt - average case 1 for input size of 10
input11.txt - average case 2 for input size of 10
input12.txt - average case 3 for input size of 10
input13.txt - average case 4 for input size of 10
input14.txt - average case 5 for input size of 10
...

!!!
In order to run the code for an average time calculation of different number of inputs (say n inputs for average calculation) than 5, following should be done:

	1- 37th line of code should be changed from:

		for f in range(0, len(input_list), 7):

	   to:

	   	for f in range(0, len(input_list), (n+2)):

	2- 39th line of code should be changed from:

		slice = input_list[f:f+7]

	   to:

	   	slice = input_list[f:f+(n+2)]

	3- 94th line of code should be changed from:

		t = avg_time/5

	   to:

	   	t = avg_time/n
!!!

