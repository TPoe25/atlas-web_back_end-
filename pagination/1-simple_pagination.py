#!/usr/bin/env python3
"""
Pagination implementation using index_range function.
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end indices for the given page number.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple of the start and end indices for the given page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    
    DATA_FILE = "Popular_Baby_Names.csv"
    
    def __init__(self):
        self.__dataset = None
        
    def dataset(self) -> List[List]:
        """
        Loads the dataset.

        Returns:
            List[List]: A list of the dataset rows.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        
        return self.__dataset
    
    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Gets the requested page from the dataset.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: The requested page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        
        return dataset[start_index:end_index] if start_index < len(dataset) else []
    