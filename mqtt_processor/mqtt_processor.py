from typing import List, Callable, Optional

import paho.mqtt.client as mqtt

from custom_logger import logging

logger = logging.getLogger(__name__)


class MQTTProcessor:
    def __init__(
            self,
            message_callback: Optional[Callable],
            topics_to_subscribe: List[str],
            host: str = "localhost",
            port: int = 1883,
            keepalive: int = 180
    ):
        logger.info("Initializing MQTT processor")
        self._topics = topics_to_subscribe

        try:
            self._client = mqtt.Client()

            self._client.on_connect = self._on_connect
            if message_callback:
                self._client.on_message = message_callback

            self._client.connect(host, port, keepalive)
        except OSError as e:
            logger.error("Error connecting to service", error=e)

    def _on_connect(self, client, userdata, flags, rc):
        logger.debug("Connecting to MQTT server, subscribing", client=client, userdata=userdata, flags=flags, rc=rc)
        for topic in self._topics:
            logger.debug("Subscribing", topic=topic)
            self._client.subscribe(topic)

    def publish(self, topic: str, message: str):
        logger.debug("Starting mqtt processing", topic=topic, message=message)
        self._client.publish(topic, message)

    def start_forever(self):
        logger.debug("Starting mqtt processing")
        self._client.loop_forever()

    def start(self):
        logger.debug("Starting mqtt processing")
        self._client.loop_start()

    def stop(self):
        logger.debug("Stopping mqtt processing")
        self._client.loop_stop()
