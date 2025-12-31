"""
Simple logger utility
"""

import logging

def get_logger(name: str, trace_id: str):
    logger = logging.getLogger(f"{name}_{trace_id}")
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger
