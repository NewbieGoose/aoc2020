#!/usr/bin/env swipl

:- use_module(library(pio)).
:- use_module(library(dcg/basics)).


numbers([])         --> call(eos), !.
numbers([N | Nums]) --> number(N), "\n" , numbers(Nums).

:- initialization(main,main).

comb([], []).
comb([H|L], [H|Ls]) :- comb(L,Ls).
comb([_|L], Ls) :- comb(L,Ls).

mult([],1).
mult([M| L], Mul) :- mult(L, RMul) , Mul is RMul * M.

sum_to_mul(NumberList, Const, Number, Mul) :-
    length(Comb,Number),
    comb(NumberList, Comb),
    sum_list(Comb, Const),
    mult(Comb,Mul).


main([InputFile, NumberAtom, ConstAtom]) :-
    phrase_from_file(numbers(Numbers), InputFile),
    atom_number(NumberAtom,Number),
    atom_number(ConstAtom,Const),
    sum_to_mul(Numbers, Const, Number, Mul),
    write(Mul), nl.