# import unittest
from youtube_instrumentals import gui, backend_ydl

class Testing: #(unittest.TestCase):
  def test_multiple_keywords_and_offline(self):
    example_values = [
      ['programming focus', 5],
      ['reverse engineering', 2],
      ['hackme', 20],
      ['real estates', 3],
    ]
    SAMPLE_INPUT = {
      0: None,
      10: 'test3', 11: '3.14', 12: '1: Without Separation : Whole track',
      20: 'inne', 21: '4', 22: '1: Without Separation : Whole track',
      30: '', 31: 0, 32: '1: Without Separation : Whole track',
      40: '', 41: 0, 42: '1: Without Separation : Whole track',
      50: '', 51: 0, 52: '1: Without Separation : Whole track',
      60: '', 61: 0, 62: '1: Without Separation : Whole track',
      70: '', 71: 0, 72: '1: Without Separation : Whole track',
      80: '', 81: 0, 82: '1: Without Separation : Whole track',
      90: '', 91: 0, 92: '1: Without Separation : Whole track',
      100: '', 101: 0, 102: '1: Without Separation : Whole track'
    }
    SAMPLE_INPUT = {**SAMPLE_INPUT, 10: 'inappropriate number of events', 11: '3'}

    '''
    This class has just to offer the interface:
      `YoutubeDL(YDL_SIMULATE_OPTS).extract_info(name)`
    '''
    class YtDownloaderMock:
      def __init__(self):
        pass

      def YoutubeDL(YDL_SIMULATE_OPTS):
        class YTDL():
          def extract_info(name):
            raise Exception("You are offline!")
            return {1: 1}
        return YTDL()

    # args = {"min_views": 15, "min_views2": 15}
    # args = dict(min_views = 10)
    args_array = [15, 15]

    gui_output = gui.main(SAMPLE_INPUT) # , **args)

    info = backend_ydl.parse(gui_output, youtube_dl = YtDownloaderMock())
    assert len(info) == 1, 'Not enough results from GUI.main'
    assert len(info[0]) == 2, 'Not enough elements in first result'
    assert info[0][0] == SAMPLE_INPUT[10], 'Error: keyword was parsed wrong'
    print(info)

if __name__ == '__main__':
  # unittest.main()
  test = Testing()
  test.test_multiple_keywords_and_offline()
