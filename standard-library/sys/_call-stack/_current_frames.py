import sys

def print_frame(frames):
    frame_addr, frame = next(iter(frames.items()))

    print(f'Frame')
    print(f'  Address      : {frame_addr}')
    print(f'  Line No      : {getattr(frame, "f_lineno"       )}')
    print(f'  Back         : {getattr(frame, "f_back"         )}')
    print(f'  Locals       : {getattr(frame, "f_locals"       )}')
    print(f'  Trace        : {getattr(frame, "f_trace"        )}')
    print(f'  Trace        : {getattr(frame, "f_trace"        )}')
    print(f'  Last i       : {getattr(frame, "f_lasti"        )}')
    print('')


def h(i):

    print_frame(sys._current_frames())

def f(a):
    x = 42

    def g(b):
        x = 'hello world'

        h(b+3)
        print_frame(sys._current_frames())

    print_frame(sys._current_frames())
    g(a*2)

f(3)
