Flags = -Wall -Wreturn-type -pedantic -pedantic-errors -Wundef -std=c++11 -O2
CPP = g++

A : A.cpp
	$(CPP) $(Flags) -o A A.cpp

B : B.cpp
	$(CPP) $(Flags) -o B B.cpp

C : C.cpp
	$(CPP) $(Flags) -o C C.cpp

D : D.cpp
	$(CPP) $(Flags) -o D D.cpp

E : E.cpp
	$(CPP) $(Flags) -o E E.cpp

$(file) : $(file).cpp
	$(CPP) $(Flags) -o $(file) $(file).cpp
