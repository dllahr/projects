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
#include "math.h"

using namespace std;

int main() {
	srand(time(NULL));

	UnbiasedFromBiased * unbiased = new UnbiasedFromBiased(new BiasedRand(1));
	
	cout << "num_runs, ratio, true_ratio, count, num_loops, buffer0, buffer1" << endl;
	
	for (unsigned long num_runs = 1000; num_runs <= 100000; num_runs *= 10) {
//		{ unsigned short int ratio = 6;
		for (unsigned short int ratio = 1; ratio <= 6; ratio++) {
			unbiased->get_biased_rand()->set_ratio(ratio);
			
			unsigned long count = 0;
			for (unsigned long i = 0; i < num_runs; i++) {
				count += unbiased->generate();
			}
			
			cout << num_runs << "," << ratio << "," << (pow(2,ratio) - 1) << ",";
			cout << count << "," << unbiased->get_num_loop_runs() << ",";
			cout << unbiased->get_buffer_entry(0) << "," << unbiased->get_buffer_entry(1) << endl;
			
			unbiased->reset();
		}
	}
}