#!/usr/bin/env python3
"""Simple Pagination"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """Returns a tupple of size two containing a start
    index and an end index corresponding to the range of indexes
    to return in a list for those particular pagination params

    Args:
        page (int): _description_
        page_size (int): _description_

    Returns:
        Tuple: _description_
    """
    start = page_size * (page - 1)
    end = page_size * page
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
        """return the appriprate page of the dataset

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
            List[List]: _description_
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_idx, end_idx = index_range(page, page_size)

        # load dataset
        self.dataset()
        
        try:
            return self.__dataset[start_idx:end_idx]
        except IndexError:
            return []
