from typing import TypedDict, Optional


class CustomerEventPayload(TypedDict):
    customer_id: str
    event_kind: str
    region: str
    schema_version: str
    correlation_id: str


class OrderMessageSchema(TypedDict):
    order_id: str
    customer_id: str
    product_id: str
    quantity: int
    unit_price: float
    currency: str
    order_status: str


class ProducerEventMessage(TypedDict):
    producer_id: str
    topic: str
    partition_key: str
    event_timestamp: str
