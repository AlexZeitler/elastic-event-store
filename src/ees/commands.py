from collections import namedtuple
from os import name
from typing import NamedTuple

Version = namedtuple('Version', [])

Commit = namedtuple(
    'Commit',
    ['stream_id',
     'expected_last_changeset',
     'expected_last_event',
     'events',
     'metadata'])

FetchStreamChangesets = namedtuple(
    'FetchStreamChangesets',
    ['stream_id',
     'from_changeset',
     'to_changeset'])

FetchStreamEvents = namedtuple(
    'FetchStreamEvents',
    ['stream_id',
     'from_event',
     'to_event'])

FetchGlobalChangesets = namedtuple(
    'FetchGlobalChangesets',
    ['checkpoint',
     'limit'])
    
FetchGlobalEvents = namedtuple(
    'FetchGlobalEvents',
    ['checkpoint',
     'event_in_checkpoint',
     'limit'])

AssignGlobalIndexes = namedtuple(
    'AssignGlobalIndexes', ['changesets'])