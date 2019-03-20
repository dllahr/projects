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
#include "custom_rand.h"
#include <math.h>

using namespace std;

struct VonNeumanResult {
  unsigned short value;
  unsigned long count;
};

void rand_compare(unsigned long num_runs);

VonNeumanResult von_neuman(CustomRand * custom_rand, bool verbose);

int main() {
	srand(time(NULL));
		
	cout << "unbiased from biased" << endl;
	cout << "enter parameters:  " << endl;
	
	bool do_rand_compare = false;
	
	bool verbose;
	cout << "verbose:  ";
	cin >> verbose;
	
	unsigned int bias;
	cout << "bias:  ";
	cin >> bias;
	BiasedRand biased_rand(bias);
	
	unsigned short num_bits;
	cout << "initial_num_bits:  ";
	cin >> num_bits;
	UnbiasedFromBiased unbiased(&biased_rand, num_bits);
	unbiased.set_verbose(verbose);
	
	unsigned int num_exp;
	cout << "number of experiments:  ";
	cin >> num_exp;
	
	unsigned long num_runs;
	cout << "number of runs per experiment:  ";
	cin >> num_runs;
	cout << endl;
	
	cout << "true bias:  " << (pow(2.0, bias) - 1.0) << endl;
	
	double total = 0.0;
	double total_sq = 0.0;
	for (unsigned int k = 0; k < num_exp; k++) {
	
		if (do_rand_compare)
			rand_compare(num_runs);
		
		unsigned long exec_count = 0;
		unsigned long count = 0;
		for (unsigned long j = 0; j < num_runs; j++) {
			VonNeumanResult result = von_neuman(&unbiased, verbose);//unbiased.generate();
			count += result.value;
			exec_count += result.count;
		}
		
		double current_result = ((double)count) / ((double)num_runs);
		total += current_result;
		total_sq += current_result*current_result;
		
		cout << "k, count, num_runs, num_bits, exec_count, unbiased_count:  " << k << " " << count << " " << num_runs;
		cout << " " << unbiased.get_num_bits() << " " << exec_count << " ";
		cout << (unbiased.get_buffer_entry(0) + unbiased.get_buffer_entry(1)) <<endl;
		
		unbiased.reset();
		
		exec_count = 0;
		count = 0;
		for (unsigned long j = 0; j < num_runs; j++) {
			VonNeumanResult result = von_neuman(&biased_rand, verbose);
			count += result.value;
			exec_count += result.count;
		}
		cout << "k, count, num_runs, exec_count:  " << k << " " << count << " " << num_runs << " " << exec_count << endl;
	}

	double average = total / ((double)num_exp);
	double expectation_sq = total_sq / ((double)num_exp);
	double variance = expectation_sq - (average*average);
	double std_dev = sqrt(variance);
	
	cout << "total, total_sq, num_exp:  " << total << " " << total_sq << " " << num_exp << endl;
	cout << "average, expectation_sq, variance, std_dev:  " << average << " " << expectation_sq << " " << variance << " " << std_dev << endl;
	
	return 0;
}

VonNeumanResult von_neuman(CustomRand * custom_rand, bool verbose) {
	unsigned short values[2] = {0,0};
	
	unsigned long count = 0;
	while(values[0] == values[1]) {
		values[0] = custom_rand->generate();
		values[1] = custom_rand->generate();
		
		count++;
	}
	
	if (verbose)
		cout << "von_neuman count:  " << count << endl;
	
	VonNeumanResult result;
	result.value = values[0];
	result.count = count;

	return result;
}


void rand_compare(unsigned long num_runs) {
		unsigned long rand_count = 0;
		for (unsigned long j = 0; j < num_runs; j++) {
			rand_count += rand()%2;
		}
		cout << "direct measurement of rand, num_runs:  " << rand_count << " " << num_runs << endl;
}