import random
import rx
from rx import operators as ops

def filternumbers(x):
   if isinstance(x, int) and x % 2 == 0:
      return x
   else:
      return None

numbers = range(1, 11)
source = rx.from_(numbers)

case1 = source.pipe(
   ops.filter(lambda c: filternumbers(c)),
   ops.map(lambda a: a * 2),
   ops.reduce(lambda acc, curr: acc + curr)
)

case1.subscribe(
   on_next=lambda i: print("Got - {0}".format(i)),
   on_error=lambda e: print("Error: {0}".format(e)),
   on_completed=lambda: print("Job Done!"),
)
