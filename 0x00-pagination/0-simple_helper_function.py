#!/usr/bin/env python3
"""
a function named index_range that takes,
two integer arguments page and page_size
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of start and end indexes for a given page and page size.
    Page numbers are 1-indexed.

    :param page: The page number (1-indexed).
    :param page_size: The size of each page.
    :return: A tuple containing start and end indexes.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
