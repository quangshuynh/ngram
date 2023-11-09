"""
Functions for manipulating DNA sequences using linked lists
file: dna.py
language: python3
author: Quang Huynh
"""

import immutable_extra as ie
import node_types as nt

def convert_to_nodes(dna_string):
    if not dna_string:
        return None
    else:
        head = nt.MutableNode(dna_string[0], None)
        current = head
        for i in dna_string[1:]:
            copy = nt.MutableNode(i, None)
            current.next = copy
            current = current.next
        return head

def convert_to_string(dna_seq):
    pass

def length_rec(dna_seq):
    pass

def is_match(dna_seq1, dna_seq2):
    pass

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
