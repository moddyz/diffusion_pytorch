from dataclasses import dataclass

from typing import Tuple

import torch


def get_optimal_device():
    """Pick the optimal device based in the current environment.

    Returns:
        torch.device
    """
    if torch.cuda.is_available():
        return torch.device("cuda")
    elif torch.backends.mps.is_available():
        return torch.device("mps")
    else:
        return torch.device("cpu")


@dataclass
class HyperParameters:
    """Global parameters used for configuring the model"""

    """Number of images processed in parallel"""
    batch_size: int = 64

    """Number of iterations to train the model."""
    train_iters: int = 100

    """Image size"""
    image_size: Tuple[int, int] = (64, 64)

    """The learning rate"""
    learning_rate: float = 3e-5

    """Total number of time steps for the diffusion process,
    which takes an input image all the way to pure gaussian noise."""
    num_time_steps: int = 1000

    """Number of values used to represent a time step embedding."""
    time_embed_dim = 32

    """Device to use."""
    device = get_optimal_device()
