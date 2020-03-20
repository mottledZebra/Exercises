#pragma once

#include <iostream>
#include "Builder.h"
#include "ProductA.h"

using namespace std;

class ConcreteBuilderA : public Builder
{
public:

  ConcreteBuilderA(void)
  {
    cout << "constructor ConcreteBuilderA" << endl;    
  }

  virtual ~ConcreteBuilderA(void)
  {
    cout << "destructor ConcreteBuilderA" << endl;   
  }

  void reset(void)
  {
    cout << "ConcreteBuilderA creates ProductA by reset()" << endl;    
    product = new ProductA();
  }
  
  void addPartA(int number)
  {
    cout << "ConcreteBuilderA adds PartA with number = " << number << " to ProductA" << endl;    
  }
  
  void addPartB(char option)
  {
    cout << "ConcreteBuilderA adds PartB with option = " << option << " to ProductA" << endl;    
  }
  
  void addPartC(void)
  {
    cout << "ConcreteBuilderA adds PartC to ProductA" << endl;    
  }
  
  ProductA* getResult(void)
  {
    cout << "ConcreteBuilderA returns ProductA by getResult()" << endl;    
    return product;
  }

protected:
  ProductA* product;
};

