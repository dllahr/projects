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

UnbiasedFromBiased::UnbiasedFromBiased(BiasedRand * biased_rand) {
	this->biased_rand = biased_rand;
	
	reset();
}


void UnbiasedFromBiased::reset() {
	buffer[0] = 1;
	buffer[1] = 1;
}


unsigned short int UnbiasedFromBiased::generate() {
	
	unsigned short int target_value;
	unsigned int ratio;
	if (buffer[0] > buffer[1]) {
		target_value = 1;
		ratio = buffer[0] / buffer[1];
	} else {
		target_value = 0;
		ratio = buffer[1] / buffer[0];
	}

//		cout << "buffer, ratio:  " << buffer[0] << " " << buffer[1] << " " << ratio << endl;
			
	unsigned short int i = 0;
	bool notDone = true;
	unsigned short int result;
	while (i < ratio && notDone) {
		result = biased_rand->generate();
			
//			cout << "\t\t" << i << " " << result << endl;
				
		if (target_value == result) {
			notDone = false;
		}
				
		buffer[result]++;
				
		i++;
	}
	
	return result;
}