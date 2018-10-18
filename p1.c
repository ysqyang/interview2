int h(void* buf, size_t len) {
    int val = 0;
    for (int i = 0; i < len; i++) {
        /* concatenate all the bytes to form a number*/
        char byte_value = *((char*)buf + i);
        val = val*256 + (int)byte_value;
    } 

    return val%len;
}