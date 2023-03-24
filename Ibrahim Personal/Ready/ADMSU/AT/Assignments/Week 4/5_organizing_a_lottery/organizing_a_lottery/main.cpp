#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;
using namespace std;


vector<pair<int,int>> Merge_pair (vector<pair<int,int>> &a, vector<pair<int,int>> &b) {
    vector<pair<int,int>> c;

    while (a.size() > 0 && b.size() > 0) {
            if(a[0].first <= b[0].first) {
                c.push_back(a[0]);
                a.erase(a.begin());
                }
            else {
                c.push_back(b[0]);
                b.erase(b.begin());
                }
    }

    if(a.size() != 0) {
    for (size_t i=0; i<a.size(); i++) {
        c.push_back(a[i]);
    }
    }

    if(b.size() != 0) {
    for (size_t i=0; i<b.size(); i++) {
        c.push_back(b[i]);
    }
    }

    return c;
}

vector<pair<int,int>> MergeSort_pair(vector<pair<int,int>> &a, int left, int right) {
  if (left == right) return a;
  if (left == right - 1) return a;
  vector<pair<int,int>> a_bar;

  int mid = (a.size()/2);



  vector<pair<int,int>> b = vector<pair<int,int>> (a.begin(), a.begin() + mid);
  vector<pair<int,int>> c = vector<pair<int,int>> (a.begin() + mid , a.end());

  b = MergeSort_pair(b, 0, b.size());
  c = MergeSort_pair(c, 0, c.size());
  a_bar = Merge_pair(b,c);
  return a_bar;
}

vector<int> fast_count_segments(vector<int> starts, vector<int> ends, vector<int> points) {
  vector<int> cnt(points.size());
  //sorting points to correlate to the inputs
 // vector<int> cnt;
  int i = 0;
  int segments_counter = 0;
  //vector< vector<int> > matrix((starts.size()+ends.size()+points.size()), vector<int>(2));


   vector<pair<int,int>>matrix;

   for(i; i<starts.size(); i++) {
    matrix.push_back(make_pair(starts[i],-1));
   }
   for(i; i<starts.size()+ends.size(); i++) {
    matrix.push_back(make_pair(ends[i-starts.size()],-2));
   }
   for(i; i<starts.size()+ends.size()+points.size(); i++) {
    matrix.push_back(make_pair(points[i-starts.size()-ends.size()], i-(starts.size()+ends.size())));
    //matrix.push_back(make_pair(points[i-starts.size()-ends.size()], "p"));
   }


   /*
   std::vector<std::pair<int,int>> matrix(starts.size() + ends.size() + points.size());
   int c = 0;

   std::transform(points.cbegin(), points.cend(),
        std::transform(ends.cbegin(), ends.cend(),
            std::transform(starts.cbegin(), starts.cend(),
                matrix.begin(),
            [](int i) { return std::pair<int,int>{i, -1}; }),
        [](int i) { return std::pair<int,int>{i, -2}; }),
    [&c](int i) { return std::pair<int,int>{i, c++}; });
    */



   matrix.resize(starts.size()+ends.size()+points.size());

   matrix = MergeSort_pair(matrix, 0, matrix.size());

   for(int i=0; i<matrix.size(); i++) {
       if(matrix[i].second == -1)
       {
            segments_counter+=1;
       }

       else if(matrix[i].second == -2)
       {
            segments_counter-=1;
       }

       else{
            cnt[matrix[i].second] = segments_counter;
       }
   }

  return cnt;

}

vector<int> naive_count_segments(vector<int> starts, vector<int> ends, vector<int> points) {
  vector<int> cnt(points.size());
  for (size_t i = 0; i < points.size(); i++) {
    for (size_t j = 0; j < starts.size(); j++) {
      cnt[i] += starts[j] <= points[i] && points[i] <= ends[j];
    }
  }
  return cnt;
}

int main() {

  int n, m;
  n = 2;
  m = 3;
  //std::cin >> n >> m;
  vector<int> starts(n), ends(n);
  for (size_t i = 0; i < starts.size(); i++) {
    std::cin >> starts[i] >> ends[i];
  }
  vector<int> points(m);
  for (size_t i = 0; i < points.size(); i++) {
    std::cin >> points[i];
  }
  //use fast_count_segments


  //vector<int> cnt = naive_count_segments(starts, ends, points);


  vector<int> cnt = fast_count_segments(starts, ends, points);

  // cout << "Returned Values" << endl;
  for (size_t i = 0; i < cnt.size(); i++) {
    std::cout << cnt[i] << ' ';
  }

  //fast_count_segments(starts, ends, points);

}



