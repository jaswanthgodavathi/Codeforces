#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int k = 0; k < t; k++)
    {
        int ca = 0, cb = 0, cc = 0;
        char matrix[3][3];

        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                cin >> matrix[i][j];

                if (matrix[i][j] == 'A')
                {
                    ca += 1;
                }
                else if (matrix[i][j] == 'B')
                {
                    cb += 1;
                }
                else if (matrix[i][j] == 'C')
                {
                    cc += 1;
                }
            }
        }

        if (ca < 3)
        {
            cout << 'A' << endl;
        }
        else if (cb < 3)
        {
            cout << 'B' << endl;
        }
        else if (cc < 3)
        {
            cout << 'C' << endl;
        }
    }

    return 0;
}
