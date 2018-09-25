

double add(double x, double y) {
    return x+y;
}

double sum_array(double arr[], int length) {
    double sum = 0.0;
    int i = 0;
    for(i=0; i<length; i++) {
        sum = add(sum, arr[i]);
    }

    return sum;
}

double secret_increment(double x) {
    return x + 1.0;
}

double do_things(double arr[], int length) {
    int i = 0; 
    for(i=0; i<length; i++) {
        arr[i] = secret_increment(arr[i]);
    }

    double sum = sum_array(arr, length);

    return sum;
}
