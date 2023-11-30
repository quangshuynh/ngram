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
    if len(dna_string) == 0:  # When length of string is 0, return None
        return None
    else:  # Recursively convert string into nodes
        node = nt.FrozenNode(dna_string[0], convert_to_nodes(dna_string[1:]))
    return node


def convert_to_string(dna_seq):
    """
    Converts linked lists of DNA into string using recursion
    :param dna_seq: A linked sequence of DNA nodes
    :return: The string value
    """
    if dna_seq is None:  # If sequence is empty, return empty string
        return ""
    else:  # Recursively convert nodes to strings
        return dna_seq.value + convert_to_string(dna_seq.next)


def length_rec(dna_seq):
    """
    Finds the length of a linked node using recursion
    :param dna_seq: A linked sequence of DNA nodes
    :return: The length of a linked node
    """
    if dna_seq is None:  # Return 0 when at the end of a sequence
        return 0
    else:  # Recursively add 1
        return length_rec(dna_seq.next) + 1


def is_match(dna_seq1, dna_seq2):
    """
    Checks if two sequences are equal to each other
    :param dna_seq1: The first linked sequence of DNA
    :param dna_seq2: The second linked sequence of DNA
    :return: A boolean that states whether the DNA sequences match or not
    """
    if dna_seq1 is None and dna_seq2 is None:  # If endings are the same
        return True
    elif dna_seq1 is None or dna_seq2 is None:  # If endings not are the same
        return False
    elif dna_seq1.value != dna_seq2.value:  # Compares if the values of sequences are equal
        return False
    else:  # Recursive call
        return is_match(dna_seq1.next, dna_seq2.next)


def is_pairing(dna_seq1, dna_seq2):
    """
    Checks and determines if two DNA sequences form a valid pairing
    :param dna_seq1: The first linked sequence of DNA
    :param dna_seq2: The second linked sequence of DNA
    :return: True if sequences form a valid pairing, else False
    """
    if dna_seq1 is None and dna_seq2 is None:  # When endings are the same
        return True
    elif dna_seq1 is None or dna_seq2 is None:  # If ending is not the same
        return False
    else:
        current = (  # Valid pairings
                dna_seq1.value == 'A' and dna_seq2.value == 'T' or
                dna_seq1.value == 'T' and dna_seq2.value == 'A' or
                dna_seq1.value == 'G' and dna_seq2.value == 'C' or
                dna_seq1.value == 'C' and dna_seq2.value == 'G')
        if current:  # Checks if ending in sequences are equal length
            return is_pairing(dna_seq1.next, dna_seq2.next)
        else:  # If pairing is not valid or equal length
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
    if idx == 0:  # Base case
        removed = ie.remove_at(0, dna_seq1)  # Remove the element at the specified index
        return ie.concatenate(nt.FrozenNode(base, None), removed)  # Concatenate the new base at the specified index
    elif dna_seq1 is None:  # Error handle
        raise IndexError("Invalid substitution index\n" +
                         "Index " + str(idx) + " is out of range for substitution")
    else:  # Recursive case
        substituted = substitute(dna_seq1.next, idx - 1, base)
        return nt.FrozenNode(dna_seq1.value, substituted)


def insert_seq(dna_seq1, dna_seq2, idx):
    """
        Inserts the entire dna_seq2 before the specified index in dna_seq1
        :param dna_seq1: The first linked sequence of DNA for insertion mutation
        :param dna_seq2: The second linked sequence of DNA to be inserted
        :param idx: Index for insertion in dna_seq1
        :return: The linked sequence after the insertion
        :raise: IndexError if idx is out of range
        """
    if idx == 0:  # Base case
        if dna_seq2 is None:
            return dna_seq1
        else:
            return nt.FrozenNode(dna_seq2.value, insert_seq(dna_seq1, dna_seq2.next, idx))
    if idx < 0:  # Error handle
        raise IndexError("Invalid insertion index\n" +
                         "Index " + str(idx) + " is less than 0")
    elif dna_seq1 is None:  # Error handle
        raise IndexError("Invalid insertion index\n" +
                         "Index " + str(idx) + " is an invalid insertion index")
    elif dna_seq2 is None and idx > 0:  # If dna_seq2 is empty, then continue with dna_seq1
        return nt.FrozenNode(dna_seq1.value, dna_seq1.next)
    else:  # Recursive case
        inserted = insert_seq(dna_seq1.next, dna_seq2, idx - 1)
        return nt.FrozenNode(dna_seq1.value, inserted)


def delete_seq(dna_seq, idx, segment_size):
    """
    Deletes a segment of elements from the DNA sequence
    :param dna_seq: The linked sequence of DNA for deletion mutation
    :param idx: Index for deletion
    :param segment_size: Number of elements to be deleted
    :return: A new linked sequence representing DNA after deletion
    :raise: IndexError if combination of idx and segment_size is out of range
    """
    if segment_size == 0:  # If deletion size is 0, return the original sequence
        return dna_seq
    if idx < 0 or segment_size < 0:  # Error handle
        raise IndexError("Invalid deletion index/segment size.\n" +
                         "Index " + str(idx) + " or segment size " +
                         str(segment_size) + " is less than 0")
    seq_length = length_rec(dna_seq)
    if idx >= seq_length or idx + segment_size > seq_length:  # Error handle
        raise IndexError("Invalid deletion index & size combination.\n" +
                         "Index " + str(idx) + " is less than " + str(seq_length) +
                         "\nor" + "\nIndex " + str(idx) + " + " + "segment size " +
                         str(segment_size) + " is less than " + str(seq_length))
    deleted = ie.remove_at(idx, dna_seq)  # Remove segment starting from specified index
    for i in range(segment_size - 1):  # Loop removal of remaining elements in segment
        deleted = ie.remove_at(idx, deleted)
    return deleted


def duplicate_seq(dna_seq, idx, segment_size, dup=None):
    """
    Duplicates a segment of elements from the DNA sequence
    :param dna_seq: The linked sequence of DNA for duplication mutation
    :param idx: Index for duplication
    :param segment_size: Number of elements to be duplicated
    :param dup: Accumulator for duplicated elements
    :return: A new linked sequence representing DNA after duplication
    :raise: IndexError if combination of idx and segment_size is out of range
    """
    if segment_size == 0:  # Base case
        return insert_seq(dna_seq, dup, idx)
    elif dna_seq is None:  # Error handle
        raise IndexError("Invalid duplication index\n" +
                         "Index " + str(idx) + " is an invalid duplication index")
    elif idx == 0:  # If index is 0 and if segment size is not 0
        if segment_size != 0:  # Append the duplicate segment to dup
            appended = duplicate_seq(dna_seq.next, idx, segment_size - 1, ie.append(dup, dna_seq.value))
            return nt.FrozenNode(dna_seq.value, appended)
    else:  # Recursive case
        duplicated = duplicate_seq(dna_seq.next, idx - 1, segment_size)
        return nt.FrozenNode(dna_seq.value, duplicated)
