from classbangumimark import BangumiMark

BgmMark = BangumiMark(218971)
if BgmMark.anime_dict['type'] == 2:
    BgmMark.calculate()
    BgmMark.write_file()
