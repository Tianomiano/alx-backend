#!/usr/bin/env python3
"""
a function named index_range that takes,
two integer arguments page and page_size
"""
from typing import Tuple
import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        a method named get_page that takes two integer arguments page,
        with default value 1 and page_size with default value 10.
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]
