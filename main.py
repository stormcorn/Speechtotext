import os
import asyncio
from dotenv import load_dotenv

from deepgram import (
    DeepgramClient,
    DeepgramClientOptions,
    LiveTranscriptionEvents,
    LiveOptions,
    Microphone
)
load_dotenv()

API_KEY=os.getenv("DEEPGRAM_API_KEY")

#https://developers.deepgram.com/docs/python-sdk-streaming-transcription
def get_transcript():

    try:
        # Configure the DeepgramClientOptions to enable KeepAlive for maintaining the WebSocket connection (only if necessary to your scenario)

        df_config = DeepgramClientOptions(
            options={
                "keepalive":"true"
            }
        )

        # Create a websocket connection using the DEEPGRAM_API_KEY from environment variables

        deepgram = DeepgramClient(API_KEY, df_config)
        
        # Create a websocket connection using the DEEPGRAM_API_KEY from environment variables

        dg_connection = deepgram.listen.asynclive.v("1")

        def message_on(self):
            pass
        def error_on(self):
            pass

        dg_connection.on(LiveTranscriptionEvents.Transcript, message_on)

        options = LiveOptions(
            
        )
        dg_connection.start(options)

        dg_connection.finish()


    except Exception as error:
        print(f"Failed to connected: {error}")
        return


if __name__=="__main__":
    asyncio.run(get_transcript())