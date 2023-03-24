
     while (true) {

        int n = rand() % 10;
        cout << n << endl;
        vector<int> a(n);
        for (size_t i = 0; i < a.size(); i++) {
                a[i] = rand() % 100;
        }

        for (size_t i = 0; i < a.size(); i++) {
                cout << a[i] << ' ';
        }
        cout << endl;

        int m = rand() % 10;
        cout << m << endl;
        vector<int> b(m);
        for (size_t i = 0; i < b.size(); i++) {
                b[i] = rand() % 100;
        }

        for (size_t i = 0; i < b.size(); i++) {
                cout << b[i] << ' ';
        }
        cout << endl;

        for (int i = 0; i < m; ++i) {
        int res1 = linear_search(a, b[i]);
        int res2 = binary_search(a, b[i]);


        if (res1 != res2) {
            cout << "Wrong answer: " << res1 << ' ' << res2 << endl;
            break;
        }
        else {
            cout << "OK" << endl;
        }

        }
    }

