#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """
    Server class for paginating and managing a database of popular baby names.

    Class that gives functionality to load, cache, n paginate data a CSV file
    containing popular baby names. Includes deletion-resilient pagination 

    Attributes:
        DATA_FILE (str): Path to the CSV file containing baby names data.
        __dataset (List[List]): Private cache of the loaded dataset.
        __indexed_dataset (Dict[int, List]): Private cache of indexed dataset.

    Methods:
        dataset(): Returns the cached dataset.
        indexed_dataset(): Returns the dataset indexed by position.
        get_hyper_index(index, page_size): Returns paginated data
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """Get a page of data with deletion-resilient pagination."""
        assert 0 <= index < len(self.indexed_dataset())

        data = []
        next_index = index
        dataset = self.indexed_dataset()

        # Gather data for the current page
        while len(data) < page_size and next_index < len(dataset):
            if next_index not in dataset:
                next_index += 1
                continue
            data.append(dataset[next_index])
            next_index += 1

        # Determine the next index for the following page
        while next_index < len(dataset) and next_index not in dataset:
            next_index += 1

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
