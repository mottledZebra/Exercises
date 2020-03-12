#pragma once

#include <iostream>
#include "Product.h"

using namespace std;

class Creator
{
public:

  Creator(void)
  {
    cout << "constructor Creator" << endl;    
  }

  virtual ~Creator(void)
  {
    cout << "destructor Creator" << endl;    
  }

  void runProduct()
  {
    cout << "Creator: runProduct()" << endl;
    Product* p = FactoryMethod();
    cout << "Creator running Product" << endl;
    p->run();
  }

protected:
  virtual Product* FactoryMethod() = 0;

};

