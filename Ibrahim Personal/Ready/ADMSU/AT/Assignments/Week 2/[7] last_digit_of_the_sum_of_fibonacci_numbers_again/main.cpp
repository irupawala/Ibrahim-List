#include <iostream>
#include <vector>
#include <stdlib.h>
using std::vector;
using namespace std;

long long get_fibonacci_partial_sum_naive(long long from, long long to) {
    long long sum = 0;

    long long current = 0;
    long long next  = 1;

    for (long long i = 0; i <= to; ++i) {
        if (i >= from) {
            sum += current;
        }

        long long new_current = next;
        next = next + current;
        current = new_current;
    }

    return sum % 10;
}

long long get_fibonacci_partial_sum(long long from, long long to) {

    int arr[60] = {};
    int fibonacci_from, fibonacci_to, sum_complete_loop = 0, total_sum = 0, loop = 0;
    int fibonacci_to_quotient, fibonacci_from_quotient;
    int sum_from_starting_element_to_loop_end = 0;
    int sum_from_start_loop_to_end_element = 0;

    // To make sure from < to
    if (from > to) {
        from = to;
        to = from;
    } else {
        from = from;
        to = to;
    }

    // To find the last element in the array
    fibonacci_to = to%60;
    fibonacci_from = from%60;

    // To find the number of times sum of entire loop should be added.
    fibonacci_to_quotient = to/60;
    fibonacci_from_quotient = from/60;

    if (fibonacci_to_quotient > fibonacci_from_quotient)
        loop = fibonacci_to_quotient - fibonacci_from_quotient - 1;
    else
        loop = fibonacci_to_quotient - fibonacci_from_quotient;


    // To generate the repetitive array
    for (int i=0; i <= 59; i++) {
        if (i<2)
            arr[i] = i;
        else {
                arr[i] = arr[i-2]%10 + arr[i-1]%10;
                arr[i] = arr[i] % 10;
        }
        //cout << "arr[" << i << "]" << arr[i] << endl;
    }

    // sum of an entire loop
    for (int i = 0; i <= 59; i++) {
        sum_complete_loop += arr[i];
        sum_complete_loop %= 10;
    }

    // sum from start element to end of loop
    for (int i = fibonacci_from; i <= 59; i++) {
        sum_from_starting_element_to_loop_end += arr[i];
        sum_from_starting_element_to_loop_end %= 10;
    }

    // sum from start of loop to end element
    for (int i = 0; i <= fibonacci_to; i++) {
        sum_from_start_loop_to_end_element += arr[i];
        sum_from_start_loop_to_end_element %= 10;
    }

    total_sum = sum_from_starting_element_to_loop_end + (loop * sum_complete_loop) + sum_from_start_loop_to_end_element;

    //cout << "sum_from_starting_element_to_loop_end = " << sum_from_starting_element_to_loop_end << endl;
    //cout << "sum_from_start_loop_to_end_element = " << sum_from_start_loop_to_end_element << endl;
    //cout << "loop = " << loop << endl;
    //cout << "sum_complete_loop = " << sum_complete_loop << endl;
    return total_sum%10;


}

int stress_test() {

    while (true) {
        int rand_1 = rand() % 20;
        int rand_2 = rand() % 20 + rand_1;
        cout << "rand_1 = " << rand_1 << endl;
        cout << "rand_2 = " << rand_2 << endl;

        long long res1 = get_fibonacci_partial_sum_naive(rand_1, rand_2);
        long long res2 = get_fibonacci_partial_sum(rand_1, rand_2);

        if (res1 != res2) {
            cout << "Wrong answer: " << res1 << ' ' << res2 << endl;
            break;
        }
        else {
            cout << "OK" << endl;
        }
    }
}

int main() {
    long long from, to;
    std::cin >> from >> to;
    //std::cout << get_fibonacci_partial_sum_naive(from, to) << '\n';
    std::cout << get_fibonacci_partial_sum(from, to) << '\n';
    //stress_test();
}
