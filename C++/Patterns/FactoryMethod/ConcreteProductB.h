#pragma once
#include "product.h"

class ConcreteProductB : public Product
{
public:

  ConcreteProductB(void)
  {
    cout << "constructor ConcreteProductB" << endl;    
  }

  ~ConcreteProductB(void)
  {
    cout << "destructor ConcreteProductB" << endl;    
  }

  void run()
  {
    cout << "ConcreteProductB: run()" << endl;
  }
};

