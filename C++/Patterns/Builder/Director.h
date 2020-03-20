#pragma once

#include <iostream>
#include "Builder.h"

using namespace std;

class Director
{
public:

  Director(void)
  {
    cout << "constructor Director" << endl;    
  }

  virtual ~Director(void)
  {
    cout << "destructor Director" << endl;    
  }

  void makeConstruction1(Builder* builder)
  {
    cout << "Director makes Construction1" << endl;    
    builder->reset();
    builder->addPartA(2);
    builder->addPartC();
  }

  void makeConstruction2(Builder* builder)
  {
    cout << "Director makes Construction2" << endl;    
    builder->reset();
    builder->addPartA(5);
    builder->addPartB('S');
  }
};

