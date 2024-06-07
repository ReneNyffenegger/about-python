#!/usr/bin/env python3

import curses
import time

def parse_diskstats(file_path="/proc/diskstats"):

    diskstats=open(file_path, 'r').readlines()

    headers = [
      # "major_number", "minor_number",
        "device_name", "reads_completed", "reads_merged", "sectors_read", "time_reading",
        "writes_completed", "writes_merged", "sectors_written", "time_writing",
        "io_in_progress", "time_io", "weighted_time_io",
        "discards_completed", "discards_merged", "sectors_discarded", "time_discarding",
        "flush_requests", "time spent flushing"
    ]

    all_stats = []
    for line in diskstats:
        all_fields         = line.split()
      # Remove major and minor number, they're not too interesting.
        interesting_fields = all_fields
        device_stats       = dict(zip(headers, interesting_fields))
        all_stats.append(device_stats)

    return headers, all_stats

def curses_out(stdscr, headers, all_stats):
    global r

    def write_num(lin, col, wid, num):
        stdscr.addstr(lin, col, num.rjust(wid))
        return col+wid

    for line, dev_stats in enumerate(all_stats, start=1):
        column = 8

        stdscr.addstr(     line,      1    , dev_stats['device_name'        ])     # Necessary in the first pass only, but for the moment, that's ok

        column = write_num(line, column, 11, dev_stats['reads_completed'    ])
        column = write_num(line, column, 11, dev_stats['reads_merged'       ])
        column = write_num(line, column, 11, dev_stats['sectors_read'       ])
        column = write_num(line, column, 11, dev_stats['time_reading'       ])
        column = write_num(line, column, 11, dev_stats['writes_completed'   ])
        column = write_num(line, column, 11, dev_stats['writes_merged'      ])
        column = write_num(line, column, 11, dev_stats['sectors_written'    ])
        column = write_num(line, column, 11, dev_stats['time_writing'       ])
        column = write_num(line, column,  8, dev_stats['io_in_progress'     ])
        column = write_num(line, column, 11, dev_stats['time_io'            ])
        column = write_num(line, column, 11, dev_stats['weighted_time_io'   ])
        column = write_num(line, column,  7, dev_stats['discards_completed' ])
        column = write_num(line, column,  8, dev_stats['discards_merged'    ])
        column = write_num(line, column,  9, dev_stats['sectors_discarded'  ])
        column = write_num(line, column,  5, dev_stats['time_discarding'    ])
        column = write_num(line, column,  8, dev_stats['flush_requests'     ])
        column = write_num(line, column,  9, dev_stats['time spent flushing'])

        stdscr.refresh()

    time.sleep(1)


def run(stdscr):
    stdscr.clear()
    while True:
       headers, all_stats = parse_diskstats()

       curses_out(stdscr, headers, all_stats)

curses.wrapper(run)
