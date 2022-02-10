from continuum.transforms.custom import BackgroundSwap
from continuum.datasets import CIFAR10
from continuum.datasets import MNIST
import torchvision
from continuum.scenarios import TransformationIncremental
from matplotlib import pyplot as plt
import pytest


@pytest.mark.slow
def test_background_swap_numpy():
    mnist = MNIST("MNIST_DATA", download=True, train=True)
    cifar = CIFAR10("CIFAR10_DATA", download=True, train=True)

    bg_swap = BackgroundSwap(cifar, input_dim=(28, 28))

    im = mnist.get_data()[0][0]
    im = bg_swap(im)

    # Uncomment for debugging
    # plt.imshow(im, interpolation='nearest')
    # plt.show()

@pytest.mark.slow
def test_background_swap_torch():
    cifar = CIFAR10("CIFAR10_DATA", download=True, train=True)

    mnist = torchvision.datasets.MNIST('./TorchMnist/', train=True, download=True,
                                       transform=torchvision.transforms.Compose([
                                           torchvision.transforms.ToTensor()
                                       ]))

    bg_swap = BackgroundSwap(cifar, input_dim=(28, 28))
    im = mnist[0][0]
    im = bg_swap(im)

    # Uncomment for debugging
    # plt.imshow(im.permute(1, 2, 0), interpolation='nearest')
    # plt.show()


def test_transform_incremental_bg_swap():
    pass
