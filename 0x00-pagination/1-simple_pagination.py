#!/usr/bin/env python3
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


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
        assert page > 0, page_size > 0
        is_page_int = isinstance(page, int)
        is_page_size_int = isinstance(page_size, int)
        raise_error = "when page and/or page_size are not ints"
        assert is_page_int and is_page_size_int, raise_error
        try:
            res = index_range(page, page_size)
            start_index, end_index = res
            dataset = self.dataset()
            return dataset[start_index: end_index]
        except IndexError:
            return []
