import std.stdio : writeln;

void main()
{
    immutable double N = 1E7;
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
    writeln((hits / N) * 4);
}
