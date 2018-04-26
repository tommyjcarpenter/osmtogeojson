from osmtogeojson import merge

def test_line_cleanup():

    dirty_input = {"type": "Feature", "id": "relation/563476", "properties": {"network": "US:NJ:Union", "ref": "651", "route": "road", "type": "route", "id": "relation/563476"}, "geometry": {"type": "MultiLineString", "coordinates": [[[-74.3398261, 40.7159394], [-74.3399473, 40.7158838], [-74.340076, 40.715781], [-74.340283, 40.715584], [-74.340515, 40.71532], [-74.340663, 40.715158], [-74.341017, 40.714769], [-74.341301, 40.714454], [-74.341526, 40.714204], [-74.341986, 40.713772], [-74.342247, 40.7135594]], [[-74.342247, 40.7135594], [-74.3426316, 40.7132707], [-74.342866, 40.713089], [-74.343733, 40.712494], [-74.344032, 40.712314], [-74.344484, 40.712095], [-74.3446858, 40.7120132], [-74.3448779, 40.7119443]], [[-74.3448779, 40.7119443], [-74.3452756, 40.711861], [-74.3454053, 40.7118325], [-74.3459905, 40.7117366], [-74.3460798, 40.711726], [-74.3463025, 40.7116996], [-74.3466338, 40.7116869], [-74.3468979, 40.711696], [-74.3471043, 40.711716], [-74.3479281, 40.7118145], [-74.3489379, 40.7119528], [-74.3501015, 40.712103], [-74.350224, 40.7121066], [-74.3504232, 40.7120902], [-74.3505457, 40.7120629], [-74.3506729, 40.7120247], [-74.3507881, 40.711961], [-74.3513343, 40.7116021]], [[-74.3513343, 40.7116021], [-74.3516964, 40.7113985]], [[-74.3516964, 40.7113985], [-74.3517948, 40.7113515]], [[-74.3517948, 40.7113515], [-74.3521998, 40.7111568]], [[-74.3521998, 40.7111568], [-74.3527195, 40.7109302], [-74.3528203, 40.7108974], [-74.3529236, 40.7108738], [-74.3530367, 40.7108588], [-74.3531516, 40.7108537], [-74.3532713, 40.7108577], [-74.3533724, 40.710877], [-74.3534756, 40.7109085], [-74.354192, 40.7111772], [-74.3543027, 40.7112265], [-74.3543595, 40.7112596], [-74.354416, 40.7112926], [-74.3567618, 40.7126586], [-74.3572078, 40.7129082], [-74.3578675, 40.7133036], [-74.3579405, 40.7133473], [-74.3580134, 40.713389], [-74.3587118, 40.7137885], [-74.3587877, 40.7138325], [-74.3588624, 40.713872], [-74.3596921, 40.7143261], [-74.3599328, 40.7144575], [-74.3600412, 40.71453], [-74.3602565, 40.714664], [-74.3605969, 40.7148482], [-74.3606745, 40.7148928], [-74.360883, 40.715014]], [[-74.360883, 40.715014], [-74.361109, 40.715147], [-74.3617045, 40.7155075], [-74.361756, 40.7155387], [-74.3618895, 40.7156195], [-74.3625049, 40.715992], [-74.3627406, 40.7161347]], [[-74.3639786, 40.7168147], [-74.3640552, 40.7168705], [-74.3640812, 40.7168963], [-74.3641248, 40.7169486], [-74.3641998, 40.7170601], [-74.3645555, 40.7176226], [-74.3647043, 40.7178627], [-74.364882, 40.7180483]], [[-74.3635144, 40.7165666], [-74.3638801, 40.7167633], [-74.3639786, 40.7168147]], [[-74.3627406, 40.7161347], [-74.3628462, 40.7161948], [-74.3630028, 40.7162819], [-74.3635144, 40.7165666]], [[-74.364882, 40.7180483], [-74.3652037, 40.7183724]], [[-74.3652037, 40.7183724], [-74.3653045, 40.7184632], [-74.3655513, 40.7187133], [-74.3656857, 40.7188749], [-74.3657466, 40.7189822], [-74.3663557, 40.7202097], [-74.3664162, 40.720327], [-74.3664535, 40.7203992], [-74.3666395, 40.7207598], [-74.3668291, 40.7211092], [-74.367043, 40.721459], [-74.367153, 40.72166], [-74.3672527, 40.7218481], [-74.3673796, 40.7220233], [-74.3674811, 40.7221579], [-74.3675812, 40.7222829], [-74.3678236, 40.7225392], [-74.3680497, 40.7227483], [-74.3682514, 40.7229047], [-74.3684626, 40.7230576], [-74.3687747, 40.7232504], [-74.3690046, 40.7233935], [-74.3699846, 40.7239963], [-74.3707351, 40.7244842], [-74.3717088, 40.725165], [-74.3718578, 40.7252758], [-74.3723894, 40.7256267], [-74.3732517, 40.7261693], [-74.3742457, 40.7267334], [-74.3743468, 40.7267949], [-74.3744468, 40.7268677], [-74.3745205, 40.7269253], [-74.3746071, 40.7270153], [-74.3750385, 40.7274969], [-74.3754127, 40.7279106], [-74.375602, 40.7281198], [-74.3759428, 40.7285217], [-74.3762213, 40.7288502], [-74.3764074, 40.7290502]], [[-74.3767688, 40.7294124], [-74.3764074, 40.7290502]]]}}


    expected_output = {"geometry": {"coordinates": [[-74.3767688, 40.7294124], [-74.3764074, 40.7290502], [-74.3762213, 40.7288502], [-74.3759428, 40.7285217], [-74.375602, 40.7281198], [-74.3754127, 40.7279106], [-74.3750385, 40.7274969], [-74.3746071, 40.7270153], [-74.3745205, 40.7269253], [-74.3744468, 40.7268677], [-74.3743468, 40.7267949], [-74.3742457, 40.7267334], [-74.3732517, 40.7261693], [-74.3723894, 40.7256267], [-74.3718578, 40.7252758], [-74.3717088, 40.725165], [-74.3707351, 40.7244842], [-74.3699846, 40.7239963], [-74.3690046, 40.7233935], [-74.3687747, 40.7232504], [-74.3684626, 40.7230576], [-74.3682514, 40.7229047], [-74.3680497, 40.7227483], [-74.3678236, 40.7225392], [-74.3675812, 40.7222829], [-74.3674811, 40.7221579], [-74.3673796, 40.7220233], [-74.3672527, 40.7218481], [-74.367153, 40.72166], [-74.367043, 40.721459], [-74.3668291, 40.7211092], [-74.3666395, 40.7207598], [-74.3664535, 40.7203992], [-74.3664162, 40.720327], [-74.3663557, 40.7202097], [-74.3657466, 40.7189822], [-74.3656857, 40.7188749], [-74.3655513, 40.7187133], [-74.3653045, 40.7184632], [-74.3652037, 40.7183724], [-74.364882, 40.7180483], [-74.3647043, 40.7178627], [-74.3645555, 40.7176226], [-74.3641998, 40.7170601], [-74.3641248, 40.7169486], [-74.3640812, 40.7168963], [-74.3640552, 40.7168705], [-74.3639786, 40.7168147], [-74.3638801, 40.7167633], [-74.3635144, 40.7165666], [-74.3630028, 40.7162819], [-74.3628462, 40.7161948], [-74.3627406, 40.7161347], [-74.3625049, 40.715992], [-74.3618895, 40.7156195], [-74.361756, 40.7155387], [-74.3617045, 40.7155075], [-74.361109, 40.715147], [-74.360883, 40.715014], [-74.3606745, 40.7148928], [-74.3605969, 40.7148482], [-74.3602565, 40.714664], [-74.3600412, 40.71453], [-74.3599328, 40.7144575], [-74.3596921, 40.7143261], [-74.3588624, 40.713872], [-74.3587877, 40.7138325], [-74.3587118, 40.7137885], [-74.3580134, 40.713389], [-74.3579405, 40.7133473], [-74.3578675, 40.7133036], [-74.3572078, 40.7129082], [-74.3567618, 40.7126586], [-74.354416, 40.7112926], [-74.3543595, 40.7112596], [-74.3543027, 40.7112265], [-74.354192, 40.7111772], [-74.3534756, 40.7109085], [-74.3533724, 40.710877], [-74.3532713, 40.7108577], [-74.3531516, 40.7108537], [-74.3530367, 40.7108588], [-74.3529236, 40.7108738], [-74.3528203, 40.7108974], [-74.3527195, 40.7109302], [-74.3521998, 40.7111568], [-74.3517948, 40.7113515], [-74.3516964, 40.7113985], [-74.3513343, 40.7116021], [-74.3507881, 40.711961], [-74.3506729, 40.7120247], [-74.3505457, 40.7120629], [-74.3504232, 40.7120902], [-74.350224, 40.7121066], [-74.3501015, 40.712103], [-74.3489379, 40.7119528], [-74.3479281, 40.7118145], [-74.3471043, 40.711716], [-74.3468979, 40.711696], [-74.3466338, 40.7116869], [-74.3463025, 40.7116996], [-74.3460798, 40.711726], [-74.3459905, 40.7117366], [-74.3454053, 40.7118325], [-74.3452756, 40.711861], [-74.3448779, 40.7119443], [-74.3446858, 40.7120132], [-74.344484, 40.712095], [-74.344032, 40.712314], [-74.343733, 40.712494], [-74.342866, 40.713089], [-74.3426316, 40.7132707], [-74.342247, 40.7135594], [-74.341986, 40.713772], [-74.341526, 40.714204], [-74.341301, 40.714454], [-74.341017, 40.714769], [-74.340663, 40.715158], [-74.340515, 40.71532], [-74.340283, 40.715584], [-74.340076, 40.715781], [-74.3399473, 40.7158838], [-74.3398261, 40.7159394]], "type": "LineString"}, "id": "relation/563476", "properties": {"id": "relation/563476", "network": "US:NJ:Union", "ref": "651", "route": "road", "type": "route"}, "type": "Feature"}

    # I do not care which way the line string goes
    dirty_input["geometry"]["coordinates"] = list(reversed(dirty_input["geometry"]["coordinates"]))
    assert merge.merge_line_string(dirty_input) == expected_output


def test_line_test_cleanup_polygon():

    dirty_input = {"type": "Feature", "id": "relation/170513", "properties": {"admin_level": "8", "border_type": "borough", "boundary": "administrative", "is_in": "USA, New Jersey", "is_in:country": "USA", "is_in:country_code": "US", "is_in:county": "Union, NJ", "is_in:iso_3166_2": "US:NJ", "is_in:state": "New Jersey", "is_in:state_code": "NJ", "name": "New Providence", "place": "borough", "source": "TIGER/Line\u00ae 2008 Place Shapefiles (http://www.census.gov/geo/www/tiger/)", "tiger:CLASSFP": "C5", "tiger:CPI": "N", "tiger:FUNCSTAT": "A", "tiger:LSAD": "21", "tiger:MTFCC": "G4110", "tiger:NAME": "New Providence", "tiger:NAMELSAD": "New Providence borough", "tiger:PCICBSA": "N", "tiger:PCINECTA": "N", "tiger:PLACEFP": "51810", "tiger:PLACENS": "00885321", "tiger:PLCIDFP": "3451810", "tiger:STATEFP": "34", "type": "boundary", "wikidata": "Q1021568", "wikipedia": "en:New Providence, New Jersey", "id": "relation/170513"}, "geometry": {"type": "MultiLineString", "coordinates": [[[-74.392757, 40.718046], [-74.392735, 40.717981], [-74.391905, 40.716111], [-74.391604, 40.71581], [-74.389769, 40.714158], [-74.388595, 40.713101], [-74.387157, 40.71229], [-74.386475, 40.71217], [-74.386193, 40.712128], [-74.3854378, 40.7114944], [-74.3847415, 40.710966], [-74.3846681, 40.7109009], [-74.3846341, 40.7108683], [-74.3846073, 40.7108168], [-74.3845518, 40.7106472], [-74.3844996, 40.7104712]], [[-74.3844996, 40.7104712], [-74.3844474, 40.7102604]], [[-74.3844474, 40.7102604], [-74.3844086, 40.709885], [-74.3843391, 40.7091525], [-74.3842681, 40.7084038], [-74.3840682, 40.7067936], [-74.3837837, 40.704551], [-74.3837037, 40.7041965], [-74.3835787, 40.7039003], [-74.3833834, 40.7035798], [-74.3829958, 40.7030845], [-74.3827652, 40.7028028], [-74.382573, 40.7025381], [-74.3824455, 40.7022649], [-74.3821406, 40.7014673], [-74.382035, 40.7009914], [-74.3819869, 40.7007389], [-74.3819805, 40.7005276], [-74.3819901, 40.7004013], [-74.3819709, 40.7002775], [-74.3819325, 40.7001755], [-74.38183, 40.7000614], [-74.3817083, 40.6999716], [-74.3814131, 40.6997804], [-74.381568, 40.699719], [-74.381737, 40.699608], [-74.382312, 40.699098], [-74.382638, 40.698807], [-74.383956, 40.697629], [-74.384045, 40.697552], [-74.38399, 40.697281], [-74.383595, 40.696101]], [[-74.429023, 40.698754], [-74.428965, 40.698808], [-74.428849, 40.698916], [-74.428707, 40.699119], [-74.428562, 40.699326], [-74.428389, 40.699574], [-74.428357, 40.69962], [-74.42835, 40.69963], [-74.428347, 40.699635], [-74.428038, 40.700077], [-74.428031, 40.700087], [-74.427997, 40.700136], [-74.426897, 40.701711], [-74.426491, 40.701885], [-74.425089, 40.701835], [-74.424733, 40.701957], [-74.424576, 40.702115], [-74.423922, 40.702775], [-74.423896, 40.702801], [-74.423552, 40.702867], [-74.422321, 40.703101], [-74.421796, 40.703201], [-74.418477, 40.705137], [-74.418453, 40.705151], [-74.418196, 40.705301], [-74.416596, 40.705301], [-74.4154, 40.705781], [-74.414453, 40.706579], [-74.413818, 40.707248], [-74.413796, 40.708001], [-74.41376, 40.708087], [-74.413757, 40.708093], [-74.413755, 40.708098], [-74.413702, 40.708225], [-74.413672, 40.708297], [-74.413631, 40.708395], [-74.413629, 40.7084], [-74.413621, 40.708418], [-74.413618, 40.708424], [-74.413614, 40.708434], [-74.41356, 40.708563], [-74.413524, 40.70865], [-74.413392, 40.708966], [-74.413061, 40.70987], [-74.412495, 40.7103], [-74.411847, 40.710345], [-74.411355, 40.710115], [-74.410806, 40.709567], [-74.410057, 40.709517], [-74.40911, 40.709812], [-74.408466, 40.710106], [-74.408448, 40.710156], [-74.408416, 40.710246], [-74.408175, 40.710925], [-74.408078, 40.711198], [-74.407575, 40.711795], [-74.407597, 40.711936], [-74.407698, 40.712599], [-74.407528, 40.713232], [-74.407504, 40.713263], [-74.40735, 40.713461], [-74.407277, 40.713523], [-74.407248, 40.713547], [-74.40724, 40.713554], [-74.407222, 40.713569], [-74.407128, 40.713649], [-74.407089, 40.713682], [-74.407072, 40.713696], [-74.406961, 40.71379], [-74.406948, 40.713801], [-74.406944, 40.713805], [-74.406939, 40.713809], [-74.406918, 40.713827], [-74.406768, 40.713954], [-74.406657, 40.714048], [-74.406126, 40.714498], [-74.405038, 40.714943], [-74.404574, 40.715245], [-74.40375, 40.716023], [-74.403096, 40.717123], [-74.402717, 40.717518], [-74.402633, 40.717605], [-74.402541, 40.717701], [-74.402518, 40.717725], [-74.402514, 40.71773], [-74.402507, 40.717737], [-74.40248, 40.717765], [-74.402254, 40.718001], [-74.401665, 40.718085], [-74.400853, 40.718023], [-74.400275, 40.71798], [-74.400144, 40.717936], [-74.399848, 40.717836], [-74.399268, 40.717738], [-74.398828, 40.717786], [-74.398605, 40.717811], [-74.398443, 40.717829], [-74.398436, 40.71783], [-74.398418, 40.717832], [-74.398248, 40.717851], [-74.397355, 40.717638], [-74.396069, 40.717277], [-74.396013, 40.717261], [-74.39509, 40.717273], [-74.394295, 40.717501], [-74.394151, 40.717582], [-74.393484, 40.717958], [-74.392937, 40.718024], [-74.392757, 40.718046]], [[-74.383595, 40.696101], [-74.384095, 40.696001], [-74.384907, 40.695634], [-74.386219, 40.69503], [-74.387416, 40.694189], [-74.38788, 40.693874], [-74.388473, 40.693534], [-74.38948, 40.69292], [-74.391946, 40.691692], [-74.3927733, 40.6914829], [-74.395363, 40.690551], [-74.395487, 40.690502], [-74.396499, 40.689896], [-74.395984, 40.688596], [-74.396132, 40.688109], [-74.3970168, 40.6871477], [-74.397127, 40.68702], [-74.3991167, 40.6864162], [-74.3994791, 40.6863601], [-74.4010583, 40.6856214], [-74.401694, 40.6855713], [-74.4028463, 40.6845451], [-74.404477, 40.683213], [-74.405075, 40.683014], [-74.405483, 40.682737], [-74.410653, 40.679228], [-74.41155, 40.680325], [-74.411868, 40.680115], [-74.412931, 40.679469], [-74.41366, 40.680724], [-74.413699, 40.680724], [-74.413728, 40.680719], [-74.4141315, 40.6814593], [-74.414595, 40.6825755], [-74.4148253, 40.6835857], [-74.415031, 40.68442], [-74.4155882, 40.6849079], [-74.4157398, 40.6850339], [-74.416375, 40.685502], [-74.41744, 40.686205], [-74.417912, 40.686506], [-74.418317, 40.686985], [-74.418743, 40.687353], [-74.418795, 40.687449], [-74.419361, 40.688093], [-74.420265, 40.688642], [-74.420451, 40.68875], [-74.420879, 40.689295], [-74.420734, 40.690351], [-74.420409, 40.692547], [-74.421532, 40.693394], [-74.423098, 40.694078], [-74.424817, 40.694829], [-74.425, 40.694891], [-74.425734, 40.695657], [-74.428955, 40.698691], [-74.429023, 40.698754]]]}}


    expected_output = {"type": "Feature", "id": "relation/170513", "properties": {"admin_level": "8", "border_type": "borough", "boundary": "administrative", "is_in": "USA, New Jersey", "is_in:country": "USA", "is_in:country_code": "US", "is_in:county": "Union, NJ", "is_in:iso_3166_2": "US:NJ", "is_in:state": "New Jersey", "is_in:state_code": "NJ", "name": "New Providence", "place": "borough", "source": "TIGER/Line\u00ae 2008 Place Shapefiles (http://www.census.gov/geo/www/tiger/)", "tiger:CLASSFP": "C5", "tiger:CPI": "N", "tiger:FUNCSTAT": "A", "tiger:LSAD": "21", "tiger:MTFCC": "G4110", "tiger:NAME": "New Providence", "tiger:NAMELSAD": "New Providence borough", "tiger:PCICBSA": "N", "tiger:PCINECTA": "N", "tiger:PLACEFP": "51810", "tiger:PLACENS": "00885321", "tiger:PLCIDFP": "3451810", "tiger:STATEFP": "34", "type": "boundary", "wikidata": "Q1021568", "wikipedia": "en:New Providence, New Jersey", "id": "relation/170513"}, "geometry": {"type": "Polygon", "coordinates": [[[-74.392757, 40.718046], [-74.392937, 40.718024], [-74.393484, 40.717958], [-74.394151, 40.717582], [-74.394295, 40.717501], [-74.39509, 40.717273], [-74.396013, 40.717261], [-74.396069, 40.717277], [-74.397355, 40.717638], [-74.398248, 40.717851], [-74.398418, 40.717832], [-74.398436, 40.71783], [-74.398443, 40.717829], [-74.398605, 40.717811], [-74.398828, 40.717786], [-74.399268, 40.717738], [-74.399848, 40.717836], [-74.400144, 40.717936], [-74.400275, 40.71798], [-74.400853, 40.718023], [-74.401665, 40.718085], [-74.402254, 40.718001], [-74.40248, 40.717765], [-74.402507, 40.717737], [-74.402514, 40.71773], [-74.402518, 40.717725], [-74.402541, 40.717701], [-74.402633, 40.717605], [-74.402717, 40.717518], [-74.403096, 40.717123], [-74.40375, 40.716023], [-74.404574, 40.715245], [-74.405038, 40.714943], [-74.406126, 40.714498], [-74.406657, 40.714048], [-74.406768, 40.713954], [-74.406918, 40.713827], [-74.406939, 40.713809], [-74.406944, 40.713805], [-74.406948, 40.713801], [-74.406961, 40.71379], [-74.407072, 40.713696], [-74.407089, 40.713682], [-74.407128, 40.713649], [-74.407222, 40.713569], [-74.40724, 40.713554], [-74.407248, 40.713547], [-74.407277, 40.713523], [-74.40735, 40.713461], [-74.407504, 40.713263], [-74.407528, 40.713232], [-74.407698, 40.712599], [-74.407597, 40.711936], [-74.407575, 40.711795], [-74.408078, 40.711198], [-74.408175, 40.710925], [-74.408416, 40.710246], [-74.408448, 40.710156], [-74.408466, 40.710106], [-74.40911, 40.709812], [-74.410057, 40.709517], [-74.410806, 40.709567], [-74.411355, 40.710115], [-74.411847, 40.710345], [-74.412495, 40.7103], [-74.413061, 40.70987], [-74.413392, 40.708966], [-74.413524, 40.70865], [-74.41356, 40.708563], [-74.413614, 40.708434], [-74.413618, 40.708424], [-74.413621, 40.708418], [-74.413629, 40.7084], [-74.413631, 40.708395], [-74.413672, 40.708297], [-74.413702, 40.708225], [-74.413755, 40.708098], [-74.413757, 40.708093], [-74.41376, 40.708087], [-74.413796, 40.708001], [-74.413818, 40.707248], [-74.414453, 40.706579], [-74.4154, 40.705781], [-74.416596, 40.705301], [-74.418196, 40.705301], [-74.418453, 40.705151], [-74.418477, 40.705137], [-74.421796, 40.703201], [-74.422321, 40.703101], [-74.423552, 40.702867], [-74.423896, 40.702801], [-74.423922, 40.702775], [-74.424576, 40.702115], [-74.424733, 40.701957], [-74.425089, 40.701835], [-74.426491, 40.701885], [-74.426897, 40.701711], [-74.427997, 40.700136], [-74.428031, 40.700087], [-74.428038, 40.700077], [-74.428347, 40.699635], [-74.42835, 40.69963], [-74.428357, 40.69962], [-74.428389, 40.699574], [-74.428562, 40.699326], [-74.428707, 40.699119], [-74.428849, 40.698916], [-74.428965, 40.698808], [-74.429023, 40.698754], [-74.428955, 40.698691], [-74.425734, 40.695657], [-74.425, 40.694891], [-74.424817, 40.694829], [-74.423098, 40.694078], [-74.421532, 40.693394], [-74.420409, 40.692547], [-74.420734, 40.690351], [-74.420879, 40.689295], [-74.420451, 40.68875], [-74.420265, 40.688642], [-74.419361, 40.688093], [-74.418795, 40.687449], [-74.418743, 40.687353], [-74.418317, 40.686985], [-74.417912, 40.686506], [-74.41744, 40.686205], [-74.416375, 40.685502], [-74.4157398, 40.6850339], [-74.4155882, 40.6849079], [-74.415031, 40.68442], [-74.4148253, 40.6835857], [-74.414595, 40.6825755], [-74.4141315, 40.6814593], [-74.413728, 40.680719], [-74.413699, 40.680724], [-74.41366, 40.680724], [-74.412931, 40.679469], [-74.411868, 40.680115], [-74.41155, 40.680325], [-74.410653, 40.679228], [-74.405483, 40.682737], [-74.405075, 40.683014], [-74.404477, 40.683213], [-74.4028463, 40.6845451], [-74.401694, 40.6855713], [-74.4010583, 40.6856214], [-74.3994791, 40.6863601], [-74.3991167, 40.6864162], [-74.397127, 40.68702], [-74.3970168, 40.6871477], [-74.396132, 40.688109], [-74.395984, 40.688596], [-74.396499, 40.689896], [-74.395487, 40.690502], [-74.395363, 40.690551], [-74.3927733, 40.6914829], [-74.391946, 40.691692], [-74.38948, 40.69292], [-74.388473, 40.693534], [-74.38788, 40.693874], [-74.387416, 40.694189], [-74.386219, 40.69503], [-74.384907, 40.695634], [-74.384095, 40.696001], [-74.383595, 40.696101], [-74.38399, 40.697281], [-74.384045, 40.697552], [-74.383956, 40.697629], [-74.382638, 40.698807], [-74.382312, 40.699098], [-74.381737, 40.699608], [-74.381568, 40.699719], [-74.3814131, 40.6997804], [-74.3817083, 40.6999716], [-74.38183, 40.7000614], [-74.3819325, 40.7001755], [-74.3819709, 40.7002775], [-74.3819901, 40.7004013], [-74.3819805, 40.7005276], [-74.3819869, 40.7007389], [-74.382035, 40.7009914], [-74.3821406, 40.7014673], [-74.3824455, 40.7022649], [-74.382573, 40.7025381], [-74.3827652, 40.7028028], [-74.3829958, 40.7030845], [-74.3833834, 40.7035798], [-74.3835787, 40.7039003], [-74.3837037, 40.7041965], [-74.3837837, 40.704551], [-74.3840682, 40.7067936], [-74.3842681, 40.7084038], [-74.3843391, 40.7091525], [-74.3844086, 40.709885], [-74.3844474, 40.7102604], [-74.3844996, 40.7104712], [-74.3845518, 40.7106472], [-74.3846073, 40.7108168], [-74.3846341, 40.7108683], [-74.3846681, 40.7109009], [-74.3847415, 40.710966], [-74.3854378, 40.7114944], [-74.386193, 40.712128], [-74.386475, 40.71217], [-74.387157, 40.71229], [-74.388595, 40.713101], [-74.389769, 40.714158], [-74.391604, 40.71581], [-74.391905, 40.716111], [-74.392735, 40.717981], [-74.392757, 40.718046]]]}}

    assert merge.merge_line_string(dirty_input) == expected_output