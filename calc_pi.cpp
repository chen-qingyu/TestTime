#include <iostream>

int main(void)
{
    const int N = 1E7;
    double x, y, hits = 0;
    for (x = 0; x * x < N; ++x)
    {
        for (y = 0; y * y < N; ++y)
        {
            if (x * x + y * y < N)
            {
                ++hits;
            }
        }
    }
    std::cout << ((hits / N) * 4) << std::endl;

    return 0;
}
