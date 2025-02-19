#include <stdlib.h> // malloc, free
#include <string.h> // strlen.
#include <stdio.h> // printf

typedef struct Point {
    int x;
    int y;
} Point;

void changeX5 (Point *pt) {
    pt = 55;
}

int main() {
  Point *my_pt = calloc(1, sizeof(Point));
  changeX5(my_pt);
  printf("%d\n", my_pt->x);
}