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

#include "unbiased_from_biased.h"
#include <iostream>
#include <math.h>

using namespace std;

UnbiasedFromBiased::UnbiasedFromBiased(BiasedRand * biased_rand, unsigned short num_bits) {
	this->biased_rand = biased_rand;
	
	if (0 == num_bits) {
		throw;
	}
	this->num_bits = num_bits;

	verbose = false;
	
	reset();
}


void UnbiasedFromBiased::reset() {
	buffer[0] = 1;
	buffer[1] = 1;
	
	num_bits = 2;
}


unsigned short UnbiasedFromBiased::generate() {

	double fraction = ((double)buffer[1]) / ((double)(buffer[0] + buffer[1]));

	if (verbose)
		cout << "buffer, fraction:  " << buffer[0] << " " << buffer[1] << " " << fraction << endl;

	if (verbose)
		cout << "biased:  ";
	unsigned int bias_int = 0;

	for (unsigned short i = 0; i < num_bits; i++) {
		unsigned short biased_result = biased_rand->generate();
		
		if (verbose)
			cout << biased_result << " ";

		bias_int += biased_result;
		
		buffer[biased_result]++;
	}
	if (verbose)
		cout << endl;
			
	double bias_double = ((double)bias_int) / ((double)num_bits);
	double ratio = bias_double / fraction;
	if (verbose)
		cout << "bias_int, num_bits, bias_double, ratio:  " << bias_int << " " << num_bits << " " << bias_double << " " << ratio << endl;

	update_num_bits();
	if (verbose)
		cout << endl;
	
	if (ratio > 1.0)
		return 1;
	else
		return 0;
}

void UnbiasedFromBiased::update_num_bits() {
	double fraction = ((double)buffer[1]) / ((double)(buffer[0] + buffer[1]));
	
	unsigned int min_bits = ceil(1.0 / fraction);
	if (num_bits < min_bits)
		num_bits = min_bits;

	unsigned int new_bits = ceil( ceil(fraction * ((double)num_bits)) / (0.001 + fraction));
	
	if (new_bits > num_bits)
		num_bits = new_bits;

	if (verbose)
		cout << "update_num_bits: fraction, min_bits, num_bits  " << fraction << " " << min_bits << " " << num_bits << endl;
}
