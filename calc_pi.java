class calc_pi {
    public static void main(String[] args) {
        final double N = 1E7;
        double x, y, hits = 0;
        for (x = 0; x * x < N; ++x) {
            for (y = 0; y * y < N; ++y) {
                if (x * x + y * y < N) {
                    ++hits;
                }
            }
        }
        System.out.println((hits / N) * 4);
    }
}
