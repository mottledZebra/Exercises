#pragma once

#include <iostream>
#include "Builder.h"
#include "ProductB.h"

using namespace std;

class ConcreteBuilderB : public Builder
{
public:

  ConcreteBuilderB(void)
  {
    cout << "constructor ConcreteBuilderB" << endl;    
  }

  virtual ~ConcreteBuilderB(void)
  {
    cout << "destructor ConcreteBuilderB" << endl;    
  }

  void reset(void)
  {
    cout << "ConcreteBuilderB creates ProductB by reset()" << endl;    
    product = new ProductB();
  }
  
  void addPartA(int number)
  {
    cout << "ConcreteBuilderB adds PartA with number = " << number << " to ProductB" << endl;    
  }
  
  void addPartB(char option)
  {
    cout << "ConcreteBuilderB adds PartB with option = " << option << " to ProductB" << endl;    
  }
  
  void addPartC(void)
  {
    cout << "ConcreteBuilderB adds PartC to ProductB" << endl;    
  }
  
  ProductB* getResult(void)
  {
    cout << "ConcreteBuilderB returns ProductB by getResult()" << endl;    
    return this->product;
  }

protected:
  ProductB* product;
};

