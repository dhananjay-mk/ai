import matplotlib.pyplot as plt

fig = plt.figure()
plt.plot([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000], [-5.747698485092027, -11.942418733221691, -27.93732527108281, -43.96068471850883, -59.416571073131415, -71.63120624510276, -83.24803404718038, -96.81489228190189, -109.74124525007339, -120.99340040661272, -134.39603284867167, -148.13605583400397, -161.1597779442585, -178.78814755740603, -188.48238876057354, -205.63944889729785, -216.80464215893625, -233.1448496437426, -248.4984074212203, -257.2465934232047, -272.35614737568176, -286.3425897045494, -301.81181368252106, -310.1461403081171, -327.0199074320692, -341.05902472291535, -358.49475453097375, -370.9759038371258, -382.9023326403819, -398.8071256174506, -409.538041188465, -425.29755691330854, -437.06440561601016, -451.78025925567255, -464.07393563426245, -477.17253268063104, -491.22023757346693, -503.4887611346097, -516.3453040193567, -532.4854333927416, -545.3579444531476, -558.889445445853, -571.6785872932461, -586.132196473544, -598.6067783911336, -611.7717400539132, -626.1329923631807, -640.1575679616498, -652.9743145167308, -665.5310681378141, -679.8684122852225, -689.523075274551, -705.0958927377105, -715.1537346393261, -730.6791709114289, -746.1335105634535, -758.8568872077548, -773.8849830276798, -782.8882628759574, -795.8359310515056, -810.1169189199345, -822.1616519780796, -837.2924543743775, -850.5957888873467, -864.1418000933438, -876.3069879598397, -889.5593690529922, -901.6148253016923, -915.0922210714579, -926.6971382748969, -940.2653563818051, -952.5625461907575, -965.7808003904227, -979.8054222072928, -992.0785925696315, -1007.1659222959074, -1019.7748805717122, -1034.8415536874973, -1048.8491530243896, -1062.4014187227508, -1075.5920436550653, -1090.781003012027, -1104.0604944155637, -1116.9666750483136, -1131.146527593961, -1145.5576837969902, -1157.5183632514656, -1168.9784020419784, -1183.3212225184036, -1198.7268080385036, -1212.9956121765604, -1226.352341783609, -1239.296895565363, -1252.6919273275707, -1267.7616012014942, -1281.0315698796624, -1295.450002015856, -1307.2701779625693, -1320.0659608852523, -1332.6480892691998]) #Plot X
plt.plot([], 'ro')
fig.suptitle('Last Log Prob vs Number of Observations', fontsize=20)
plt.ylabel('Last Log Prob')
plt.xlabel('Number of Observations')
plt.show()

fig = plt.figure()
plt.plot([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000], [12.0, 11.0, 21.0, 21.0, 19.0, 27.0, 42.0, 26.0, 38.0, 76.0, 39.0, 28.0, 80.0, 36.0, 68.0, 39.0, 66.0, 55.0, 86.0, 98.0, 78.0, 75.0, 94.0, 170.0, 98.0, 140.0, 93.0, 88.0, 97.0, 86.0, 187.0, 77.0, 88.0, 111.0, 110.0, 86.0, 89.0, 186.0, 160.0, 157.0, 111.0, 145.0, 151.0, 132.0, 134.0, 165.0, 182.0, 113.0, 105.0, 120.0, 146.0, 216.0, 176.0, 292.0, 274.0, 174.0, 221.0, 172.0, 150.0, 169.0, 148.0, 153.0, 178.0, 153.0, 156.0, 185.0, 161.0, 208.0, 136.0, 141.0, 177.0, 136.0, 205.0, 157.0, 220.0, 142.0, 137.0, 134.0, 132.0, 156.0, 141.0, 140.0, 132.0, 147.0, 109.0, 109.0, 106.0, 111.0, 119.0, 119.0, 127.0, 134.0, 138.0, 134.0, 133.0, 144.0, 155.0, 238.0, 216.0, 357.0])
plt.plot([], 'ro')
fig.suptitle('Number of Iterations vs Number of Observations', fontsize=20)
plt.ylabel('Number of Iterations')
plt.xlabel('Number of Observations')
plt.show()


fig = plt.figure()
plt.plot([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000], [0.5642175945778704, 0.5498396253035319, 0.3326928024999482, 0.21379386810240475, 0.1496569957261469, 0.1364633253574373, 0.1290082294300892, 0.11968426761439184, 0.10621925500962029, 0.11472905755777495, 0.09803805423004969, 0.08646216886930781, 0.07839672739311555, 0.05816100399010859, 0.0702491313612484, 0.052850912640315495, 0.05205605487617238, 0.04134253532697155, 0.033575543018071904, 0.04575731154918376, 0.03633531724125712, 0.029679661506580173, 0.023342702177906002, 0.03621285661532109, 0.025239864921943182, 0.025595252213068142, 0.01954713211086028, 0.02299611566942341, 0.026310225698765847, 0.0231290161555108, 0.02721707409804348, 0.023436822934176794, 0.025496939078287442, 0.023175161191176043, 0.02258780652580944, 0.0186187662385201, 0.011573767968698717, 0.015712763608896372, 0.014875261848524684, 0.0117909795970061, 0.01040776206959008, 0.010962619179321358, 0.012203797557305664, 0.009018741439019165, 0.011087420233557422, 0.010103165241547028, 0.010260738519015109, 0.008537030739618966, 0.010672148317918372, 0.012459037410021455, 0.01103074208972586, 0.010891576442655931, 0.008252295520537148, 0.014173708758775865, 0.01110219535456289, 0.009190167196125943, 0.010346894837859848, 0.009818990104279411, 0.012493906368089324, 0.013277637082668799, 0.012468278847041112, 0.012241931765673076, 0.010843325973437477, 0.010736154847717713, 0.010114168194591563, 0.009579418004046615, 0.009942061665949976, 0.01090496291782558, 0.010095597564495039, 0.011027862209600763, 0.01093555758574614, 0.01154661140653652, 0.011413512346113949, 0.010720261331925652, 0.012040205782737068, 0.010451495622158137, 0.010420743311678997, 0.008733405835085467, 0.00874972333060147, 0.0087146921642068, 0.008778634594622034, 0.007979452698783508, 0.00760771626954805, 0.00799013633468373, 0.007436656904427451, 0.0073913184731594795, 0.00729618802434776, 0.006927444011208283, 0.006667450910590285, 0.006784258429219144, 0.006994538272274016, 0.006871674690346815, 0.006817573215446584, 0.007263823567039743, 0.006638815759647116, 0.006559810274978965, 0.005941636693093642, 0.00705323675498832, 0.0067578149222978015, 0.00765640135142098])
plt.plot([], 'ro')
fig.suptitle('Relative Log Probability Error vs Number of Observations', fontsize=20)
plt.ylabel('Relative Log Probability Error')
plt.xlabel('Number of Observations')
plt.show()