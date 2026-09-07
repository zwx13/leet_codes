int reverseBits(int n) {
    unsigned char bit = 0;
    int constructed = 0;
    for(size_t i = 0; i < 31; ++i){
        bit = n & 1;
        n >>= 1;
        constructed += bit;
        constructed <<= 1;
    }
    bit = n & 1;
    constructed += bit;
    
    return constructed;
}