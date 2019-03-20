/*Copyright (C) 2013 David L. Lahr

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in the 
Software without restriction, including without limitation the rights to use, copy, 
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the
following conditions:

The above copyright notice and this permission notice shall be included in all copies
or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
DEALINGS IN THE SOFTWARE.*/

#include <iostream>
#include "biased_rand.h"
#include "unbiased_from_biased.h"
#include <stdlib.h>
#include <time.h>

using namespace std;

void test_biased();

void test_max_value();

void test_unbiased();

int main() {
	srand(time(NULL));
	
	test_biased();
	
	test_max_value();
	
	test_unbiased();
}

void test_unbiased() {
	cout << "test_unbiased:  \n";

	UnbiasedFromBiased unbiased(new BiasedRand(3), 20);
	unbiased.set_verbose(true);
	
	for (int i = 0; i < 10; i++)
		cout << unbiased.generate() << endl << endl;
}

void test_max_value() {
	cout << "test_max_value:  ";
	for (int i = 1; i <= 10; i++) {
		UnbiasedFromBiased unbiased(NULL, i);
		cout << unbiased.get_max_value() << " ";
	}
	cout << endl;
}

void test_biased() {
	BiasedRand biased_rand(3);
	
	unsigned long buffer[2];
	buffer[0] = 0;
	buffer[1] = 0;

	for (int i = 0; i < 10000; i++) {
		buffer[biased_rand.generate()]++;
	}
	
	float ratio = ((float)buffer[0]) / ((float)buffer[1]);
	cout << "test biased:  " << buffer[0] << " " << buffer[1] << " " << ratio << endl;
}
