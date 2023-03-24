#include <iostream>

int get_change(int m) {

  int total_sum = m;
  int no_of_coins = 0;

    if(total_sum/10 > 0) {
        no_of_coins += total_sum/10;
        total_sum = total_sum - (total_sum/10) * 10;
    }
    if(total_sum/5 > 0) {
        no_of_coins += total_sum/5;
        total_sum = total_sum - (total_sum/5) * 5;
    }
    if(total_sum > 0) {
        no_of_coins += total_sum;
    }
return (no_of_coins);

}

int main() {
  int m;
  std::cin >> m;
  std::cout << get_change(m) << '\n';
}
