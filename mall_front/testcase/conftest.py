from interface.member import MemberInterface
from interface.cart import CartInterface
from interface.order import OrderInterface
import pytest

body = {
    "username": "ldk",
    "password": "123456"
}


@pytest.fixture(scope='session')
def headers():
    return MemberInterface().get_token(body)


@pytest.fixture()
def cart(headers):
    return CartInterface(headers)


@pytest.fixture()
def order(headers):
    return OrderInterface(headers)
