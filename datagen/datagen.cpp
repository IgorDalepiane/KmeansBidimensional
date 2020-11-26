#include <cstdlib>
#include <ctime>
#include <iostream>

// -----------------------------------
// Code made by Marcelo Resende Thielo
// -----------------------------------

using namespace std;

void datagen(double x0, double y0, double s, int n, int m) {
  double x, y;

  for (int i = 0; i < n; i++) {
    x = x0;
    y = y0;
    for (int j = 0; j < m; j++) {

      x = x + (2.0 * s) * (double)rand() / (double)RAND_MAX - s;
      y = y + (2.0 * s) * (double)rand() / (double)RAND_MAX - s;
    }
    cout << x << " " << y << endl;
  }
}

int main(void) {

  datagen(100,100,10,1000,1000);
  datagen(200,700,10,1000,1000);
  datagen(1400,200,10,1000,1000);
  datagen(750,800,10,1000,1000);
  datagen(1290,990,10,1000,1000);
  datagen(1700,1700,10,1000,1000);
}