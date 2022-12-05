pragma circom 2.0.0;

template Multiplier(){

    signal input a;
    signal input b;
    signal input c;
    signal input d;
    signal output out;

    //Constraints
    a + b === c;
    b * c === d;
    out <== c + d;
}
component main = Multiplier();