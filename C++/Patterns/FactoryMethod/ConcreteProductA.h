#pragma once
#include "product.h"

class ConcreteProductA : public Product
{
public:

  ConcreteProductA(void)
  {
    cout << "constructor ConcreteProductA" << endl;    
  }

  ~ConcreteProductA(void)
  {
    cout << "destructor ConcreteProductA" << endl;    
  }

  void run()
  {
    cout << "ConcreteProductA: run()" << endl;
  }
};

