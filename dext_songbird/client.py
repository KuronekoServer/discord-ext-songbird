from discord import VoiceProtocol
from .dext import VoiceConnector


class VoiceClient(VoiceProtocol):
    
    def __init__(self, client, channel):
        super().__init__(client, channel)
        self._connector = VoiceConnector()
