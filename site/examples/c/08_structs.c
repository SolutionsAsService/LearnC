#include <stdio.h>

struct Person {
    char name[50];
    int age;
};

static void birthday(struct Person *p) {
    p->age++;                     /* -> is (*p).age */
}

int main(void) {
    struct Person person1 = {"John", 30};
    birthday(&person1);
    printf("Name: %s\n", person1.name);
    printf("Age: %d\n", person1.age);
    printf("sizeof(struct Person) = %zu bytes\n", sizeof person1);
    return 0;
}
