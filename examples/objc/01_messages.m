#include "Root.h"
#include <stdio.h>

@interface Lamp : Root {
    int on;
}
- (id)toggle;
- (int)isOn;
@end

@implementation Lamp
- (id)toggle { on = !on; return self; }
- (int)isOn { return on; }
@end

int main(void) {
    Lamp *lamp = [Lamp new];
    [[lamp toggle] toggle];           /* messages chain: each returns self */
    [lamp toggle];
    printf("lamp is %s\n", [lamp isOn] ? "on" : "off");

    Lamp *nobody = nil;
    printf("message to nil returns %d\n", [nobody isOn]);  /* no crash */
    [lamp free];
    return 0;
}
