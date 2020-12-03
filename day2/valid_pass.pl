#!/usr/bin/env swipl

:- use_module(library(pio)).
:- use_module(library(dcg/basics)).

%%%%%%% Validation for policy 1 %%%%%%%
count_char([],_,0).
count_char([C|L], C, N) :- count_char(L,C,NN), N is NN + 1, !.
count_char([C|L], CC, N) :- CC\= C, count_char(L,CC,N), !.

is_valid_pass((Range, Char, Pass)) :- is_valid_pass(Range, Char, Pass).
is_valid_pass((Low, High), Char, Password) :- 
    count_char(Password, Char, Occurrences),
    between(Low, High, Occurrences).

count_valid([],0).
count_valid([Rec| Records], NN) :-
    (is_valid_pass(Rec), count_valid(Records, N), NN is N + 1); 
    (\+ is_valid_pass(Rec), count_valid(Records, N), NN = N).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%% Validation for policy 2 %%%%%%%
is_valid_pass2((Positions, Char, Pass)) :- is_valid_pass2(Positions, Char, Pass).
is_valid_pass2((Pos1, Pos2), Char, Pass) :-
    nth1(Pos1, Pass, Char1),
    nth1(Pos2, Pass, Char2),
    xor(Char1 == Char, Char2 == Char).

count_valid2([], 0).
count_valid2([Rec| Records], NN) :-
    (is_valid_pass2(Rec), count_valid2(Records, N), NN is N + 1); 
    (\+ is_valid_pass2(Rec), count_valid2(Records, N), NN = N).

xor(P1, P2) :- or(P1, P2), nand(P1,P2), !.
or(P1, P2) :- P1 ; P2.
nand(P1,P2) :- \+ (P1, P2).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%% File parsing rules %%%%%%%
range((Start,End))              --> number(Start) , "-" , number(End).
record((Range,Char, Password))  -->
    range(Range), " ", [Char], ": ", string_without("\n",Password).

records([])         --> call(eos), !.
records([R | Recs]) --> record(R), "\n", records(Recs).
%%%%%%%%%%%%

:- initialization(main,main).

main([InputFile]) :-
    main([InputFile, '1']).

main([InputFile, '1']) :-
    write('First policy'), nl,
    phrase_from_file(records(Rec), InputFile),
    count_valid(Rec, Valid),
    write(Valid), nl.

main([InputFile,'2']) :-
    write('Second policy\n'), nl,
    phrase_from_file(records(Rec), InputFile),
    count_valid2(Rec, Valid),
    write(Valid), nl.