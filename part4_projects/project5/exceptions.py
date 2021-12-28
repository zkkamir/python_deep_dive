from datetime import datetime
from http import HTTPStatus
import json


class WidgetException(Exception):
    """Base exception class for widget application."""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'API exception occurred.'
    user_err_msg = 'We are sorry. An unexpected error occurred on our end.'

    def __init__(self, *args, user_err_msg):
        if args:
            self.internal_err_msg = args[0]
            super().__init__(*args)
        else:
            super().__init__(self.internal_err_msg)

        if user_err_msg is not None:
            self.user_err_msg = user_err_msg

    def to_json(self):
        err_object = {'status': self.http_status, 'message': self.user_err_msg}
        return json.dumps(err_object)

    def log_exception(self):
        exception = {
            'type': type(self).__name__,
            'http_status': self.http_status,
            'message': self.args[0] if self.args else self.internal_err_msg,
            'args': self.args[1:]
        }
        print(f'EXCEPTION: {datetime.utcnow().isoformat()}: {exception}')


class SupplierException(WidgetException):
    """Generic supplier exception."""


class NotManufacturedAnyMoreException(SupplierException):
    """Not manufactured anymore exception."""


class ProductionDelayedException(SupplierException):
    """Production delayed exception."""


class ShippingDelayedException(SupplierException):
    """Shipping delayed exception."""


class CheckoutException(WidgetException):
    """Generic checkout exception."""


class InventoryTypeException(CheckoutException):
    """Inventory type exception."""


class OutOfStockException(InventoryTypeException):
    """Out of stock exception."""


class PricingException(CheckoutException):
    """Pricing exception."""


class InvalidCouponCode(PricingException):
    """Invalid coupon code exception."""
    http_status = HTTPStatus.BAD_REQUEST
    internal_err_msg = 'Bad.'
    user_err_msg = 'Not Good.'


class CanNotStackCouponException(PricingException):
    """Can not stack coupon exceotion."""
    http_status = HTTPStatus.BAD_REQUEST
    internal_err_msg = 'Bad.'
    user_err_msg = 'Not Good.'
