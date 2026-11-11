#include "Root.h"

@implementation Root
+ (id)alloc { return class_createInstance(self, 0); }
+ (id)new { return [[self alloc] init]; }
- (id)init { return self; }
- (void)free { object_dispose(self); }
- (BOOL)respondsTo:(SEL)selector {
    return class_respondsToSelector(object_getClass(self), selector);
}
@end
