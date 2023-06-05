from qwak_proto import wire_dependencies
from qwak.alerting.alerting_registry_client import AlertingRegistryClient
from qwak.alerting.channel import SlackChannel, Channel

wire_dependencies()

# from qwak_proto.di_configuration.session import Session
# Session().set_environment("daisy")


def add_slack_channel(channel_name: str, webhook_url: str):
    client = AlertingRegistryClient()
    slack = SlackChannel(
        api_url=webhook_url
    )
    channel = Channel(
        name=channel_name,
        channel_conf=slack
    )
    client.create_alerting_channel(channel)


if __name__ == '__main__':
    SLACK_CHANNEL_NAME = "monitor-alerts"
    SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"
    add_slack_channel(channel_name=SLACK_CHANNEL_NAME,
                      webhook_url=SLACK_WEBHOOK_URL)
