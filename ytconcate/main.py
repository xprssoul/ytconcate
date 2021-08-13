from ytconcate.pipeline.steps.get_video_list import GetVideoList
from ytconcate.pipeline.steps.download_captions import DownloadCaptions
from ytconcate.pipeline.steps.preflight import Preflight
from ytconcate.pipeline.steps.postflight import Postflight
from ytconcate.pipeline.steps.step import StepException
from ytconcate.utils import Utils

from ytconcate.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }
    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        Postflight()
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
