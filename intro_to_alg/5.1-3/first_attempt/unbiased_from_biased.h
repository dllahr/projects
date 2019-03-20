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

#ifndef _unbiased_from_biased_h
#define _unbiased_from_biased_h

#include "biased_rand.h"

class UnbiasedFromBiased {
private:
  unsigned long buffer[2];
  
  BiasedRand * biased_rand;

public:
  UnbiasedFromBiased(BiasedRand * biased_rand);
  ~UnbiasedFromBiased() {}
  
  unsigned short int generate();
  
  BiasedRand * get_biased_rand() {return biased_rand;}
  
  void reset();
  
  //each time the loop executes the value in one of the buffer entries is
  //incremented.  But each buffer starts with a value of 1.
  unsigned long get_num_loop_runs() {return buffer[0] + buffer[1] - 2;}
  
  unsigned long get_buffer_entry(unsigned short int index) {return buffer[index];}
};

#endif