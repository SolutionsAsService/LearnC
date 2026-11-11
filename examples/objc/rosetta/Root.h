/* Root.h: a minimal root class over the GNU Objective-C runtime.
   On Apple platforms you would inherit from NSObject (Foundation) instead;
   Foundation is not part of this toolchain, so these few lines stand in. */
#include <objc/runtime.h>

__attribute__((objc_root_class))
@interface Root {
    Class isa;               /* every object begins with a pointer to its class */
}
+ (id)alloc;
+ (id)new;
- (id)init;
- (void)free;
- (BOOL)respondsTo:(SEL)selector;
@end
