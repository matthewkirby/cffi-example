

double add(double x, double y) {
    return x+y;
}

double sum_array(double arr[], int length) {
    double sum = 0.0;
    int i = 0;
    for(i=0; i<length; i++) {
        sum += arr[i];
    }

    return sum;
}
