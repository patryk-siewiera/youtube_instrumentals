from youtube_dl import YoutubeDL
import pprint
import PySimpleGUI as sg

# import youtube_dl
results_dictionary = {'abr': 160,
                      'acodec': 'opus',
                      'age_limit': 0,
                      'album': None,
                      'alt_title': 'Flume feat. Toro y Moi - The Difference [Official Lyric Video]',
                      'annotations': None,
                      'artist': 'Flume feat. Toro y Moi',
                      'automatic_captions': {},
                      'average_rating': 4.9602461,
                      'categories': ['Music'],
                      'channel_id': 'UCXAhoI7XO2kafTMjocm0jCg',
                      'channel_url': 'http://www.youtube.com/channel/UCXAhoI7XO2kafTMjocm0jCg',
                      'chapters': None,
                      'creator': 'Flume feat. Toro y Moi',
                      'description': 'Flume feat. Toro y Moi - The Difference (Official Music Video '
                                     'directed by Jonathan Zawada)\n'
                                     '\n'
                                     'Subscribe to the Flume YouTube channel: '
                                     'https://flu.me/YouTube\n'
                                     '\n'
                                     'We made this song between a day at my place in LA and and a '
                                     'day at Chaz’s spot in Oakland. This was our first time '
                                     'working together, I’ve been a Toro Y Moi fan for a while. His '
                                     'song Talamak is a longtime favorite. I listened to that one a '
                                     'lot when I first started Flume as a project.\n'
                                     '-Harley\n'
                                     '\n'
                                     "'The Difference' feat. Toro y Moi out now: "
                                     'https://flu.me/TheDifference\n'
                                     'Spotify: https://flu.me/TheDifference/Spotify\n'
                                     'Apple Music: https://flu.me/TheDifference/AppleMusic\n'
                                     'Amazon: https://flu.me/TheDifference/AZ\n'
                                     '\n'
                                     'Credits:\n'
                                     'Director: Jonathan Zawada\n'
                                     'Production Company: Ways & Means\n'
                                     'Executive Producers: Lana Kim & Jett Steiger\n'
                                     'Producer: Sloane Skala\n'
                                     '\n'
                                     'Director of Photography: Frank Mobilio\n'
                                     'Production Designer: Sean Genrich\n'
                                     'Wardrobe Stylist: Laura Francis\n'
                                     'Hair & Makeup: Amy Marie Wilson\n'
                                     '\n'
                                     'Post Producer: Grant Keiner\n'
                                     'Edit & VFX: Jonathan Zawada\n'
                                     'Color: Ethos, Kaitlyn Batiselli\n'
                                     '\n'
                                     'Special thanks to extras Michelle Manfre, Zilah Drahn, Faye '
                                     'Wellman, Otto Rasch, Erik McLay, Jay Ryves, Alex Mars, Mylen '
                                     'Walker & Percy.\n'
                                     '\n'
                                     'Mixed by Eric J Dubowsky\n'
                                     'Mastered by Matt Colon\n'
                                     '\n'
                                     'Follow Flume\n'
                                     'Facebook: http://flu.me/facebook\n'
                                     'Instagram: http://flu.me/Instagram\n'
                                     'Twitter: http://flu.me/twitter\n'
                                     'YouTube: https://flu.me/YouTube\n'
                                     'Spotify: https://flu.me/Essentials\n'
                                     'Apple Music: https://flu.me/AppleMusic\n'
                                     '\n'
                                     'Follow Toro y Moi\n'
                                     'Facebook: https://facebook.com/toroymoi\n'
                                     'Instagram: https://instagram.com/toroymoi\n'
                                     'Twitter: https://twitter.com/toroymoi\n'
                                     'YouTube: @Toro y Moi\n'
                                     '\n'
                                     'Lyrics:\n'
                                     'The difference in between\n'
                                     'all the faces you read\n'
                                     "When the grass ain't green\n"
                                     'When you fix everything\n'
                                     '\n'
                                     "I don't know about you but I got to get it out and I don't "
                                     'know how soon\n'
                                     'But if we die, I want to bring the whole thing\n'
                                     '\n'
                                     'Chorus oooohs\n'
                                     '\n'
                                     'Who cares about a game\n'
                                     "when it's all been replaced\n"
                                     'Each level feels the same\n'
                                     'It really goes either way\n'
                                     '\n'
                                     "I don't know about you but I got to get it out and I don't "
                                     'know how soon\n'
                                     'But if we die, I want to bring the whole thing\n'
                                     '\n'
                                     'Chorus oooohs\n'
                                     '\n'
                                     'Just another world that I gotta get a grip of and hold onto\n'
                                     'Just another world that I gotta get a grip of and hold on\n'
                                     'Just another world that I gotta get a grip of and hold onto\n'
                                     'Just another world that I gotta get a grip of and hold onto\n'
                                     '\n'
                                     '#Flume\n'
                                     '#ToroYMoi\n'
                                     '#TheDifference',
                      'dislike_count': 593,
                      'display_id': 'MCRiUi28UpA',
                      'duration': 140,
                      'end_time': None,
                      'episode_number': None,
                      'ext': 'mp4',
                      'extractor': 'youtube',
                      'extractor_key': 'Youtube',
                      'format': '137 - 1920x1080 (1080p)+251 - audio only (tiny)',
                      'format_id': '137+251',
                      'formats': [{...},
                                  {...},
                                  {...},
                                  {...},
                                  {...},
                                  {...},
                                  {...},
                                  {...},
                                  {...},
                                  {...},
                                  {...},
                                  {...},
                                  {...},
                                  {...},
                                  {...},
                                  {...},
                                  {...},
                                  {...},
                                  {...},
                                  {...},
                                  {...},
                                  {...},
                                  {...}],
                      'fps': 24,
                      'height': 1080,
                      'id': 'MCRiUi28UpA',
                      'is_live': None,
                      'license': None,
                      'like_count': 59074,
                      'playlist': None,
                      'playlist_index': None,
                      'release_date': None,
                      'release_year': None,
                      'requested_formats': ({...}, {...}),
                      'requested_subtitles': None,
                      'resolution': None,
                      'season_number': None,
                      'series': None,
                      'start_time': None,
                      'stretched_ratio': None,
                      'subtitles': {},
                      'tags': ['the difference',
                               'flume',
                               'the difference flume',
                               'flume the difference',
                               'toro y moi',
                               'toro y moi the difference',
                               'the difference toro y moi',
                               'flume toro y moi',
                               'flume & toro y moi - the difference',
                               'the difference lyrics',
                               'the difference flume lyrics',
                               'toro y moi flume',
                               'toroymoi',
                               'chaz bear',
                               'chaz bundick',
                               'the difference video',
                               'flume the distance inbetween',
                               'flume differance between',
                               'toro y moi inbetween',
                               'flume difference between',
                               'airpods pro',
                               'airpods song',
                               'apple song',
                               'apple airpod song'],
                      'thumbnail': 'https://i.ytimg.com/vi/MCRiUi28UpA/maxresdefault.jpg',
                      'thumbnails': [{...}],
                      'title': 'Flume feat. Toro y Moi - The Difference (Official Music Video)',
                      'track': 'Flume feat. Toro y Moi - The Difference [Official Lyric Video]',
                      'upload_date': '20200311',
                      'uploader': 'Flume',
                      'uploader_id': 'FlumeAUS',
                      'uploader_url': 'http://www.youtube.com/user/FlumeAUS',
                      'vbr': None,
                      'vcodec': 'avc1.640028',
                      'view_count': 1882906,
                      'webpage_url': 'https://www.youtube.com/watch?v=MCRiUi28UpA',
                      'webpage_url_basename': 'watch',
                      'width': 1920}

get_info_output = [{'id': 'Pl46Qsk-Wvs', 'uploader': 'SteveVaiHimself', 'uploader_id': 'SteveVaiHimself',
                    'uploader_url': 'http://www.youtube.com/user/SteveVaiHimself',
                    'channel_id': 'UCdkBa5GZKEAfiTjqfqotWhQ',
                    'channel_url': 'http://www.youtube.com/channel/UCdkBa5GZKEAfiTjqfqotWhQ', 'upload_date': '20200505',
                    'license': None, 'creator': 'Steve Vai', 'title': 'Steve Vai - "Bad Horsie" from the Harmony Hut',
                    'alt_title': 'Bad Horsie', 'thumbnail': 'https://i.ytimg.com/vi/Pl46Qsk-Wvs/maxresdefault.jpg',
                    'description': 'Bad Horsie" live from the Harmony Hu', 'categories': ['Music'],
                    'tags': ['Steve', 'Vai', 'Steve Vai', 'Bad Horsie', 'Harmony Hut'], 'subtitles': {},
                    'automatic_captions': {}, 'duration': 344, 'age_limit': 0, 'annotations': None, 'chapters': None,
                    'webpage_url': 'https://www.youtube.com/watch?v=Pl46Qsk-Wvs', 'view_count': 470138,
                    'like_count': 34725, 'dislike_count': 218, 'average_rating': 4.9750452, 'formats': [
        {'format_id': '249',
         'url': 'https://r3---sn-u2oxu-f5fed.googlevideo.com/videoplayback?expire=1590022021&ei=JHvFXtLAOoK7yQWNrqXYCA&ip=193.43.136.244&id=o-AJlPb7J8bfiCTZj36Aw9a4fp3ufPiN7CPd5JFVRNgDBw&itag=249&source=youtube&requiressl=yes&mh=Bp&mm=31%2C26&mn=sn-u2oxu-f5fed%2Csn-4g5e6nlk&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=517500&vprv=1&mime=audio%2Fwebm&gir=yes&clen=1956415&dur=344.221&lmt=1589018151643651&mt=1590000341&fvip=3&keepalive=yes&fexp=23882513&c=WEB&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAIBz-mGanOoGe65UED-NcmApFBVth6iaYGdk14g1G_jKAiEA6utWbcvcXJEekHm_tIxvzmqFhD19JCNG42dZj-OaPvs%3D&sig=AOq0QJ8wRQIgCcVgsqO43BPYr5h0iKojh9b0j-2bZMDN4HBj83Fz8HYCIQDcQCPD87gLfwXEU93NJP8BsZTUEmbIaJ0FqKjoImvRmg==&ratebypass=yes',
         'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'ext': 'webm', 'format_note': 'tiny',
         'acodec': 'opus', 'abr': 50, 'asr': 48000, 'filesize': 1956415, 'fps': None, 'height': None, 'tbr': 55.892,
         'width': None, 'vcodec': 'none', 'downloader_options': {'http_chunk_size': 10485760},
         'format': '249 - audio only (tiny)', 'protocol': 'https', 'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}}, {'format_id': '250',
                                                                                        'url': 'https://r3---sn-u2oxu-f5fed.googlevideo.com/videoplayback?expire=1590022021&ei=JHvFXtLAOoK7yQWNrqXYCA&ip=193.43.136.244&id=o-AJlPb7J8bfiCTZj36Aw9a4fp3ufPiN7CPd5JFVRNgDBw&itag=250&source=youtube&requiressl=yes&mh=Bp&mm=31%2C26&mn=sn-u2oxu-f5fed%2Csn-4g5e6nlk&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=517500&vprv=1&mime=audio%2Fwebm&gir=yes&clen=2594686&dur=344.221&lmt=1589018151177893&mt=1590000341&fvip=3&keepalive=yes&fexp=23882513&c=WEB&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAIBz-mGanOoGe65UED-NcmApFBVth6iaYGdk14g1G_jKAiEA6utWbcvcXJEekHm_tIxvzmqFhD19JCNG42dZj-OaPvs%3D&sig=AOq0QJ8wRQIhAKiklaFxE-urI7MdS3Vczjxz2y0MPZdljPJFlp-aOiBaAiABI-kd10ShcCPl7WiuniyDEOURoGUXqKOL4JkFWs9c3g==&ratebypass=yes',
                                                                                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js',
                                                                                        'ext': 'webm',
                                                                                        'format_note': 'tiny',
                                                                                        'acodec': 'opus', 'abr': 70,
                                                                                        'asr': 48000,
                                                                                        'filesize': 2594686,
                                                                                        'fps': None, 'height': None,
                                                                                        'tbr': 72.86, 'width': None,
                                                                                        'vcodec': 'none',
                                                                                        'downloader_options': {
                                                                                            'http_chunk_size': 10485760},
                                                                                        'format': '250 - audio only (tiny)',
                                                                                        'protocol': 'https',
                                                                                        'http_headers': {
                                                                                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                                                                                            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                                                                                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                                                                            'Accept-Encoding': 'gzip, deflate',
                                                                                            'Accept-Language': 'en-us,en;q=0.5'}},
        {'format_id': '140',
         'url': 'https://r3---sn-u2oxu-f5fed.googlevideo.com/videoplayback?expire=1590022021&ei=JHvFXtLAOoK7yQWNrqXYCA&ip=193.43.136.244&id=o-AJlPb7J8bfiCTZj36Aw9a4fp3ufPiN7CPd5JFVRNgDBw&itag=140&source=youtube&requiressl=yes&mh=Bp&mm=31%2C26&mn=sn-u2oxu-f5fed%2Csn-4g5e6nlk&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=517500&vprv=1&mime=audio%2Fmp4&gir=yes&clen=5572172&dur=344.259&lmt=1589018152781764&mt=1590000341&fvip=3&keepalive=yes&fexp=23882513&c=WEB&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAIBz-mGanOoGe65UED-NcmApFBVth6iaYGdk14g1G_jKAiEA6utWbcvcXJEekHm_tIxvzmqFhD19JCNG42dZj-OaPvs%3D&sig=AOq0QJ8wRQIgG47vsoaaTcvQ8RhYzSI3hdhZ7tS3gnS8ZISI3OjgTYwCIQDaybs6Ryr4rmQq7gZ8ua1N6lJGY-Ua40cjQ5gjeWNZsA==&ratebypass=yes',
         'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'ext': 'm4a', 'format_note': 'tiny',
         'acodec': 'mp4a.40.2', 'abr': 128, 'container': 'm4a_dash', 'asr': 44100, 'filesize': 5572172, 'fps': None,
         'height': None, 'tbr': 130.324, 'width': None, 'vcodec': 'none',
         'downloader_options': {'http_chunk_size': 10485760}, 'format': '140 - audio only (tiny)', 'protocol': 'https',
         'http_headers': {
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
             'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}}, {'format_id': '251',
                                                                                         'url': 'https://r3---sn-u2oxu-f5fed.googlevideo.com/videoplayback?expire=1590022021&ei=JHvFXtLAOoK7yQWNrqXYCA&ip=193.43.136.244&id=o-AJlPb7J8bfiCTZj36Aw9a4fp3ufPiN7CPd5JFVRNgDBw&itag=251&source=youtube&requiressl=yes&mh=Bp&mm=31%2C26&mn=sn-u2oxu-f5fed%2Csn-4g5e6nlk&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=517500&vprv=1&mime=audio%2Fwebm&gir=yes&clen=5173249&dur=344.221&lmt=1589018151995998&mt=1590000341&fvip=3&keepalive=yes&fexp=23882513&c=WEB&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAIBz-mGanOoGe65UED-NcmApFBVth6iaYGdk14g1G_jKAiEA6utWbcvcXJEekHm_tIxvzmqFhD19JCNG42dZj-OaPvs%3D&sig=AOq0QJ8wRAIgTxuchcMtw0yH1xjgzIeYgpPKGrSR8aONF5AaRJBN6GQCIBXsHuMT6f1tG6Z8tXy7dwbo_khARm0iX5zwvcR6-lEI&ratebypass=yes',
                                                                                         'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js',
                                                                                         'ext': 'webm',
                                                                                         'format_note': 'tiny',
                                                                                         'acodec': 'opus', 'abr': 160,
                                                                                         'asr': 48000,
                                                                                         'filesize': 5173249,
                                                                                         'fps': None, 'height': None,
                                                                                         'tbr': 143.624, 'width': None,
                                                                                         'vcodec': 'none',
                                                                                         'downloader_options': {
                                                                                             'http_chunk_size': 10485760},
                                                                                         'format': '251 - audio only (tiny)',
                                                                                         'protocol': 'https',
                                                                                         'http_headers': {
                                                                                             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                                                                                             'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                                                                                             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                                                                             'Accept-Encoding': 'gzip, deflate',
                                                                                             'Accept-Language': 'en-us,en;q=0.5'}},
        {'format_id': '394',
         'url': 'https://r3---sn-u2oxu-f5fed.googlevideo.com/videoplayback?expire=1590022021&ei=JHvFXtLAOoK7yQWNrqXYCA&ip=193.43.136.244&id=o-AJlPb7J8bfiCTZj36Aw9a4fp3ufPiN7CPd5JFVRNgDBw&itag=394&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C394%2C395%2C396%2C397%2C398&source=youtube&requiressl=yes&mh=Bp&mm=31%2C26&mn=sn-u2oxu-f5fed%2Csn-4g5e6nlk&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=517500&vprv=1&mime=video%2Fmp4&gir=yes&clen=3130128&dur=344.133&lmt=1589032257102354&mt=1590000341&fvip=3&keepalive=yes&fexp=23882513&c=WEB&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAIBz-mGanOoGe65UED-NcmApFBVth6iaYGdk14g1G_jKAiEA6utWbcvcXJEekHm_tIxvzmqFhD19JCNG42dZj-OaPvs%3D&sig=AOq0QJ8wRQIgC0NMsGJlcTvRWOIPtiXvA9f1RVz0k-QdVLbfF_KlAwMCIQCHeGD-TwG7bHjcTouI__9KhIhRsKcrinQNoVdZ8o9u-Q==&ratebypass=yes',
         'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'acodec': 'none',
         'vcodec': 'av01.0.00M.08', 'asr': None, 'filesize': 3130128, 'format_note': '144p', 'fps': 30, 'height': 144,
         'tbr': 79.552, 'width': 256, 'ext': 'mp4', 'downloader_options': {'http_chunk_size': 10485760},
         'format': '394 - 256x144 (144p)', 'protocol': 'https', 'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}}, {'format_id': '278',
                                                                                        'url': 'https://r3---sn-u2oxu-f5fed.googlevideo.com/videoplayback?expire=1590022021&ei=JHvFXtLAOoK7yQWNrqXYCA&ip=193.43.136.244&id=o-AJlPb7J8bfiCTZj36Aw9a4fp3ufPiN7CPd5JFVRNgDBw&itag=278&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C394%2C395%2C396%2C397%2C398&source=youtube&requiressl=yes&mh=Bp&mm=31%2C26&mn=sn-u2oxu-f5fed%2Csn-4g5e6nlk&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=517500&vprv=1&mime=video%2Fwebm&gir=yes&clen=3873943&dur=344.133&lmt=1589020805551536&mt=1590000341&fvip=3&keepalive=yes&fexp=23882513&c=WEB&txp=5535432&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAIBz-mGanOoGe65UED-NcmApFBVth6iaYGdk14g1G_jKAiEA6utWbcvcXJEekHm_tIxvzmqFhD19JCNG42dZj-OaPvs%3D&sig=AOq0QJ8wRAIgGtN5Mr0ecz7b6rIO8TJuTKjE4xlmRU-ChrQN5WBsObICIGLNg212b_dfwI_1MT1JlhCWJ0SX2UO9eCDibqWE255q&ratebypass=yes',
                                                                                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js',
                                                                                        'ext': 'webm', 'height': 144,
                                                                                        'format_note': '144p',
                                                                                        'container': 'webm',
                                                                                        'vcodec': 'vp9', 'asr': None,
                                                                                        'filesize': 3873943, 'fps': 30,
                                                                                        'tbr': 97.162, 'width': 256,
                                                                                        'acodec': 'none',
                                                                                        'downloader_options': {
                                                                                            'http_chunk_size': 10485760},
                                                                                        'format': '278 - 256x144 (144p)',
                                                                                        'protocol': 'https',
                                                                                        'http_headers': {
                                                                                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                                                                                            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                                                                                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                                                                            'Accept-Encoding': 'gzip, deflate',
                                                                                            'Accept-Language': 'en-us,en;q=0.5'}},
        {'format_id': '160',
         'url': 'https://r3---sn-u2oxu-f5fed.googlevideo.com/videoplayback?expire=1590022021&ei=JHvFXtLAOoK7yQWNrqXYCA&ip=193.43.136.244&id=o-AJlPb7J8bfiCTZj36Aw9a4fp3ufPiN7CPd5JFVRNgDBw&itag=160&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C394%2C395%2C396%2C397%2C398&source=youtube&requiressl=yes&mh=Bp&mm=31%2C26&mn=sn-u2oxu-f5fed%2Csn-4g5e6nlk&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=517500&vprv=1&mime=video%2Fmp4&gir=yes&clen=2619418&dur=344.133&lmt=1589019300324108&mt=1590000341&fvip=3&keepalive=yes&fexp=23882513&c=WEB&txp=5535432&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAIBz-mGanOoGe65UED-NcmApFBVth6iaYGdk14g1G_jKAiEA6utWbcvcXJEekHm_tIxvzmqFhD19JCNG42dZj-OaPvs%3D&sig=AOq0QJ8wRAIgVvVh_4wrAh-NCOCbO5BLV_YGbR0EPUjjZSyMRrM4F2UCIEbQ2TMq2eZ7NjwGsszii2aPfHxnJZTo3O07BPvFtSLw&ratebypass=yes',
         'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'ext': 'mp4', 'height': 144,
         'format_note': '144p', 'vcodec': 'avc1.4d400c', 'asr': None, 'filesize': 2619418, 'fps': 30, 'tbr': 103.902,
         'width': 256, 'acodec': 'none', 'downloader_options': {'http_chunk_size': 10485760},
         'format': '160 - 256x144 (144p)', 'protocol': 'https', 'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}}, {'format_id': '395',
                                                                                        'url': 'https://r3---sn-u2oxu-f5fed.googlevideo.com/videoplayback?expire=1590022021&ei=JHvFXtLAOoK7yQWNrqXYCA&ip=193.43.136.244&id=o-AJlPb7J8bfiCTZj36Aw9a4fp3ufPiN7CPd5JFVRNgDBw&itag=395&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C394%2C395%2C396%2C397%2C398&source=youtube&requiressl=yes&mh=Bp&mm=31%2C26&mn=sn-u2oxu-f5fed%2Csn-4g5e6nlk&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=517500&vprv=1&mime=video%2Fmp4&gir=yes&clen=6418257&dur=344.133&lmt=1589032189767090&mt=1590000341&fvip=3&keepalive=yes&fexp=23882513&c=WEB&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAIBz-mGanOoGe65UED-NcmApFBVth6iaYGdk14g1G_jKAiEA6utWbcvcXJEekHm_tIxvzmqFhD19JCNG42dZj-OaPvs%3D&sig=AOq0QJ8wRQIhAJHJaEe8FDqa7up2L-b-DikZiShUKn0G4iioThzbUZAVAiBBwdsbc7F6tZkGjwf8lKOaq9_vGCkdp2u9ApgLkgK1Dw==&ratebypass=yes',
                                                                                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js',
                                                                                        'acodec': 'none',
                                                                                        'vcodec': 'av01.0.00M.08',
                                                                                        'asr': None,
                                                                                        'filesize': 6418257,
                                                                                        'format_note': '240p',
                                                                                        'fps': 30, 'height': 240,
                                                                                        'tbr': 176.447, 'width': 426,
                                                                                        'ext': 'mp4',
                                                                                        'downloader_options': {
                                                                                            'http_chunk_size': 10485760},
                                                                                        'format': '395 - 426x240 (240p)',
                                                                                        'protocol': 'https',
                                                                                        'http_headers': {
                                                                                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                                                                                            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                                                                                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                                                                            'Accept-Encoding': 'gzip, deflate',
                                                                                            'Accept-Language': 'en-us,en;q=0.5'}},
        {'format_id': '242',
         'url': 'https://r3---sn-u2oxu-f5fed.googlevideo.com/videoplayback?expire=1590022021&ei=JHvFXtLAOoK7yQWNrqXYCA&ip=193.43.136.244&id=o-AJlPb7J8bfiCTZj36Aw9a4fp3ufPiN7CPd5JFVRNgDBw&itag=242&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C394%2C395%2C396%2C397%2C398&source=youtube&requiressl=yes&mh=Bp&mm=31%2C26&mn=sn-u2oxu-f5fed%2Csn-4g5e6nlk&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=517500&vprv=1&mime=video%2Fwebm&gir=yes&clen=5922333&dur=344.133&lmt=1589020805550106&mt=1590000341&fvip=3&keepalive=yes&fexp=23882513&c=WEB&txp=5535432&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAIBz-mGanOoGe65UED-NcmApFBVth6iaYGdk14g1G_jKAiEA6utWbcvcXJEekHm_tIxvzmqFhD19JCNG42dZj-OaPvs%3D&sig=AOq0QJ8wRQIhAOzi98cfZUX6Yo9xqLrWY9J3pEU51QWat5W6ojxKepvMAiAmngEJ_eDDhy3yhkK_T3QySJUI_673GCsnHsw8FN5rsw==&ratebypass=yes',
         'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'ext': 'webm', 'height': 240,
         'format_note': '240p', 'vcodec': 'vp9', 'asr': None, 'filesize': 5922333, 'fps': 30, 'tbr': 190.789,
         'width': 426, 'acodec': 'none', 'downloader_options': {'http_chunk_size': 10485760},
         'format': '242 - 426x240 (240p)', 'protocol': 'https', 'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}}, {'format_id': '133',
                                                                                        'url': 'https://r3---sn-u2oxu-f5fed.googlevideo.com/videoplayback?expire=1590022021&ei=JHvFXtLAOoK7yQWNrqXYCA&ip=193.43.136.244&id=o-AJlPb7J8bfiCTZj36Aw9a4fp3ufPiN7CPd5JFVRNgDBw&itag=133&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C394%2C395%2C396%2C397%2C398&source=youtube&requiressl=yes&mh=Bp&mm=31%2C26&mn=sn-u2oxu-f5fed%2Csn-4g5e6nlk&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=517500&vprv=1&mime=video%2Fmp4&gir=yes&clen=5175125&dur=344.133&lmt=1589019300323772&mt=1590000341&fvip=3&keepalive=yes&fexp=23882513&c=WEB&txp=5535432&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAIBz-mGanOoGe65UED-NcmApFBVth6iaYGdk14g1G_jKAiEA6utWbcvcXJEekHm_tIxvzmqFhD19JCNG42dZj-OaPvs%3D&sig=AOq0QJ8wRQIhAL56odaAqqfkMY11S5liuiTGj6j9fr9R_SXXcTPYIwG5AiAB_2cHx4n3aNmY8erznewS5_IPHYr0UpybHMqzovlMSg==&ratebypass=yes',
                                                                                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js',
                                                                                        'ext': 'mp4', 'height': 240,
                                                                                        'format_note': '240p',
                                                                                        'vcodec': 'avc1.4d4015',
                                                                                        'asr': None,
                                                                                        'filesize': 5175125, 'fps': 30,
                                                                                        'tbr': 220.62, 'width': 426,
                                                                                        'acodec': 'none',
                                                                                        'downloader_options': {
                                                                                            'http_chunk_size': 10485760},
                                                                                        'format': '133 - 426x240 (240p)',
                                                                                        'protocol': 'https',
                                                                                        'http_headers': {
                                                                                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                                                                                            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                                                                                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                                                                            'Accept-Encoding': 'gzip, deflate',
                                                                                            'Accept-Language': 'en-us,en;q=0.5'}},
        {'format_id': '396',
         'url': 'https://r3---sn-u2oxu-f5fed.googlevideo.com/videoplayback?expire=1590022021&ei=JHvFXtLAOoK7yQWNrqXYCA&ip=193.43.136.244&id=o-AJlPb7J8bfiCTZj36Aw9a4fp3ufPiN7CPd5JFVRNgDBw&itag=396&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C394%2C395%2C396%2C397%2C398&source=youtube&requiressl=yes&mh=Bp&mm=31%2C26&mn=sn-u2oxu-f5fed%2Csn-4g5e6nlk&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=517500&vprv=1&mime=video%2Fmp4&gir=yes&clen=11498552&dur=344.133&lmt=1589032588853240&mt=1590000341&fvip=3&keepalive=yes&fexp=23882513&c=WEB&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAIBz-mGanOoGe65UED-NcmApFBVth6iaYGdk14g1G_jKAiEA6utWbcvcXJEekHm_tIxvzmqFhD19JCNG42dZj-OaPvs%3D&sig=AOq0QJ8wRQIgMylAUjIg8MZlznaNGVc72XVc8RvLue9Y28Sua_LK_r0CIQCvujZCWRWUVV11cPjCKsgewf4gnm-X-xebzq5hdUMITw==&ratebypass=yes',
         'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'acodec': 'none',
         'vcodec': 'av01.0.01M.08', 'asr': None, 'filesize': 11498552, 'format_note': '360p', 'fps': 30, 'height': 360,
         'tbr': 324.801, 'width': 640, 'ext': 'mp4', 'downloader_options': {'http_chunk_size': 10485760},
         'format': '396 - 640x360 (360p)', 'protocol': 'https', 'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}}, {'format_id': '243',
                                                                                        'url': 'https://r3---sn-u2oxu-f5fed.googlevideo.com/videoplayback?expire=1590022021&ei=JHvFXtLAOoK7yQWNrqXYCA&ip=193.43.136.244&id=o-AJlPb7J8bfiCTZj36Aw9a4fp3ufPiN7CPd5JFVRNgDBw&itag=243&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C394%2C395%2C396%2C397%2C398&source=youtube&requiressl=yes&mh=Bp&mm=31%2C26&mn=sn-u2oxu-f5fed%2Csn-4g5e6nlk&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=517500&vprv=1&mime=video%2Fwebm&gir=yes&clen=10158036&dur=344.133&lmt=1589020805554541&mt=1590000341&fvip=3&keepalive=yes&fexp=23882513&c=WEB&txp=5535432&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAIBz-mGanOoGe65UED-NcmApFBVth6iaYGdk14g1G_jKAiEA6utWbcvcXJEekHm_tIxvzmqFhD19JCNG42dZj-OaPvs%3D&sig=AOq0QJ8wRgIhANj3Rn2dHVcqFMGh78XWttnU3r0_HMzg_4GIl-RRyMTqAiEAuHVOApX1daXki8BHCmzyppH_l4bKuzuj7c1bKl_-Rh4=&ratebypass=yes',
                                                                                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js',
                                                                                        'ext': 'webm', 'height': 360,
                                                                                        'format_note': '360p',
                                                                                        'vcodec': 'vp9', 'asr': None,
                                                                                        'filesize': 10158036, 'fps': 30,
                                                                                        'tbr': 325.962, 'width': 640,
                                                                                        'acodec': 'none',
                                                                                        'downloader_options': {
                                                                                            'http_chunk_size': 10485760},
                                                                                        'format': '243 - 640x360 (360p)',
                                                                                        'protocol': 'https',
                                                                                        'http_headers': {
                                                                                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                                                                                            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                                                                                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                                                                            'Accept-Encoding': 'gzip, deflate',
                                                                                            'Accept-Language': 'en-us,en;q=0.5'}},
        {'format_id': '134',
         'url': 'https://r3---sn-u2oxu-f5fed.googlevideo.com/videoplayback?expire=1590022021&ei=JHvFXtLAOoK7yQWNrqXYCA&ip=193.43.136.244&id=o-AJlPb7J8bfiCTZj36Aw9a4fp3ufPiN7CPd5JFVRNgDBw&itag=134&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C394%2C395%2C396%2C397%2C398&source=youtube&requiressl=yes&mh=Bp&mm=31%2C26&mn=sn-u2oxu-f5fed%2Csn-4g5e6nlk&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=517500&vprv=1&mime=video%2Fmp4&gir=yes&clen=9373358&dur=344.133&lmt=1589019300361938&mt=1590000341&fvip=3&keepalive=yes&fexp=23882513&c=WEB&txp=5535432&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAIBz-mGanOoGe65UED-NcmApFBVth6iaYGdk14g1G_jKAiEA6utWbcvcXJEekHm_tIxvzmqFhD19JCNG42dZj-OaPvs%3D&sig=AOq0QJ8wRQIgCiw7Asmy_K53g9uzCUsv6UvibP1NsVVZQ9IkumXitRECIQCAY_JJFAueR2k1aVlmVXmThegW4KNKHBPWwEag4eDB2Q==&ratebypass=yes',
         'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'ext': 'mp4', 'height': 360,
         'format_note': '360p', 'vcodec': 'avc1.4d401e', 'asr': None, 'filesize': 9373358, 'fps': 30, 'tbr': 418.04,
         'width': 640, 'acodec': 'none', 'downloader_options': {'http_chunk_size': 10485760},
         'format': '134 - 640x360 (360p)', 'protocol': 'https', 'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}}, {'format_id': '244',
                                                                                        'url': 'https://r3---sn-u2oxu-f5fed.googlevideo.com/videoplayback?expire=1590022021&ei=JHvFXtLAOoK7yQWNrqXYCA&ip=193.43.136.244&id=o-AJlPb7J8bfiCTZj36Aw9a4fp3ufPiN7CPd5JFVRNgDBw&itag=244&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C394%2C395%2C396%2C397%2C398&source=youtube&requiressl=yes&mh=Bp&mm=31%2C26&mn=sn-u2oxu-f5fed%2Csn-4g5e6nlk&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=517500&vprv=1&mime=video%2Fwebm&gir=yes&clen=14343367&dur=344.133&lmt=1589020805600348&mt=1590000341&fvip=3&keepalive=yes&fexp=23882513&c=WEB&txp=5535432&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAIBz-mGanOoGe65UED-NcmApFBVth6iaYGdk14g1G_jKAiEA6utWbcvcXJEekHm_tIxvzmqFhD19JCNG42dZj-OaPvs%3D&sig=AOq0QJ8wRgIhAOeDiO7LZqCOJkvZ9fzDgmYA3oZLSY24JPRPWjyuq3dCAiEAyf5ZLxO8J0bbPkW2w5XZ36KTPQiwFoksievJX7VfEbw=&ratebypass=yes',
                                                                                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js',
                                                                                        'ext': 'webm', 'height': 480,
                                                                                        'format_note': '480p',
                                                                                        'vcodec': 'vp9', 'asr': None,
                                                                                        'filesize': 14343367, 'fps': 30,
                                                                                        'tbr': 488.154, 'width': 854,
                                                                                        'acodec': 'none',
                                                                                        'downloader_options': {
                                                                                            'http_chunk_size': 10485760},
                                                                                        'format': '244 - 854x480 (480p)',
                                                                                        'protocol': 'https',
                                                                                        'http_headers': {
                                                                                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                                                                                            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                                                                                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                                                                            'Accept-Encoding': 'gzip, deflate',
                                                                                            'Accept-Language': 'en-us,en;q=0.5'}},
        {'format_id': '397',
         'url': 'https://r3---sn-u2oxu-f5fed.googlevideo.com/videoplayback?expire=1590022021&ei=JHvFXtLAOoK7yQWNrqXYCA&ip=193.43.136.244&id=o-AJlPb7J8bfiCTZj36Aw9a4fp3ufPiN7CPd5JFVRNgDBw&itag=397&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C394%2C395%2C396%2C397%2C398&source=youtube&requiressl=yes&mh=Bp&mm=31%2C26&mn=sn-u2oxu-f5fed%2Csn-4g5e6nlk&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=517500&vprv=1&mime=video%2Fmp4&gir=yes&clen=19599104&dur=344.133&lmt=1589032690091396&mt=1590000341&fvip=3&keepalive=yes&fexp=23882513&c=WEB&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAIBz-mGanOoGe65UED-NcmApFBVth6iaYGdk14g1G_jKAiEA6utWbcvcXJEekHm_tIxvzmqFhD19JCNG42dZj-OaPvs%3D&sig=AOq0QJ8wRQIhAO3JL_QAmI-EiR2TVPhlL2OCnr5AtwWp-jrVu82JA7VZAiAuF5u94cYF9axFMFaquNg5_D9-HsDTASGAgQnxS7Azqw==&ratebypass=yes',
         'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'acodec': 'none',
         'vcodec': 'av01.0.04M.08', 'asr': None, 'filesize': 19599104, 'format_note': '480p', 'fps': 30, 'height': 480,
         'tbr': 564.276, 'width': 854, 'ext': 'mp4', 'downloader_options': {'http_chunk_size': 10485760},
         'format': '397 - 854x480 (480p)', 'protocol': 'https', 'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}}, {'format_id': '135',
                                                                                        'url': 'https://r3---sn-u2oxu-f5fed.googlevideo.com/videoplayback?expire=1590022021&ei=JHvFXtLAOoK7yQWNrqXYCA&ip=193.43.136.244&id=o-AJlPb7J8bfiCTZj36Aw9a4fp3ufPiN7CPd5JFVRNgDBw&itag=135&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C394%2C395%2C396%2C397%2C398&source=youtube&requiressl=yes&mh=Bp&mm=31%2C26&mn=sn-u2oxu-f5fed%2Csn-4g5e6nlk&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=517500&vprv=1&mime=video%2Fmp4&gir=yes&clen=15850495&dur=344.133&lmt=1589019300337536&mt=1590000341&fvip=3&keepalive=yes&fexp=23882513&c=WEB&txp=5535432&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAIBz-mGanOoGe65UED-NcmApFBVth6iaYGdk14g1G_jKAiEA6utWbcvcXJEekHm_tIxvzmqFhD19JCNG42dZj-OaPvs%3D&sig=AOq0QJ8wRgIhAJUcKJwgunJd3d0mrgJp40z76rujgZahcvehXQCi8PIpAiEA_vJqJyAVsOYbnU-fW04WkobiXv3dqv7uO6HcFMajLuc=&ratebypass=yes',
                                                                                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js',
                                                                                        'ext': 'mp4', 'height': 480,
                                                                                        'format_note': '480p',
                                                                                        'vcodec': 'avc1.4d401f',
                                                                                        'asr': None,
                                                                                        'filesize': 15850495, 'fps': 30,
                                                                                        'tbr': 644.333, 'width': 854,
                                                                                        'acodec': 'none',
                                                                                        'downloader_options': {
                                                                                            'http_chunk_size': 10485760},
                                                                                        'format': '135 - 854x480 (480p)',
                                                                                        'protocol': 'https',
                                                                                        'http_headers': {
                                                                                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                                                                                            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                                                                                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                                                                            'Accept-Encoding': 'gzip, deflate',
                                                                                            'Accept-Language': 'en-us,en;q=0.5'}},
        {'format_id': '247',
         'url': 'https://r3---sn-u2oxu-f5fed.googlevideo.com/videoplayback?expire=1590022021&ei=JHvFXtLAOoK7yQWNrqXYCA&ip=193.43.136.244&id=o-AJlPb7J8bfiCTZj36Aw9a4fp3ufPiN7CPd5JFVRNgDBw&itag=247&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C394%2C395%2C396%2C397%2C398&source=youtube&requiressl=yes&mh=Bp&mm=31%2C26&mn=sn-u2oxu-f5fed%2Csn-4g5e6nlk&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=517500&vprv=1&mime=video%2Fwebm&gir=yes&clen=23449469&dur=344.133&lmt=1589020805552319&mt=1590000341&fvip=3&keepalive=yes&fexp=23882513&c=WEB&txp=5535432&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAIBz-mGanOoGe65UED-NcmApFBVth6iaYGdk14g1G_jKAiEA6utWbcvcXJEekHm_tIxvzmqFhD19JCNG42dZj-OaPvs%3D&sig=AOq0QJ8wRAIgS_TnlFmyvks76nyJGjShMXGjAibtqwG3n69441qP4l0CICJ4zTZT5usdAmgaznOl2_wD2fkKSwL2CeEVhusW1hUg&ratebypass=yes',
         'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'ext': 'webm', 'height': 720,
         'format_note': '720p', 'vcodec': 'vp9', 'asr': None, 'filesize': 23449469, 'fps': 30, 'tbr': 784.642,
         'width': 1280, 'acodec': 'none', 'downloader_options': {'http_chunk_size': 10485760},
         'format': '247 - 1280x720 (720p)', 'protocol': 'https', 'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}}, {'format_id': '136',
                                                                                        'url': 'https://r3---sn-u2oxu-f5fed.googlevideo.com/videoplayback?expire=1590022021&ei=JHvFXtLAOoK7yQWNrqXYCA&ip=193.43.136.244&id=o-AJlPb7J8bfiCTZj36Aw9a4fp3ufPiN7CPd5JFVRNgDBw&itag=136&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C394%2C395%2C396%2C397%2C398&source=youtube&requiressl=yes&mh=Bp&mm=31%2C26&mn=sn-u2oxu-f5fed%2Csn-4g5e6nlk&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=517500&vprv=1&mime=video%2Fmp4&gir=yes&clen=23623345&dur=344.133&lmt=1589019300322450&mt=1590000341&fvip=3&keepalive=yes&fexp=23882513&c=WEB&txp=5535432&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAIBz-mGanOoGe65UED-NcmApFBVth6iaYGdk14g1G_jKAiEA6utWbcvcXJEekHm_tIxvzmqFhD19JCNG42dZj-OaPvs%3D&sig=AOq0QJ8wRAIgBYiBsSBtu560LOZw8d5mhHP4DMRplUCvJB2Ys2Rz0VECIEbnMcZGuVAWEAvqVcoXVYlzRxxfwaL--6qx_s1xKc7k&ratebypass=yes',
                                                                                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js',
                                                                                        'ext': 'mp4', 'height': 720,
                                                                                        'format_note': '720p',
                                                                                        'vcodec': 'avc1.4d401f',
                                                                                        'asr': None,
                                                                                        'filesize': 23623345, 'fps': 30,
                                                                                        'tbr': 974.082, 'width': 1280,
                                                                                        'acodec': 'none',
                                                                                        'downloader_options': {
                                                                                            'http_chunk_size': 10485760},
                                                                                        'format': '136 - 1280x720 (720p)',
                                                                                        'protocol': 'https',
                                                                                        'http_headers': {
                                                                                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                                                                                            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                                                                                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                                                                            'Accept-Encoding': 'gzip, deflate',
                                                                                            'Accept-Language': 'en-us,en;q=0.5'}},
        {'format_id': '398',
         'url': 'https://r3---sn-u2oxu-f5fed.googlevideo.com/videoplayback?expire=1590022021&ei=JHvFXtLAOoK7yQWNrqXYCA&ip=193.43.136.244&id=o-AJlPb7J8bfiCTZj36Aw9a4fp3ufPiN7CPd5JFVRNgDBw&itag=398&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C394%2C395%2C396%2C397%2C398&source=youtube&requiressl=yes&mh=Bp&mm=31%2C26&mn=sn-u2oxu-f5fed%2Csn-4g5e6nlk&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=517500&vprv=1&mime=video%2Fmp4&gir=yes&clen=40168117&dur=344.133&lmt=1589033786341567&mt=1590000341&fvip=3&keepalive=yes&fexp=23882513&c=WEB&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAIBz-mGanOoGe65UED-NcmApFBVth6iaYGdk14g1G_jKAiEA6utWbcvcXJEekHm_tIxvzmqFhD19JCNG42dZj-OaPvs%3D&sig=AOq0QJ8wRQIgGwKYpIymwgnvZWqZyYxK5D_yg1-gA1j_qr--1FlmBJkCIQDNRLGo-5z1TXa90bsecS4qkFt3hzAEXW2Nga3-LvCTOg==&ratebypass=yes',
         'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'asr': None, 'filesize': 40168117,
         'format_note': '720p', 'fps': 30, 'height': 720, 'tbr': 1106.917, 'width': 1280, 'ext': 'mp4',
         'vcodec': 'av01.0.05M.08', 'acodec': 'none', 'downloader_options': {'http_chunk_size': 10485760},
         'format': '398 - 1280x720 (720p)', 'protocol': 'https', 'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}}, {'format_id': '18',
                                                                                        'url': 'https://r3---sn-u2oxu-f5fed.googlevideo.com/videoplayback?expire=1590022021&ei=JHvFXtLAOoK7yQWNrqXYCA&ip=193.43.136.244&id=o-AJlPb7J8bfiCTZj36Aw9a4fp3ufPiN7CPd5JFVRNgDBw&itag=18&source=youtube&requiressl=yes&mh=Bp&mm=31%2C26&mn=sn-u2oxu-f5fed%2Csn-4g5e6nlk&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=517500&vprv=1&mime=video%2Fmp4&gir=yes&clen=22182917&ratebypass=yes&dur=344.259&lmt=1589017781605798&mt=1590000341&fvip=3&fexp=23882513&c=WEB&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAIBz-mGanOoGe65UED-NcmApFBVth6iaYGdk14g1G_jKAiEA6utWbcvcXJEekHm_tIxvzmqFhD19JCNG42dZj-OaPvs%3D&sig=AOq0QJ8wRAIgHj0WTaspsS4fFAeOrc2EUd1YgP1BkB63K-TCQDkykDQCIFN8GjJpDUtS5mVaUNUHdnVwN_0d4YMvsCEKRCcrauTQ',
                                                                                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js',
                                                                                        'ext': 'mp4', 'width': 640,
                                                                                        'height': 360,
                                                                                        'acodec': 'mp4a.40.2',
                                                                                        'abr': 96,
                                                                                        'vcodec': 'avc1.42001E',
                                                                                        'asr': 44100,
                                                                                        'filesize': 22182917,
                                                                                        'format_note': '360p',
                                                                                        'fps': 30, 'tbr': 515.682,
                                                                                        'format': '18 - 640x360 (360p)',
                                                                                        'protocol': 'https',
                                                                                        'http_headers': {
                                                                                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                                                                                            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                                                                                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                                                                            'Accept-Encoding': 'gzip, deflate',
                                                                                            'Accept-Language': 'en-us,en;q=0.5'}}],
                    'is_live': None, 'start_time': None, 'end_time': None, 'series': None, 'season_number': None,
                    'episode_number': None, 'track': 'Bad Horsie', 'artist': 'Steve Vai',
                    'album': 'The Guitars that Destroyed the World (Live in China)', 'release_date': None,
                    'release_year': None, 'extractor': 'youtube', 'webpage_url_basename': 'watch',
                    'extractor_key': 'Youtube', 'playlist': None, 'playlist_index': None,
                    'thumbnails': [{'url': 'https://i.ytimg.com/vi/Pl46Qsk-Wvs/maxresdefault.jpg', 'id': '0'}],
                    'display_id': 'Pl46Qsk-Wvs', 'requested_subtitles': None, 'requested_formats': ({'format_id': '398',
                                                                                                     'url': 'https://r3---sn-u2oxu-f5fed.googlevideo.com/videoplayback?expire=1590022021&ei=JHvFXtLAOoK7yQWNrqXYCA&ip=193.43.136.244&id=o-AJlPb7J8bfiCTZj36Aw9a4fp3ufPiN7CPd5JFVRNgDBw&itag=398&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C394%2C395%2C396%2C397%2C398&source=youtube&requiressl=yes&mh=Bp&mm=31%2C26&mn=sn-u2oxu-f5fed%2Csn-4g5e6nlk&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=517500&vprv=1&mime=video%2Fmp4&gir=yes&clen=40168117&dur=344.133&lmt=1589033786341567&mt=1590000341&fvip=3&keepalive=yes&fexp=23882513&c=WEB&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAIBz-mGanOoGe65UED-NcmApFBVth6iaYGdk14g1G_jKAiEA6utWbcvcXJEekHm_tIxvzmqFhD19JCNG42dZj-OaPvs%3D&sig=AOq0QJ8wRQIgGwKYpIymwgnvZWqZyYxK5D_yg1-gA1j_qr--1FlmBJkCIQDNRLGo-5z1TXa90bsecS4qkFt3hzAEXW2Nga3-LvCTOg==&ratebypass=yes',
                                                                                                     'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js',
                                                                                                     'asr': None,
                                                                                                     'filesize': 40168117,
                                                                                                     'format_note': '720p',
                                                                                                     'fps': 30,
                                                                                                     'height': 720,
                                                                                                     'tbr': 1106.917,
                                                                                                     'width': 1280,
                                                                                                     'ext': 'mp4',
                                                                                                     'vcodec': 'av01.0.05M.08',
                                                                                                     'acodec': 'none',
                                                                                                     'downloader_options': {
                                                                                                         'http_chunk_size': 10485760},
                                                                                                     'format': '398 - 1280x720 (720p)',
                                                                                                     'protocol': 'https',
                                                                                                     'http_headers': {
                                                                                                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                                                                                                         'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                                                                                                         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                                                                                         'Accept-Encoding': 'gzip, deflate',
                                                                                                         'Accept-Language': 'en-us,en;q=0.5'}},
                                                                                                    {'format_id': '251',
                                                                                                     'url': 'https://r3---sn-u2oxu-f5fed.googlevideo.com/videoplayback?expire=1590022021&ei=JHvFXtLAOoK7yQWNrqXYCA&ip=193.43.136.244&id=o-AJlPb7J8bfiCTZj36Aw9a4fp3ufPiN7CPd5JFVRNgDBw&itag=251&source=youtube&requiressl=yes&mh=Bp&mm=31%2C26&mn=sn-u2oxu-f5fed%2Csn-4g5e6nlk&ms=au%2Conr&mv=m&mvi=2&pl=24&initcwndbps=517500&vprv=1&mime=audio%2Fwebm&gir=yes&clen=5173249&dur=344.221&lmt=1589018151995998&mt=1590000341&fvip=3&keepalive=yes&fexp=23882513&c=WEB&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAIBz-mGanOoGe65UED-NcmApFBVth6iaYGdk14g1G_jKAiEA6utWbcvcXJEekHm_tIxvzmqFhD19JCNG42dZj-OaPvs%3D&sig=AOq0QJ8wRAIgTxuchcMtw0yH1xjgzIeYgpPKGrSR8aONF5AaRJBN6GQCIBXsHuMT6f1tG6Z8tXy7dwbo_khARm0iX5zwvcR6-lEI&ratebypass=yes',
                                                                                                     'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js',
                                                                                                     'ext': 'webm',
                                                                                                     'format_note': 'tiny',
                                                                                                     'acodec': 'opus',
                                                                                                     'abr': 160,
                                                                                                     'asr': 48000,
                                                                                                     'filesize': 5173249,
                                                                                                     'fps': None,
                                                                                                     'height': None,
                                                                                                     'tbr': 143.624,
                                                                                                     'width': None,
                                                                                                     'vcodec': 'none',
                                                                                                     'downloader_options': {
                                                                                                         'http_chunk_size': 10485760},
                                                                                                     'format': '251 - audio only (tiny)',
                                                                                                     'protocol': 'https',
                                                                                                     'http_headers': {
                                                                                                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                                                                                                         'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                                                                                                         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                                                                                         'Accept-Encoding': 'gzip, deflate',
                                                                                                         'Accept-Language': 'en-us,en;q=0.5'}}),
                    'format': '398 - 1280x720 (720p)+251 - audio only (tiny)', 'format_id': '398+251', 'width': 1280,
                    'height': 720, 'resolution': None, 'fps': 30, 'vcodec': 'av01.0.05M.08', 'vbr': None,
                    'stretched_ratio': None, 'acodec': 'opus', 'abr': 160, 'ext': 'mp4'},
                   {'id': '-s58ryovTDc', 'uploader': 'SteveVaiHimself', 'uploader_id': 'SteveVaiHimself',
                    'uploader_url': 'http://www.youtube.com/user/SteveVaiHimself',
                    'channel_id': 'UCdkBa5GZKEAfiTjqfqotWhQ',
                    'channel_url': 'http://www.youtube.com/channel/UCdkBa5GZKEAfiTjqfqotWhQ', 'upload_date': '20190821',
                    'license': None, 'creator': 'Steve Vai', 'title': '"Stillness In Motion" Blu-Ray Release',
                    'alt_title': 'The Story of Light',
                    'thumbnail': 'https://i.ytimg.com/vi/-s58ryovTDc/maxresdefault.jpg',
                    'description': 'On September 13th, I\'m proud to be releasing "Stillness In Motion" on Blu-Ray for the first time! It originally came out on DVD because Sony decided not to release a Blu-Ray, but I always felt it should be released on Blu-Ray so I got the rights back and am now releasing this concert and amazing bonus footage on Blu-Ray. The package consists of 2 Blu-Ray discs, one is the full concert performance from Club Nokia and the other is “The Space Between The Notes” which is one my favorite projects that I\'ve ever completed. “The Space Between the Notes” has over 3.5 hours of off-stage video footage and photo montages. If you are interested in behind-the-scenes type footage, this is the mother load!\n\nThis package will also include 2 audio CDs with all of the audio from the Club Nokia show.\n\nAt this time, I’m working on composing new and tweaking existing symphony scores that will all be recorded in the studio in June 2020 with various orchestras in Europe. I’m enjoying doing this a lot… like a lot a lot. And I’m happy to announce that the entire concept for my next studio record was downloaded to me from the abyss as a mental image about 2 weeks ago, so after I finish the orchestra music, I will be starting on that. Thanks so much for following all this.',
                    'categories': ['Music'], 'tags': ['Steve', 'Vai'], 'subtitles': {}, 'automatic_captions': {},
                    'duration': 160, 'age_limit': 0, 'annotations': None, 'chapters': None,
                    'webpage_url': 'https://www.youtube.com/watch?v=-s58ryovTDc', 'view_count': 51844,
                    'like_count': 742, 'dislike_count': 28, 'average_rating': 4.8545456, 'formats': [
                       {'format_id': '249',
                        'url': 'https://r7---sn-u2oxu-f5fr.googlevideo.com/videoplayback?expire=1590022021&ei=JXvFXoeLMMP17QThhJqoCw&ip=193.43.136.244&id=o-AFwqoKNBYJ7NS_gkkc6b2P1Pg8JYKSiut529sf8D2_dM&itag=249&source=youtube&requiressl=yes&mh=AI&mm=31%2C26&mn=sn-u2oxu-f5fr%2Csn-4g5e6nsy&ms=au%2Conr&mv=m&mvi=6&pl=24&initcwndbps=592500&vprv=1&mime=audio%2Fwebm&gir=yes&clen=968655&dur=159.621&lmt=1566415044845194&mt=1590000341&fvip=2&keepalive=yes&beids=9466586&c=WEB&txp=2301222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgZp4d2EVBEajfObyIiOm9g_a9tM7f5UOaOP_qJ1Xq7xoCIQDxMuM6xZicpHf_Au8m4r1UfXowHrk9cFn5-Xl8uuFEoQ%3D%3D&sig=AOq0QJ8wRQIhAINqWcn940roYkRuCN1ceRyJHP3eQiQsOEImoS6-N77VAiAhFvf0z2-M_0NhA9kU0llsk-BXtBY54DHVeIHGGq__Bg==&ratebypass=yes',
                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'ext': 'webm',
                        'format_note': 'tiny', 'acodec': 'opus', 'abr': 50, 'asr': 48000, 'filesize': 968655,
                        'fps': None, 'height': None, 'tbr': 52.8, 'width': None, 'vcodec': 'none',
                        'downloader_options': {'http_chunk_size': 10485760}, 'format': '249 - audio only (tiny)',
                        'protocol': 'https', 'http_headers': {
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}},
                       {'format_id': '250',
                        'url': 'https://r7---sn-u2oxu-f5fr.googlevideo.com/videoplayback?expire=1590022021&ei=JXvFXoeLMMP17QThhJqoCw&ip=193.43.136.244&id=o-AFwqoKNBYJ7NS_gkkc6b2P1Pg8JYKSiut529sf8D2_dM&itag=250&source=youtube&requiressl=yes&mh=AI&mm=31%2C26&mn=sn-u2oxu-f5fr%2Csn-4g5e6nsy&ms=au%2Conr&mv=m&mvi=6&pl=24&initcwndbps=592500&vprv=1&mime=audio%2Fwebm&gir=yes&clen=1289569&dur=159.621&lmt=1566415045635063&mt=1590000341&fvip=2&keepalive=yes&beids=9466586&c=WEB&txp=2301222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgZp4d2EVBEajfObyIiOm9g_a9tM7f5UOaOP_qJ1Xq7xoCIQDxMuM6xZicpHf_Au8m4r1UfXowHrk9cFn5-Xl8uuFEoQ%3D%3D&sig=AOq0QJ8wRgIhAK-78YrW29MTsPV2zaTRrXuknnAjY09MxXvxU9j7mcCfAiEAk_oJwTtKXk9U0ts44q5K7pZMOBZFNXLnEGO20zUMwfg=&ratebypass=yes',
                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'ext': 'webm',
                        'format_note': 'tiny', 'acodec': 'opus', 'abr': 70, 'asr': 48000, 'filesize': 1289569,
                        'fps': None, 'height': None, 'tbr': 70.194, 'width': None, 'vcodec': 'none',
                        'downloader_options': {'http_chunk_size': 10485760}, 'format': '250 - audio only (tiny)',
                        'protocol': 'https', 'http_headers': {
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}},
                       {'format_id': '140',
                        'url': 'https://r7---sn-u2oxu-f5fr.googlevideo.com/videoplayback?expire=1590022021&ei=JXvFXoeLMMP17QThhJqoCw&ip=193.43.136.244&id=o-AFwqoKNBYJ7NS_gkkc6b2P1Pg8JYKSiut529sf8D2_dM&itag=140&source=youtube&requiressl=yes&mh=AI&mm=31%2C26&mn=sn-u2oxu-f5fr%2Csn-4g5e6nsy&ms=au%2Conr&mv=m&mvi=6&pl=24&initcwndbps=592500&vprv=1&mime=audio%2Fmp4&gir=yes&clen=2584590&dur=159.660&lmt=1566414589972413&mt=1590000341&fvip=2&keepalive=yes&beids=9466586&c=WEB&txp=2311222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgZp4d2EVBEajfObyIiOm9g_a9tM7f5UOaOP_qJ1Xq7xoCIQDxMuM6xZicpHf_Au8m4r1UfXowHrk9cFn5-Xl8uuFEoQ%3D%3D&sig=AOq0QJ8wRQIgY381YZlQwzUHJ0J9WyBwCrY7wJLsmsmqPCv4RsskewoCIQDAHSoPffsvz7pMzyQ-Q7HfOUky4c02VE6g8ngKI9Corw==&ratebypass=yes',
                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'ext': 'm4a',
                        'format_note': 'tiny', 'acodec': 'mp4a.40.2', 'abr': 128, 'container': 'm4a_dash', 'asr': 44100,
                        'filesize': 2584590, 'fps': None, 'height': None, 'tbr': 130.426, 'width': None,
                        'vcodec': 'none', 'downloader_options': {'http_chunk_size': 10485760},
                        'format': '140 - audio only (tiny)', 'protocol': 'https', 'http_headers': {
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}},
                       {'format_id': '251',
                        'url': 'https://r7---sn-u2oxu-f5fr.googlevideo.com/videoplayback?expire=1590022021&ei=JXvFXoeLMMP17QThhJqoCw&ip=193.43.136.244&id=o-AFwqoKNBYJ7NS_gkkc6b2P1Pg8JYKSiut529sf8D2_dM&itag=251&source=youtube&requiressl=yes&mh=AI&mm=31%2C26&mn=sn-u2oxu-f5fr%2Csn-4g5e6nsy&ms=au%2Conr&mv=m&mvi=6&pl=24&initcwndbps=592500&vprv=1&mime=audio%2Fwebm&gir=yes&clen=2576924&dur=159.621&lmt=1566415046443545&mt=1590000341&fvip=2&keepalive=yes&beids=9466586&c=WEB&txp=2301222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgZp4d2EVBEajfObyIiOm9g_a9tM7f5UOaOP_qJ1Xq7xoCIQDxMuM6xZicpHf_Au8m4r1UfXowHrk9cFn5-Xl8uuFEoQ%3D%3D&sig=AOq0QJ8wRQIgCFWV3zlMWilqFCe_8-e63FiC8nkq4_ap31xH9VoEEcMCIQCJo0TaDYBXn0b-GCPHJE-K8AKA34An3P_pP_Qm4EkkAw==&ratebypass=yes',
                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'ext': 'webm',
                        'format_note': 'tiny', 'acodec': 'opus', 'abr': 160, 'asr': 48000, 'filesize': 2576924,
                        'fps': None, 'height': None, 'tbr': 139.201, 'width': None, 'vcodec': 'none',
                        'downloader_options': {'http_chunk_size': 10485760}, 'format': '251 - audio only (tiny)',
                        'protocol': 'https', 'http_headers': {
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}},
                       {'format_id': '278',
                        'url': 'https://r7---sn-u2oxu-f5fr.googlevideo.com/videoplayback?expire=1590022021&ei=JXvFXoeLMMP17QThhJqoCw&ip=193.43.136.244&id=o-AFwqoKNBYJ7NS_gkkc6b2P1Pg8JYKSiut529sf8D2_dM&itag=278&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278&source=youtube&requiressl=yes&mh=AI&mm=31%2C26&mn=sn-u2oxu-f5fr%2Csn-4g5e6nsy&ms=au%2Conr&mv=m&mvi=6&pl=24&initcwndbps=592500&vprv=1&mime=video%2Fwebm&gir=yes&clen=1956034&dur=159.592&lmt=1566414603609349&mt=1590000341&fvip=2&keepalive=yes&beids=9466586&c=WEB&txp=2316222&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgZp4d2EVBEajfObyIiOm9g_a9tM7f5UOaOP_qJ1Xq7xoCIQDxMuM6xZicpHf_Au8m4r1UfXowHrk9cFn5-Xl8uuFEoQ%3D%3D&sig=AOq0QJ8wRgIhAI6M3y1ZevZ3y6Vb9i3BG2mzEn7ywScwu7SyQGsURYzpAiEAh_lEFnyVJjWbROXZvXFFHPTdy18_UN3tcdE_etWeg80=&ratebypass=yes',
                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'ext': 'webm',
                        'height': 144, 'format_note': '144p', 'container': 'webm', 'vcodec': 'vp9', 'asr': None,
                        'filesize': 1956034, 'fps': 30, 'tbr': 129.489, 'width': 256, 'acodec': 'none',
                        'downloader_options': {'http_chunk_size': 10485760}, 'format': '278 - 256x144 (144p)',
                        'protocol': 'https', 'http_headers': {
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}},
                       {'format_id': '160',
                        'url': 'https://r7---sn-u2oxu-f5fr.googlevideo.com/videoplayback?expire=1590022021&ei=JXvFXoeLMMP17QThhJqoCw&ip=193.43.136.244&id=o-AFwqoKNBYJ7NS_gkkc6b2P1Pg8JYKSiut529sf8D2_dM&itag=160&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278&source=youtube&requiressl=yes&mh=AI&mm=31%2C26&mn=sn-u2oxu-f5fr%2Csn-4g5e6nsy&ms=au%2Conr&mv=m&mvi=6&pl=24&initcwndbps=592500&vprv=1&mime=video%2Fmp4&gir=yes&clen=2178398&dur=159.592&lmt=1566414610484287&mt=1590000341&fvip=2&keepalive=yes&beids=9466586&c=WEB&txp=2316222&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgZp4d2EVBEajfObyIiOm9g_a9tM7f5UOaOP_qJ1Xq7xoCIQDxMuM6xZicpHf_Au8m4r1UfXowHrk9cFn5-Xl8uuFEoQ%3D%3D&sig=AOq0QJ8wRAIgFlmHUiOaTQIZOH71S22H11XQlM7JT3eEx6XV1wU55sECIDwLvD5jVwAzKgOMWfrDQBtVLcCEufkFEw3XqVMMP1c-&ratebypass=yes',
                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'ext': 'mp4', 'height': 144,
                        'format_note': '144p', 'vcodec': 'avc1.4d400c', 'asr': None, 'filesize': 2178398, 'fps': 30,
                        'tbr': 154.219, 'width': 256, 'acodec': 'none',
                        'downloader_options': {'http_chunk_size': 10485760}, 'format': '160 - 256x144 (144p)',
                        'protocol': 'https', 'http_headers': {
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}},
                       {'format_id': '242',
                        'url': 'https://r7---sn-u2oxu-f5fr.googlevideo.com/videoplayback?expire=1590022021&ei=JXvFXoeLMMP17QThhJqoCw&ip=193.43.136.244&id=o-AFwqoKNBYJ7NS_gkkc6b2P1Pg8JYKSiut529sf8D2_dM&itag=242&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278&source=youtube&requiressl=yes&mh=AI&mm=31%2C26&mn=sn-u2oxu-f5fr%2Csn-4g5e6nsy&ms=au%2Conr&mv=m&mvi=6&pl=24&initcwndbps=592500&vprv=1&mime=video%2Fwebm&gir=yes&clen=4258299&dur=159.592&lmt=1566414603617497&mt=1590000341&fvip=2&keepalive=yes&beids=9466586&c=WEB&txp=2316222&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgZp4d2EVBEajfObyIiOm9g_a9tM7f5UOaOP_qJ1Xq7xoCIQDxMuM6xZicpHf_Au8m4r1UfXowHrk9cFn5-Xl8uuFEoQ%3D%3D&sig=AOq0QJ8wRAIgTg3QeyBKIa4hLnChm0kacyfs-Ik8QOtHiAOUz8TSVLsCIC61LtnGa5jOjQGmVKfmxrvSRhIHLL-12I4BDvc-UqzK&ratebypass=yes',
                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'ext': 'webm',
                        'height': 240, 'format_note': '240p', 'vcodec': 'vp9', 'asr': None, 'filesize': 4258299,
                        'fps': 30, 'tbr': 281.672, 'width': 426, 'acodec': 'none',
                        'downloader_options': {'http_chunk_size': 10485760}, 'format': '242 - 426x240 (240p)',
                        'protocol': 'https', 'http_headers': {
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}},
                       {'format_id': '133',
                        'url': 'https://r7---sn-u2oxu-f5fr.googlevideo.com/videoplayback?expire=1590022021&ei=JXvFXoeLMMP17QThhJqoCw&ip=193.43.136.244&id=o-AFwqoKNBYJ7NS_gkkc6b2P1Pg8JYKSiut529sf8D2_dM&itag=133&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278&source=youtube&requiressl=yes&mh=AI&mm=31%2C26&mn=sn-u2oxu-f5fr%2Csn-4g5e6nsy&ms=au%2Conr&mv=m&mvi=6&pl=24&initcwndbps=592500&vprv=1&mime=video%2Fmp4&gir=yes&clen=4816879&dur=159.592&lmt=1566414610648857&mt=1590000341&fvip=2&keepalive=yes&beids=9466586&c=WEB&txp=2316222&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgZp4d2EVBEajfObyIiOm9g_a9tM7f5UOaOP_qJ1Xq7xoCIQDxMuM6xZicpHf_Au8m4r1UfXowHrk9cFn5-Xl8uuFEoQ%3D%3D&sig=AOq0QJ8wRQIhAN5kvIO9G6VPZVvTF1OvoX_-26FRvWLiz4-h_iy1OxAIAiBwWdlSGjurXxe0TBKxHgljohufMk9CTfvmsJGW0PIGgw==&ratebypass=yes',
                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'ext': 'mp4', 'height': 240,
                        'format_note': '240p', 'vcodec': 'avc1.4d4015', 'asr': None, 'filesize': 4816879, 'fps': 30,
                        'tbr': 344.994, 'width': 426, 'acodec': 'none',
                        'downloader_options': {'http_chunk_size': 10485760}, 'format': '133 - 426x240 (240p)',
                        'protocol': 'https', 'http_headers': {
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}},
                       {'format_id': '243',
                        'url': 'https://r7---sn-u2oxu-f5fr.googlevideo.com/videoplayback?expire=1590022021&ei=JXvFXoeLMMP17QThhJqoCw&ip=193.43.136.244&id=o-AFwqoKNBYJ7NS_gkkc6b2P1Pg8JYKSiut529sf8D2_dM&itag=243&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278&source=youtube&requiressl=yes&mh=AI&mm=31%2C26&mn=sn-u2oxu-f5fr%2Csn-4g5e6nsy&ms=au%2Conr&mv=m&mvi=6&pl=24&initcwndbps=592500&vprv=1&mime=video%2Fwebm&gir=yes&clen=7632998&dur=159.592&lmt=1566414603611090&mt=1590000341&fvip=2&keepalive=yes&beids=9466586&c=WEB&txp=2316222&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgZp4d2EVBEajfObyIiOm9g_a9tM7f5UOaOP_qJ1Xq7xoCIQDxMuM6xZicpHf_Au8m4r1UfXowHrk9cFn5-Xl8uuFEoQ%3D%3D&sig=AOq0QJ8wRQIgQmuISdzZF83U7MPCNAIvDHNYVW8U7Q-aLy3X9zmLORECIQC8krS0q6K7GQZNTZzSPyaqIxhA_BUIxgue-xYJRVUu5w==&ratebypass=yes',
                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'ext': 'webm',
                        'height': 360, 'format_note': '360p', 'vcodec': 'vp9', 'asr': None, 'filesize': 7632998,
                        'fps': 30, 'tbr': 544.539, 'width': 640, 'acodec': 'none',
                        'downloader_options': {'http_chunk_size': 10485760}, 'format': '243 - 640x360 (360p)',
                        'protocol': 'https', 'http_headers': {
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}},
                       {'format_id': '134',
                        'url': 'https://r7---sn-u2oxu-f5fr.googlevideo.com/videoplayback?expire=1590022021&ei=JXvFXoeLMMP17QThhJqoCw&ip=193.43.136.244&id=o-AFwqoKNBYJ7NS_gkkc6b2P1Pg8JYKSiut529sf8D2_dM&itag=134&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278&source=youtube&requiressl=yes&mh=AI&mm=31%2C26&mn=sn-u2oxu-f5fr%2Csn-4g5e6nsy&ms=au%2Conr&mv=m&mvi=6&pl=24&initcwndbps=592500&vprv=1&mime=video%2Fmp4&gir=yes&clen=10539026&dur=159.592&lmt=1566414610502805&mt=1590000341&fvip=2&keepalive=yes&beids=9466586&c=WEB&txp=2316222&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgZp4d2EVBEajfObyIiOm9g_a9tM7f5UOaOP_qJ1Xq7xoCIQDxMuM6xZicpHf_Au8m4r1UfXowHrk9cFn5-Xl8uuFEoQ%3D%3D&sig=AOq0QJ8wRQIgfgF-Oymtu_n0N61hYg_4ZR5ztWxk8Bwfv6B95v-EttMCIQCio4Q2h-vsGuXicRKw5PyZWwXot-VCOaN5HnBoh4BhLA==&ratebypass=yes',
                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'ext': 'mp4', 'height': 360,
                        'format_note': '360p', 'vcodec': 'avc1.4d401e', 'asr': None, 'filesize': 10539026, 'fps': 30,
                        'tbr': 783.596, 'width': 640, 'acodec': 'none',
                        'downloader_options': {'http_chunk_size': 10485760}, 'format': '134 - 640x360 (360p)',
                        'protocol': 'https', 'http_headers': {
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}},
                       {'format_id': '244',
                        'url': 'https://r7---sn-u2oxu-f5fr.googlevideo.com/videoplayback?expire=1590022021&ei=JXvFXoeLMMP17QThhJqoCw&ip=193.43.136.244&id=o-AFwqoKNBYJ7NS_gkkc6b2P1Pg8JYKSiut529sf8D2_dM&itag=244&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278&source=youtube&requiressl=yes&mh=AI&mm=31%2C26&mn=sn-u2oxu-f5fr%2Csn-4g5e6nsy&ms=au%2Conr&mv=m&mvi=6&pl=24&initcwndbps=592500&vprv=1&mime=video%2Fwebm&gir=yes&clen=13665819&dur=159.592&lmt=1566414603607282&mt=1590000341&fvip=2&keepalive=yes&beids=9466586&c=WEB&txp=2316222&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgZp4d2EVBEajfObyIiOm9g_a9tM7f5UOaOP_qJ1Xq7xoCIQDxMuM6xZicpHf_Au8m4r1UfXowHrk9cFn5-Xl8uuFEoQ%3D%3D&sig=AOq0QJ8wRQIgbAEzSR_wmS_HE2L-O3qHFqFjrcBTlAi_9w7R2OWDEl8CIQCo-MuWcG49dT7YM2DD8If9sGzakfelUsTeX9oZDkxghw==&ratebypass=yes',
                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'ext': 'webm',
                        'height': 480, 'format_note': '480p', 'vcodec': 'vp9', 'asr': None, 'filesize': 13665819,
                        'fps': 30, 'tbr': 982.873, 'width': 854, 'acodec': 'none',
                        'downloader_options': {'http_chunk_size': 10485760}, 'format': '244 - 854x480 (480p)',
                        'protocol': 'https', 'http_headers': {
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}},
                       {'format_id': '135',
                        'url': 'https://r7---sn-u2oxu-f5fr.googlevideo.com/videoplayback?expire=1590022021&ei=JXvFXoeLMMP17QThhJqoCw&ip=193.43.136.244&id=o-AFwqoKNBYJ7NS_gkkc6b2P1Pg8JYKSiut529sf8D2_dM&itag=135&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278&source=youtube&requiressl=yes&mh=AI&mm=31%2C26&mn=sn-u2oxu-f5fr%2Csn-4g5e6nsy&ms=au%2Conr&mv=m&mvi=6&pl=24&initcwndbps=592500&vprv=1&mime=video%2Fmp4&gir=yes&clen=19934549&dur=159.592&lmt=1566414610497024&mt=1590000341&fvip=2&keepalive=yes&beids=9466586&c=WEB&txp=2316222&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgZp4d2EVBEajfObyIiOm9g_a9tM7f5UOaOP_qJ1Xq7xoCIQDxMuM6xZicpHf_Au8m4r1UfXowHrk9cFn5-Xl8uuFEoQ%3D%3D&sig=AOq0QJ8wRAIgUGYcmv-4DAZolLq075z7as8YnOIFERri6Jib-G9TLv0CIGmEgKvfi0GDsuX-rv_1PO_onna8X4CQLfP9sneICf0W&ratebypass=yes',
                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'ext': 'mp4', 'height': 480,
                        'format_note': '480p', 'vcodec': 'avc1.4d401f', 'asr': None, 'filesize': 19934549, 'fps': 30,
                        'tbr': 1407.647, 'width': 854, 'acodec': 'none',
                        'downloader_options': {'http_chunk_size': 10485760}, 'format': '135 - 854x480 (480p)',
                        'protocol': 'https', 'http_headers': {
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}},
                       {'format_id': '247',
                        'url': 'https://r7---sn-u2oxu-f5fr.googlevideo.com/videoplayback?expire=1590022021&ei=JXvFXoeLMMP17QThhJqoCw&ip=193.43.136.244&id=o-AFwqoKNBYJ7NS_gkkc6b2P1Pg8JYKSiut529sf8D2_dM&itag=247&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278&source=youtube&requiressl=yes&mh=AI&mm=31%2C26&mn=sn-u2oxu-f5fr%2Csn-4g5e6nsy&ms=au%2Conr&mv=m&mvi=6&pl=24&initcwndbps=592500&vprv=1&mime=video%2Fwebm&gir=yes&clen=25973561&dur=159.592&lmt=1566414603617699&mt=1590000341&fvip=2&keepalive=yes&beids=9466586&c=WEB&txp=2316222&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgZp4d2EVBEajfObyIiOm9g_a9tM7f5UOaOP_qJ1Xq7xoCIQDxMuM6xZicpHf_Au8m4r1UfXowHrk9cFn5-Xl8uuFEoQ%3D%3D&sig=AOq0QJ8wRQIhAIaSAz_W2M8r9ncqvmjO5UqFKrd8hSeC3iRZi2x_UQC1AiBU7_cVg3HxgH-tJCYIjurT3PDMv8tUSYdl8xgNpw2Udw==&ratebypass=yes',
                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'ext': 'webm',
                        'height': 720, 'format_note': '720p', 'vcodec': 'vp9', 'asr': None, 'filesize': 25973561,
                        'fps': 30, 'tbr': 2158.105, 'width': 1280, 'acodec': 'none',
                        'downloader_options': {'http_chunk_size': 10485760}, 'format': '247 - 1280x720 (720p)',
                        'protocol': 'https', 'http_headers': {
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}},
                       {'format_id': '136',
                        'url': 'https://r7---sn-u2oxu-f5fr.googlevideo.com/videoplayback?expire=1590022021&ei=JXvFXoeLMMP17QThhJqoCw&ip=193.43.136.244&id=o-AFwqoKNBYJ7NS_gkkc6b2P1Pg8JYKSiut529sf8D2_dM&itag=136&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278&source=youtube&requiressl=yes&mh=AI&mm=31%2C26&mn=sn-u2oxu-f5fr%2Csn-4g5e6nsy&ms=au%2Conr&mv=m&mvi=6&pl=24&initcwndbps=592500&vprv=1&mime=video%2Fmp4&gir=yes&clen=39211954&dur=159.592&lmt=1566414610482438&mt=1590000341&fvip=2&keepalive=yes&beids=9466586&c=WEB&txp=2316222&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgZp4d2EVBEajfObyIiOm9g_a9tM7f5UOaOP_qJ1Xq7xoCIQDxMuM6xZicpHf_Au8m4r1UfXowHrk9cFn5-Xl8uuFEoQ%3D%3D&sig=AOq0QJ8wRAIgUvzVSXH8Oc7u8lDsD03DBxDjUlSdB_mfHpW6ql0MSboCIGoy2IM-7rclS2duqcSM9KHUwS1JN567TRicJ33fIhq9&ratebypass=yes',
                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'ext': 'mp4', 'height': 720,
                        'format_note': '720p', 'vcodec': 'avc1.4d401f', 'asr': None, 'filesize': 39211954, 'fps': 30,
                        'tbr': 2883.951, 'width': 1280, 'acodec': 'none',
                        'downloader_options': {'http_chunk_size': 10485760}, 'format': '136 - 1280x720 (720p)',
                        'protocol': 'https', 'http_headers': {
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}},
                       {'format_id': '248',
                        'url': 'https://r7---sn-u2oxu-f5fr.googlevideo.com/videoplayback?expire=1590022021&ei=JXvFXoeLMMP17QThhJqoCw&ip=193.43.136.244&id=o-AFwqoKNBYJ7NS_gkkc6b2P1Pg8JYKSiut529sf8D2_dM&itag=248&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278&source=youtube&requiressl=yes&mh=AI&mm=31%2C26&mn=sn-u2oxu-f5fr%2Csn-4g5e6nsy&ms=au%2Conr&mv=m&mvi=6&pl=24&initcwndbps=592500&vprv=1&mime=video%2Fwebm&gir=yes&clen=41599214&dur=159.592&lmt=1566414603603667&mt=1590000341&fvip=2&keepalive=yes&beids=9466586&c=WEB&txp=2316222&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgZp4d2EVBEajfObyIiOm9g_a9tM7f5UOaOP_qJ1Xq7xoCIQDxMuM6xZicpHf_Au8m4r1UfXowHrk9cFn5-Xl8uuFEoQ%3D%3D&sig=AOq0QJ8wRAIgY_FthY6t8MHrsruUGAy0mEnTq5j6I7-nyKNDvcFT8BECIDNSoODmOdylcfLLeUhM5IUeT2HEvF2cgQCt4HaaV_9y&ratebypass=yes',
                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'ext': 'webm',
                        'height': 1080, 'format_note': '1080p', 'vcodec': 'vp9', 'asr': None, 'filesize': 41599214,
                        'fps': 30, 'tbr': 3306.94, 'width': 1920, 'acodec': 'none',
                        'downloader_options': {'http_chunk_size': 10485760}, 'format': '248 - 1920x1080 (1080p)',
                        'protocol': 'https', 'http_headers': {
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}},
                       {'format_id': '137',
                        'url': 'https://r7---sn-u2oxu-f5fr.googlevideo.com/videoplayback?expire=1590022021&ei=JXvFXoeLMMP17QThhJqoCw&ip=193.43.136.244&id=o-AFwqoKNBYJ7NS_gkkc6b2P1Pg8JYKSiut529sf8D2_dM&itag=137&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278&source=youtube&requiressl=yes&mh=AI&mm=31%2C26&mn=sn-u2oxu-f5fr%2Csn-4g5e6nsy&ms=au%2Conr&mv=m&mvi=6&pl=24&initcwndbps=592500&vprv=1&mime=video%2Fmp4&gir=yes&clen=77870667&dur=159.592&lmt=1566414610481783&mt=1590000341&fvip=2&keepalive=yes&beids=9466586&c=WEB&txp=2316222&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgZp4d2EVBEajfObyIiOm9g_a9tM7f5UOaOP_qJ1Xq7xoCIQDxMuM6xZicpHf_Au8m4r1UfXowHrk9cFn5-Xl8uuFEoQ%3D%3D&sig=AOq0QJ8wRQIhANlIcS6UTZ-nwjqntb_YSU0ExbYWWVu0Em6Vh-Usthj1AiBu2rG3d60mk0rkIK_szjRX3BBNjw1HBiOixxNmChsBFQ==&ratebypass=yes',
                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'ext': 'mp4',
                        'height': 1080, 'format_note': '1080p', 'vcodec': 'avc1.640028', 'asr': None,
                        'filesize': 77870667, 'fps': 30, 'tbr': 5436.91, 'width': 1920, 'acodec': 'none',
                        'downloader_options': {'http_chunk_size': 10485760}, 'format': '137 - 1920x1080 (1080p)',
                        'protocol': 'https', 'http_headers': {
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}},
                       {'format_id': '18',
                        'url': 'https://r7---sn-u2oxu-f5fr.googlevideo.com/videoplayback?expire=1590022021&ei=JXvFXoeLMMP17QThhJqoCw&ip=193.43.136.244&id=o-AFwqoKNBYJ7NS_gkkc6b2P1Pg8JYKSiut529sf8D2_dM&itag=18&source=youtube&requiressl=yes&mh=AI&mm=31%2C26&mn=sn-u2oxu-f5fr%2Csn-4g5e6nsy&ms=au%2Conr&mv=m&mvi=6&pl=24&initcwndbps=592500&vprv=1&mime=video%2Fmp4&gir=yes&clen=13431311&ratebypass=yes&dur=159.660&lmt=1566414590249960&mt=1590000341&fvip=2&beids=9466586&c=WEB&txp=2311222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgZp4d2EVBEajfObyIiOm9g_a9tM7f5UOaOP_qJ1Xq7xoCIQDxMuM6xZicpHf_Au8m4r1UfXowHrk9cFn5-Xl8uuFEoQ%3D%3D&sig=AOq0QJ8wRAIgbwXnIJAoXrkTQDfCT-yYkybkp89YAi8W2rw5PihaheICIFj9E3cfuEJBveMeWcF2Iyz7emDN3P4cgOoruKW-jkbr',
                        'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js', 'ext': 'mp4', 'width': 640,
                        'height': 360, 'acodec': 'mp4a.40.2', 'abr': 96, 'vcodec': 'avc1.42001E', 'asr': 44100,
                        'filesize': 13431311, 'format_note': '360p', 'fps': 30, 'tbr': 673.282,
                        'format': '18 - 640x360 (360p)', 'protocol': 'https', 'http_headers': {
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5'}}], 'is_live': None,
                    'start_time': None, 'end_time': None, 'series': None, 'season_number': None, 'episode_number': None,
                    'track': 'The Story of Light', 'artist': 'Steve Vai', 'album': None, 'release_date': None,
                    'release_year': None, 'extractor': 'youtube', 'webpage_url_basename': 'watch',
                    'extractor_key': 'Youtube', 'playlist': None, 'playlist_index': None,
                    'thumbnails': [{'url': 'https://i.ytimg.com/vi/-s58ryovTDc/maxresdefault.jpg', 'id': '0'}],
                    'display_id': '-s58ryovTDc', 'requested_subtitles': None, 'requested_formats': ({'format_id': '137',
                                                                                                     'url': 'https://r7---sn-u2oxu-f5fr.googlevideo.com/videoplayback?expire=1590022021&ei=JXvFXoeLMMP17QThhJqoCw&ip=193.43.136.244&id=o-AFwqoKNBYJ7NS_gkkc6b2P1Pg8JYKSiut529sf8D2_dM&itag=137&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278&source=youtube&requiressl=yes&mh=AI&mm=31%2C26&mn=sn-u2oxu-f5fr%2Csn-4g5e6nsy&ms=au%2Conr&mv=m&mvi=6&pl=24&initcwndbps=592500&vprv=1&mime=video%2Fmp4&gir=yes&clen=77870667&dur=159.592&lmt=1566414610481783&mt=1590000341&fvip=2&keepalive=yes&beids=9466586&c=WEB&txp=2316222&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgZp4d2EVBEajfObyIiOm9g_a9tM7f5UOaOP_qJ1Xq7xoCIQDxMuM6xZicpHf_Au8m4r1UfXowHrk9cFn5-Xl8uuFEoQ%3D%3D&sig=AOq0QJ8wRQIhANlIcS6UTZ-nwjqntb_YSU0ExbYWWVu0Em6Vh-Usthj1AiBu2rG3d60mk0rkIK_szjRX3BBNjw1HBiOixxNmChsBFQ==&ratebypass=yes',
                                                                                                     'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js',
                                                                                                     'ext': 'mp4',
                                                                                                     'height': 1080,
                                                                                                     'format_note': '1080p',
                                                                                                     'vcodec': 'avc1.640028',
                                                                                                     'asr': None,
                                                                                                     'filesize': 77870667,
                                                                                                     'fps': 30,
                                                                                                     'tbr': 5436.91,
                                                                                                     'width': 1920,
                                                                                                     'acodec': 'none',
                                                                                                     'downloader_options': {
                                                                                                         'http_chunk_size': 10485760},
                                                                                                     'format': '137 - 1920x1080 (1080p)',
                                                                                                     'protocol': 'https',
                                                                                                     'http_headers': {
                                                                                                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                                                                                                         'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                                                                                                         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                                                                                         'Accept-Encoding': 'gzip, deflate',
                                                                                                         'Accept-Language': 'en-us,en;q=0.5'}},
                                                                                                    {'format_id': '251',
                                                                                                     'url': 'https://r7---sn-u2oxu-f5fr.googlevideo.com/videoplayback?expire=1590022021&ei=JXvFXoeLMMP17QThhJqoCw&ip=193.43.136.244&id=o-AFwqoKNBYJ7NS_gkkc6b2P1Pg8JYKSiut529sf8D2_dM&itag=251&source=youtube&requiressl=yes&mh=AI&mm=31%2C26&mn=sn-u2oxu-f5fr%2Csn-4g5e6nsy&ms=au%2Conr&mv=m&mvi=6&pl=24&initcwndbps=592500&vprv=1&mime=audio%2Fwebm&gir=yes&clen=2576924&dur=159.621&lmt=1566415046443545&mt=1590000341&fvip=2&keepalive=yes&beids=9466586&c=WEB&txp=2301222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgZp4d2EVBEajfObyIiOm9g_a9tM7f5UOaOP_qJ1Xq7xoCIQDxMuM6xZicpHf_Au8m4r1UfXowHrk9cFn5-Xl8uuFEoQ%3D%3D&sig=AOq0QJ8wRQIgCFWV3zlMWilqFCe_8-e63FiC8nkq4_ap31xH9VoEEcMCIQCJo0TaDYBXn0b-GCPHJE-K8AKA34An3P_pP_Qm4EkkAw==&ratebypass=yes',
                                                                                                     'player_url': '/s/player/e3cd195e/player_ias.vflset/en_US/base.js',
                                                                                                     'ext': 'webm',
                                                                                                     'format_note': 'tiny',
                                                                                                     'acodec': 'opus',
                                                                                                     'abr': 160,
                                                                                                     'asr': 48000,
                                                                                                     'filesize': 2576924,
                                                                                                     'fps': None,
                                                                                                     'height': None,
                                                                                                     'tbr': 139.201,
                                                                                                     'width': None,
                                                                                                     'vcodec': 'none',
                                                                                                     'downloader_options': {
                                                                                                         'http_chunk_size': 10485760},
                                                                                                     'format': '251 - audio only (tiny)',
                                                                                                     'protocol': 'https',
                                                                                                     'http_headers': {
                                                                                                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3706.6 Safari/537.36',
                                                                                                         'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
                                                                                                         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                                                                                         'Accept-Encoding': 'gzip, deflate',
                                                                                                         'Accept-Language': 'en-us,en;q=0.5'}}),
                    'format': '137 - 1920x1080 (1080p)+251 - audio only (tiny)', 'format_id': '137+251', 'width': 1920,
                    'height': 1080, 'resolution': None, 'fps': 30, 'vcodec': 'avc1.640028', 'vbr': None,
                    'stretched_ratio': None, 'acodec': 'opus', 'abr': 160, 'ext': 'mp4'}]

"""
This is second page 
after pressing 
DOWNLOAD button
-> show what could be downloaded
and use checkboxes to tick if interested in downloading """

ydl_opts = {
    'ignoreerrors': True,
    'quiet': False
}

youtube_dl_opts = {}


def pretty_print_results(result):
    pp = pprint.PrettyPrinter(depth=2)
    return pp.pformat(result)


def get_info(video):
    output = []
    for i in range(len(video)):
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video[i], download=False)
            output.append(info_dict)
    return output


# pretty_print_results(get_info(video))
def frame(title, inside_text):
    output = []

    def one_frame(title, inside_text):
        return [sg.Frame(title=title, layout=[[sg.Text(inside_text)]])]

    for i in range(len(title)):
        output.append(one_frame(title[i], inside_text[i]))
    # print(title)
    print("\n\n\n\n\n", inside_text)
    return output


# TODO do list
# def table(data):
#     return [[sg.Table]]

def create_window(data_input):
    output = []
    # add tags
    title = []
    inside_text = []
    for j in range(len(data_input)):
        data = (data_input[j])
        title.append(data["artist"])
        current_average = float(data["average_rating"]) / 5 * 100
        inside_text.append("\ntitle:\t\t" + data["title"] \
                           + "\nuploader_id:\t" + str(data["uploader_id"]) \
                           + "\naverage rating:\t" + str("{:.2f}").format(current_average) + " %" \
                           + "\nview_count:\t" + str(data["view_count"]) \
                           + "\n")

    # activate frame here in layout =
    window = sg.Window('Frame with buttons', layout=([[sg.Frame(layout=frame(title, inside_text), title="frame out")]]),
                       font=("Helvetica", 12))
    event, values = window.read()
    window.close()


title = ["title", "53544823658", 2, 3, 4, 5]

data = {
    "title": title[1],
    "inside_text": "inside_text xxx",
    "number_of_frames": 1,
}
# create_window(results_dictionary)

video = ["https://www.youtube.com/watch?v=Pl46Qsk-Wvs",
         "https://www.youtube.com/watch?v=-s58ryovTDc",
         "https://www.youtube.com/watch?v=txezAqv-0Mg",
         "https://www.youtube.com/watch?v=Rk0NIQfEXBA",
         "https://www.youtube.com/watch?v=LjLn3H1_1Gw",
         "https://www.youtube.com/watch?v=uYgxa_VMq0E",
         "https://www.youtube.com/watch?v=YJVmu6yttiw"]


# print(get_info_output)
# get_info(video)
# print(get_info_output[1]['title'])


def save_results_file(file, results):
    with open(file, 'w', encoding="utf-8") as f:
        f.write(str(pretty_print_results(results)))


output_real = (get_info(video))
save_results_file("searching_results-SAMPLE1.txt", output_real)


# pretty_print_results(output_real)


# create_window(get_info_output)
# create_window(output_real)
