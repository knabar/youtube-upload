import getpass

import gdata.youtube
import gdata.youtube.service

from devkeys import YT_DEVKEY, YT_USERNAME


yt_service = gdata.youtube.service.YouTubeService()

yt_service.developer_key = YT_DEVKEY

yt_service.email = YT_USERNAME
yt_service.password = getpass.getpass(prompt='Password for %s: ' % YT_USERNAME)
yt_service.source = 'youtube-upload-test'
yt_service.ProgrammaticLogin()

