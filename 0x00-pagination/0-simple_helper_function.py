#!/usr/bin/env python3
"""Simple Helper Function"""

from typing import Tuple


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
