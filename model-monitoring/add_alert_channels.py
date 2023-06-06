from qwak_proto import wire_dependencies
from qwak.alerting.alerting_registry_client import AlertingRegistryClient
from qwak.alerting.channel import SlackChannel, Channel

wire_dependencies()


def set_session(env_name: str):
    """
    Sets the working environment for this session
    """
    from qwak_proto.di_configuration.session import Session
    Session().set_environment(env_name)


def add_slack_channel(api_url: str, channel_name: str):
    """
    Adds a new Slack channel to Qwak
    """
    client = AlertingRegistryClient()
    slack = SlackChannel(
        api_url=api_url
    )
    channel = Channel(
        name=channel_name,
        channel_conf=slack
    )
    client.create_alerting_channel(channel)


if __name__ == '__main__':
    """
    Use this script to add new Slack channels to receive model monitoring alerts
    """

    # Optionally set a different remove environment
    # set_session("daisy")

    # This URL should be your Webhook URL provided from Slack
    SLACK_API_URL = "<your-slack-webhook-url>"
    # The Slack channel where alerts are received
    SLACK_CHANNEL_NAME = "monitor-alerts"

    add_slack_channel(
        api_url=SLACK_API_URL,
        channel_name=SLACK_CHANNEL_NAME
    )
