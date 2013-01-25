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


title = 'MRI Stack'
description = 'Volume rendering of ImageJ\'s "MRI Stack" sample dataset.'
keywords = 'sample, mri'

# prepare a media group object to hold our video's meta-data
my_media_group = gdata.media.Group(
    title=gdata.media.Title(text=title),
    description=gdata.media.Description(description_type='plain',
                                        text=description),
    keywords=gdata.media.Keywords(text=keywords),
    category=[gdata.media.Category(
      text='Tech',
      scheme='http://gdata.youtube.com/schemas/2007/categories.cat',
      label='Science & Technology')],
    player=None
)

# create the gdata.youtube.YouTubeVideoEntry to be uploaded
video_entry = gdata.youtube.YouTubeVideoEntry(media=my_media_group)

# set the path for the video file binary
video_file_location = 'samples/mri-stack.mov'

print "Uploading"

new_entry = yt_service.InsertVideoEntry(video_entry, video_file_location)

print "Done"
