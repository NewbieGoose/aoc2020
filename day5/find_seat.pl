#!/usr/bin/env swipl

:- use_module(library(dcg/basics)).
:- use_module(library(pio)).

seat([1|Seat])      --> ("B" ; "R"), seat(Seat).
seat([0|Seat])      --> ("F" ; "L"), seat(Seat).
seat([])            --> "\n".

seats([Seat | S])   --> seat(Seat), seats(S).
seats([])           --> call(eos).

binary([], 0).
binary([B | L], NN) :-
    binary(L,N),
    NN is N * 2 + B.

bin_seat_id(L,N) :- reverse(L,RL), binary(RL, N).


max_seat(L, Max) :-
    maplist(bin_seat_id, L, Seats),
    max_list(Seats, Max), !.

find_empty_seat(L, EmptySeat) :- 
    maplist(bin_seat_id, L, Seats),
    sort(Seats, Sorted),
    find_missing(Sorted, EmptySeat),!.

find_missing([S1, S2 | Sorted], Missing) :- 
    succ(S1,S2),
    find_missing([S2| Sorted], Missing).

find_missing([S1,S2 | _], Missing) :-
    \+ succ(S1,S2),
    succ(S1, Missing).


:- initialization(main,main).

main([InputFile, 'max']) :- 
    phrase_from_file(seats(Seats), InputFile),
    max_seat(Seats, Max),
    format('Max seat id: ~d', [Max]), nl.

main([InputFile, 'seat']) :-
    phrase_from_file(seats(Seats), InputFile),
    find_empty_seat(Seats, Missing),
    format('Grab a seat at: ~d', [Missing]), nl.

main([InputFile]) :-
    main([InputFile, 'seat']).


main([]) :-
    main(['input.txt']).