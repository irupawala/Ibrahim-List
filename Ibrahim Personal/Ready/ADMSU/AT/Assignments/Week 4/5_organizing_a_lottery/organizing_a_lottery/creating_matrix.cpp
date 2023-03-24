#include <iostream>
#include <vector>

using std::vector;
using namespace std;


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


   cout << "Output Matrix" << endl;
   for(int i=0; i<matrix.size(); i++) {
    cout << matrix[i].first << " " << matrix[i].second << endl;
    }



}


int main() {

  int n, m;
  std::cin >> n >> m;
  vector<int> starts(n), ends(n);
  for (size_t i = 0; i < starts.size(); i++) {
    std::cin >> starts[i] >> ends[i];
  }
  vector<int> points(m);
  for (size_t i = 0; i < points.size(); i++) {
    std::cin >> points[i];
  }


  fast_count_segments(starts, ends, points);

}
