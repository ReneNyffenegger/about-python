#!/usr/bin/python3

print("{} {} {}"                 .format(1, -17, 33)          ) #  1 -17 33
print("{:4d} {:4d} {:4d}"        .format(1, -17, 33)          ) #     1  -17   33
print("{:04d} {:04d} {:04d}"     .format(1, -17, 33)          ) #  0001 -017 0033

print("{:10s} {:10s}"            .format('foo', 'bar')        ) #  foo        bar
print("{:>10s} {:>10s}"          .format('foo', 'bar')        ) #         foo        bar

print("{:f} {:f}"                .format(22.390490903, -19.1) ) #  22.390491 -19.100000
print("{:6.2f} {:6.2f}"          .format(22.390490903, -19.1) ) #   22.39 -19.10
print("{:-6.2f} {:-6.2f}"        .format(22.390490903, -19.1) ) #   22.39 -19.10
print("{:+6.2f} {:+6.2f}"        .format(22.390490903, -19.1) ) #  +22.39 -19.10

print("foo: {foo} and bar: {bar}".format(foo=42.42, bar='baz')) # foo: 42.42 and bar: baz
