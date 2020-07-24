from django.conf import settings

APIMODE_SANDBOX = 'sandbox'
APIMODE_LIVE = 'live'

APIMODE_CHOICES = [
    (APIMODE_SANDBOX, 'Sandbox'),
    (APIMODE_LIVE, 'Live'),
]

PAYPAL_API_BASE_URL_SANDBOX = 'https://api.sandbox.paypal.com'
PAYPAL_API_BASE_URL_LIVE    = 'https://api.paypal.com'

if settings.PAYPAL_SUBSCRIPTIONS_MODE == 'sandbox':
    PAYPAL_API_BASE_URL = PAYPAL_API_BASE_URL_SANDBOX
elif settings.PAYPAL_SUBSCRIPTIONS_MODE == 'live':
    PAYPAL_API_BASE_URL = PAYPAL_API_BASE_URL_LIVE

PRODUCT_TYPE_PHYSICAL = 'PHYSICAL'
PRODUCT_TYPE_DIGITAL  = 'DIGITAL'
PRODUCT_TYPE_SERVICE  = 'SERVICE'

PRODUCT_TYPES = [
    (PRODUCT_TYPE_PHYSICAL, 'Physical'),
    (PRODUCT_TYPE_DIGITAL,  'Digital'),
    (PRODUCT_TYPE_SERVICE,  'Service'),
]

PLAN_STATUS_CREATED  = 'CREATED'
PLAN_STATUS_INACTIVE = 'INACTIVE'
PLAN_STATUS_ACTIVE   = 'ACTIVE'

PLAN_STATUS_CHOICES = [
    (PLAN_STATUS_CREATED, 'Created'),
    (PLAN_STATUS_INACTIVE, 'Inactive'),
    (PLAN_STATUS_ACTIVE, 'Active'),
]

SUBSCRIPTION_STATUS_APPROVAL_PENDING = 'APPROVAL_PENDING'
SUBSCRIPTION_STATUS_APPROVED         = 'APPROVED'
SUBSCRIPTION_STATUS_ACTIVE           = 'ACTIVE'
SUBSCRIPTION_STATUS_SUSPENDED        = 'SUSPENDED'
SUBSCRIPTION_STATUS_CANCELLED        = 'CANCELLED'
SUBSCRIPTION_STATUS_EXPIRED          = 'EXPIRED'

SUBSCRIPTION_STATUS_CHOICES = [
    (SUBSCRIPTION_STATUS_APPROVAL_PENDING, 'Approval pending'),
    (SUBSCRIPTION_STATUS_APPROVED,         'Approved'),
    (SUBSCRIPTION_STATUS_ACTIVE,           'Active'),
    (SUBSCRIPTION_STATUS_SUSPENDED,        'Suspended'),
    (SUBSCRIPTION_STATUS_CANCELLED,        'Cancelled'),
    (SUBSCRIPTION_STATUS_EXPIRED,          'Expired'),
]
