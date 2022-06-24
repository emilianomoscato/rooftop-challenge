from copy import deepcopy


def get_test_cases():
    TESTING_DATA = [
        {
            "email": "emiliano.moscato@gmail.com",
            "token": "emiliano.moscato",
            "blocks": ["abcdefghijklmnopqrstuvwxyz"],
            "sorted": ["abcdefghijklmnopqrstuvwxyz"]
        },
        {
            "email": "user@prueba.com",
            "token": "user",
            "blocks": ["abcdefghijklmnopqrstuvwxyz", "12345678901234567890123456",
                       "1234567890abcdefghijklmnop"],
            "sorted": ["abcdefghijklmnopqrstuvwxyz", "1234567890abcdefghijklmnop",
                       "12345678901234567890123456"]
        },
        {
            "email": "user1@prueba.com",
            "token": "user1",
            "blocks": ["abcdefghijklmnopqrstuvwxyz", "12345678901234567890123456"],
            "sorted": ["abcdefghijklmnopqrstuvwxyz", "12345678901234567890123456"]
        },
        {
            "email": "user2@prueba.com",
            "token": "user2",
            "blocks": [
                'oT365hrMf8rDZiJEAd9DPAi5yJKLWKI7gOzGNFq2L0NuZo4r6PQKPoCDrTyxPzgoZ1Rg34pAjX3pd5pdpHlxMoscgeExQGSLjpo8',
                'aBViyEyi1GulTDBqvT7rMPx85R0p6zE2tiYSf2YdB6BE4jL554KtCVLoDmGjH6IRkpIKu2FKkMAKA5mxojfRduOGBHvggSURu44B',
                '3IVDaw1SlA7BPZlekEcGbcR7np1XUbcb0DG5TzxL51DiKNP4kXvIyr4u4zXCtXSsxdcmiyWr0IIUrjFUH77weiqu7r410XdUsIuW',
                'bPlHgdZRmw5Ur2sMReqWJIJLWOHMgfHxwHeGbnRrfCEmseyNL97wlpwdjxwFi1AyMFTMgLifrHvPMb38PYhdnt5OY8Z5rvyl3mEZ',
                'ZFOzIq1rILXqEY3PS0u7aJkHIu3bR1DBpQC6bVoOwu3pAxoquEOTck7vAlU279n9DkzAXvvYMsNPZ8JacTIIPVzUtPqZXX9GI4e9',
                '6gJwjQioFGHqEdizPNE5ybVakFQ0dcvMdFsrgl7NSLHXSVsEHq25q4XGUSUwGnECx0UIowjHnKcSv8FM4clWgGuakFUp0IOPuu3B',
                'MomVIWVUxHcW8MCslR1wzVgPqv5nxpqnsMIvmHI1WXphd7xjtRedEr7ItaGNOJDiSnLsC7mVfrBdHCl2VyX3uDrueUk51KreFdeN',
                'mXCMzRCr0Q4YmQmAW0A46pl1yCcTiI89HmO7IGBnOds1v6h6ZySkN7MCfEeswQdyPoQ3RLyvP3KAQ2k1ixTreimBhnoIiYJdqszl',
                'TTnW5d3MVQY8SfQcPjIphzVsaiCKoWPGr6LyNhEnDJ6jOLtB7dacJJpEyAziSDbdX8Qxzhtvo8HERfxGiT1SU3fnPs2YQNHrAkj5'
            ],
            "sorted": [
                'oT365hrMf8rDZiJEAd9DPAi5yJKLWKI7gOzGNFq2L0NuZo4r6PQKPoCDrTyxPzgoZ1Rg34pAjX3pd5pdpHlxMoscgeExQGSLjpo8',
                'MomVIWVUxHcW8MCslR1wzVgPqv5nxpqnsMIvmHI1WXphd7xjtRedEr7ItaGNOJDiSnLsC7mVfrBdHCl2VyX3uDrueUk51KreFdeN',
                'TTnW5d3MVQY8SfQcPjIphzVsaiCKoWPGr6LyNhEnDJ6jOLtB7dacJJpEyAziSDbdX8Qxzhtvo8HERfxGiT1SU3fnPs2YQNHrAkj5',
                '3IVDaw1SlA7BPZlekEcGbcR7np1XUbcb0DG5TzxL51DiKNP4kXvIyr4u4zXCtXSsxdcmiyWr0IIUrjFUH77weiqu7r410XdUsIuW',
                'mXCMzRCr0Q4YmQmAW0A46pl1yCcTiI89HmO7IGBnOds1v6h6ZySkN7MCfEeswQdyPoQ3RLyvP3KAQ2k1ixTreimBhnoIiYJdqszl',
                'ZFOzIq1rILXqEY3PS0u7aJkHIu3bR1DBpQC6bVoOwu3pAxoquEOTck7vAlU279n9DkzAXvvYMsNPZ8JacTIIPVzUtPqZXX9GI4e9',
                'bPlHgdZRmw5Ur2sMReqWJIJLWOHMgfHxwHeGbnRrfCEmseyNL97wlpwdjxwFi1AyMFTMgLifrHvPMb38PYhdnt5OY8Z5rvyl3mEZ',
                'aBViyEyi1GulTDBqvT7rMPx85R0p6zE2tiYSf2YdB6BE4jL554KtCVLoDmGjH6IRkpIKu2FKkMAKA5mxojfRduOGBHvggSURu44B',
                '6gJwjQioFGHqEdizPNE5ybVakFQ0dcvMdFsrgl7NSLHXSVsEHq25q4XGUSUwGnECx0UIowjHnKcSv8FM4clWgGuakFUp0IOPuu3B'
            ]
        },
        {
            "email": "user3@prueba.com",
            "token": "user3",
            "blocks": [
                'oT365hrMf8rDZiJEAd9DPAi5yJKLWKI7gOzGNFq2L0NuZo4r6PQKPoCDrTyxPzgoZ1Rg34pAjX3pd5pdpHlxMoscgeExQGSLjpo8',
                'aBViyEyi1GulTDBqvT7rMPx85R0p6zE2tiYSf2YdB6BE4jL554KtCVLoDmGjH6IRkpIKu2FKkMAKA5mxojfRduOGBHvggSURu44B',
            ],
            "sorted": [
                'oT365hrMf8rDZiJEAd9DPAi5yJKLWKI7gOzGNFq2L0NuZo4r6PQKPoCDrTyxPzgoZ1Rg34pAjX3pd5pdpHlxMoscgeExQGSLjpo8',
                'aBViyEyi1GulTDBqvT7rMPx85R0p6zE2tiYSf2YdB6BE4jL554KtCVLoDmGjH6IRkpIKu2FKkMAKA5mxojfRduOGBHvggSURu44B',
            ]
        }
    ]
    return deepcopy(TESTING_DATA)
