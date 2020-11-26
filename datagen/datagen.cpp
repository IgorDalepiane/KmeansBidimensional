#include <cstdlib>
#include <ctime>
#include <iostream>

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

  datagen(500, 400, 100, 1000, 1000);
  datagen(800, 900, 100, 1000, 1000);
  datagen(1200, 1100, 100, 1000, 1000);
  // datagen(100, 50, 10, 1000, 1000);
  // datagen(200, 300, 10, 1000, 1000);
  // datagen(1300, 1500, 10, 1000, 1000);
  // datagen(1800, 1700, 10, 1000, 1000);
  // datagen(700, 700, 10, 1000, 1000);
  // datagen(2000, 1900, 10, 1000, 1000);
}