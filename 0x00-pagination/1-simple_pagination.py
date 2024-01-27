#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple
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

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """return a tuple of size two containing a
           start index and an end index
        """
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page of data"""
        raise_error = "Page must be a positive integer"
        assert isinstance(page, int) and page > 0, raise_error
        assert isinstance(page_size, int) and page_size > 0, raise_error
        res = self.index_range(page, page_size)
        start_index, end_index = res
        data = self.dataset()
        if start_index >= len(data):
            return []
        return data[start_index: end_index]
