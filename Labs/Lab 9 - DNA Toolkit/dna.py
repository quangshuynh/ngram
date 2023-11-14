"""
Functions for manipulating DNA sequences using linked lists
file: dna.py
language: python3
author: Quang Huynh
"""

import immutable_extra as ie
import node_types as nt


def convert_to_nodes(dna_string):
    """
    Converts a string of DNA into one node in a sequence
    :param dna_string: Inputted string of DNA
    :return: A linked-node representing the inputted DNA sequence
    """
    if len(dna_string) == 0:
        return None
    else:
        node = nt.FrozenNode(dna_string[0], convert_to_nodes(dna_string[1:]))
    return node


def convert_to_string(dna_seq):
    """
    Converts linked lists of DNA into string using recursion
    :param dna_seq: A linked sequence of DNA nodes
    :return: The string value
    """
    if dna_seq is None:
        return ""
    else:
        return dna_seq.value + convert_to_string(dna_seq.next)


def length_rec(dna_seq):
    """
    Finds the length of a linked node using recursion
    :param dna_seq: A linked sequence of DNA nodes
    :return: The length of a linked node
    """
    if not dna_seq:
        return 0
    else:
        return 1 + length_rec(dna_seq.next)


def is_match(dna_seq1, dna_seq2):
    """
    Checks if two sequences are equal to each other
    :param dna_seq1: The first linked sequence of DNA
    :param dna_seq2: The second linked sequence of DNA
    :return: A boolean that states whether the DNA sequences match or not
    """
    if dna_seq1 is None and dna_seq2 is None:
        return True
    elif dna_seq1 is None or dna_seq2 is None:
        return False
    elif dna_seq1.value is not dna_seq2.value:
        return False
    else:
        return is_match(dna_seq1.next, dna_seq2.next)


def is_pairing(dna_seq1, dna_seq2):
    """
    Checks and determines if two DNA sequences form a valid pairing
    :param dna_seq1: The first linked sequence of DNA
    :param dna_seq2: The second linked sequence of DNA
    :return: True if sequences form a valid pairing, else False
    """
    if dna_seq1 is None and dna_seq2 is None:
        return True
    elif dna_seq1 is None or dna_seq2 is None:
        return False
    else:
        current = (
                dna_seq1.value == 'A' and dna_seq2.value == 'T' or
                dna_seq1.value == 'T' and dna_seq2.value == 'A' or
                dna_seq1.value == 'G' and dna_seq2.value == 'C' or
                dna_seq1.value == 'C' and dna_seq2.value == 'G'
        )
        if current:  # Checks if the end in the sequence is the same length
            return is_pairing(dna_seq1.next, dna_seq2.next)
        else:  # Return False if lengths are different
            return False


def substitute(dna_seq1, idx, base):
    """
    Performs a substitution mutation on a DNA sequence.
    :param dna_seq1: The original linked list of a DNA sequence
    :param idx: Index of the substitution
    :param base: The new linked list of a DNA sequence
    :return: The linked sequence after substitution mutation
    :raise: IndexError if idx is out of range
    """
    dna_seq1_length = length_rec(dna_seq1)
    if idx < 0 or idx > dna_seq1_length:
        raise IndexError("Invalid substitution index.")
    removed = ie.remove_at(idx, dna_seq1)  # Remove the element at the specified index
    substituted = ie.concatenate(removed, nt.FrozenNode(base, None))  # Concatenate the new base at the specified index
    return substituted


def insert_seq(dna_seq1, dna_seq2, idx):
    """
        Inserts the entire dna_seq2 before the specified index in dna_seq1
        :param dna_seq1: The first linked sequence of DNA for insertion mutation
        :param dna_seq2: The second linked sequence of DNA to be inserted
        :param idx: Index for insertion in dna_seq1
        :return: The linked sequence after the insertion
        :raise: IndexError if idx is out of range
        """
    if idx < 0:
        raise IndexError("Invalid insertion index")
    if idx == 0:
        if dna_seq2 is None:
            return dna_seq1
        else:
            return nt.FrozenNode(dna_seq2.value, insert_seq(dna_seq1, dna_seq2.next, idx))
    elif dna_seq1 is None and idx > 0:
        raise IndexError("Invalid insertion index")
    else:
        insert_next = insert_seq(dna_seq1.next, dna_seq2, idx - 1)  # Recursively insert into the rest of the sequence
        return nt.FrozenNode(dna_seq1.value, insert_next)


def delete_seq(dna_seq, idx, segment_size):
    """
    Deletes a segment of elements from the DNA sequence
    :param dna_seq: The linked sequence of DNA for deletion mutation
    :param idx: Index for deletion
    :param segment_size: Number of elements to be deleted
    :return: A new linked sequence representing DNA after deletion
    :raise: IndexError if combination of idx and segment_size is out of range
    """
    if idx < 0 or segment_size < 0:
        raise IndexError("Invalid deletion index or segment size.")
    if segment_size == 0:  # If deletion size is 0, return the original sequence
        return dna_seq
    seq_length = length_rec(dna_seq)
    if idx >= seq_length or idx + segment_size > seq_length:
        raise IndexError("Deletion index and size combination is out of range.")
    deleted = ie.remove_at(idx, dna_seq)  # Remove segment starting from specified index
    for i in range(segment_size - 1):  # Loop removal of remaining elements in segment
        deleted = ie.remove_at(idx, deleted)
    return deleted


def duplicate_seq(dna_seq, idx, segment_size):
    """
    Duplicates a segment of elements from the DNA sequence
    :param dna_seq: The linked sequence of DNA for duplication mutation
    :param idx: Index for duplication
    :param segment_size: Number of elements to be duplicated
    :return: A new linked sequence representing DNA after duplication
    :raise: IndexError if combination of idx and segment_size is out of range
    """
    if idx < 0 or segment_size < 0:
        raise IndexError("Invalid duplication index or segment size.")
        # If segment size is 0, duplication succeeds by default, return the original sequence
    if segment_size == 0:
        return dna_seq
    seq_length = length_rec(dna_seq)
    if idx >= seq_length or idx + segment_size > seq_length:
        raise IndexError("Duplication index and size combination is out of range.")
    # Extract the segment to duplicate
    segment_to_duplicate = ie.remove_at(idx, dna_seq)
    for i in range(segment_size - 1):
        segment_to_duplicate = ie.remove_at(idx, segment_to_duplicate)
    # Duplicate the segment using append
    duplicated_segment = ie.append(segment_to_duplicate, segment_to_duplicate)
    # Concatenate the duplicated segment back into the original sequence
    result = ie.concatenate(ie.remove_at(idx, dna_seq), duplicated_segment)
    return result
