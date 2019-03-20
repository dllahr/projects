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
#include <stdlib.h>
#include <time.h>
#include "biased_rand.h"
#include "unbiased_from_biased.h"

using namespace std;

int main() {
	bool verbose = false;
	
	srand(time(NULL));
		
	cout << "unbiased from biased" << endl;
	
	
	cout << "enter n for ratio of (2^n) - 1:  ";
	
	BiasedRand biased_rand(2);
	UnbiasedFromBiased unbiased(&biased_rand);
	
	unsigned int num_exp;
	cout << endl << "enter number of experiments:  ";
	cin >> num_exp;
	cout << endl;
	
	unsigned long num_runs;
	cout << endl << "enter number of runs:  ";
	cin >> num_runs;
	cout << endl;
	
	for (unsigned int k = 0; k < num_exp; k++) {
	
		unsigned long rand_count = 0;
		for (unsigned long j = 0; j < num_runs; j++) {
			rand_count += rand()%2;
		}
		cout << "direct measurement of rand, num_runs:  " << rand_count << " " << num_runs << endl;
		
		unbiased.reset();
		unsigned long count = 0;
		for (unsigned long j = 0; j < num_runs; j++) {
			count += unbiased.generate();
			//cout << "result:  " << result << endl;
		}
		
		cout << "unbiased attempt, number of 1's returned:  " << count << " " << num_runs << endl;
	}

	return 0;
}

