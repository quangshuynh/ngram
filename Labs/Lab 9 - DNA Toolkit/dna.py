"""
Functions for manipulating DNA sequences using linked lists
file: dna.py
language: python3
author: Quang Huynh
"""

import immutable_extra as ie
import node_types as nt

def convert_to_nodes(dna_string):
    if len(dna_string) == 0:
        return None
    else:
        node = nt.FrozenNode(dna_string[0], convert_to_nodes(dna_string[1:]))
    return node

def convert_to_string(dna_seq):
    if not dna_seq:
        return ""
    else:
        return dna_seq.value + convert_to_string(dna_seq.next)

def length_rec(dna_seq):
    if not dna_seq:
        return 0
    else:
        return 1 + length_rec(dna_seq.next)

def is_match(dna_seq1, dna_seq2):
    if dna_seq1 is None and dna_seq2 is None:
        return True
    elif dna_seq1 is None or dna_seq2 is None:
        return False
    elif dna_seq1.value is not dna_seq2.value:
        return False
    else:
        return is_match(dna_seq1.next, dna_seq2.next)

def is_pairing(dna_seq1, dna_seq2):
    pass

def substitute(dna_seq1, idx, base):
    pass

def insert_seq(dna_seq1, dna_seq2, idx):
    pass

def delete_seq(dna_seq, idx, segment_size):
    pass

def duplicate_seq(dna_seq, idx, segment_size):
    pass
