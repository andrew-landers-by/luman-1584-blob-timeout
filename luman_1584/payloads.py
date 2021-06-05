"""
This module provides some predefined payloads for the
Ocean PTA service. This can be extended as needed
to investigate the performance of blob downloads.
"""

class Payloads:

    class Keys:
        TRANSACTION_ID = "transactionId"
        LATITUDE = "latitude"
        LONGITUDE = "longitude"
        VESSEL_NAME = "vesselName"
        DEPARTURE_PORT = "actualDeparturePort"
        ARRIVAL_PORT = "actualArrivalPort"
        DEPARTURE_TIME = "departTimeAtDeparturePort"
        TIMESTAMP = "timestamp"

    SINGLE_INPUT = {
        "transactionId": "xyzzy-12300",
        "latitude": 33.05814,
        "longitude": -78.03655,
        "vesselName": "maersk utah",
        "actualDeparturePort": "ussav",
        "actualArrivalPort": "beanr",
        "departTimeAtDeparturePort": "2021-09-21 09:15:00+00:00",
        "timestamp": "2021-09-21 09:29:08+0000"
    }
    BATCH_INPUT = [
        {
            "timestamp": "2021-01-26 21:56:34+00:00",
            "latitude": 1.33375,
            "longitude": 103.5558,
            "vesselName": "MURCIA MAERSK 101W",
            "actualDeparturePort": "CNNGB",
            "actualArrivalPort": "SEGOT",
            "departTimeAtDeparturePort": "2021-01-20 06:45:00+00:00"
        },
        {
            "timestamp": "2021-01-16 04:57:07+00:00",
            "latitude": 30.63035,
            "longitude": 122.0496,
            "vesselName": "CMA CGM JEAN MERMOZ",
            "actualDeparturePort": "CNNGB",
            "actualArrivalPort": "FRLEH",
            "departTimeAtDeparturePort": "2021-01-15 04:58:00+00:00"
        },
        {
            "timestamp": "2021-01-25 14:56:17+00:00",
            "latitude": 25.14243,
            "longitude": 121.7558,
            "imo": -1,
            "vesselName": "PHILIPPOS-MICHALIS",
            "actualDeparturePort": "CNSZX",
            "actualArrivalPort": "TWKEL",
            "departTimeAtDeparturePort": "2021-01-22 09:04:42+00:00"
        },
        {
            "timestamp": "2021-01-10 22:56:45+00:00",
            "latitude": 31.94373,
            "longitude": 31.68317,
            "vesselName": "MSC LARA",
            "actualDeparturePort": "CNNGB",
            "actualArrivalPort": "UAODS",
            "departTimeAtDeparturePort": "2021-01-11 22:15:09+00:00"
        },
        {
            "timestamp": "2021-02-14 18:52:42+00:00",
            "latitude": 35.8949,
            "longitude": -5.492232,
            "imo": -1,
            "vesselName": "APL LION CITY 0FM69W1MA",
            "actualDeparturePort": "CNNGB",
            "actualArrivalPort": "NLRTM",
            "departTimeAtDeparturePort": "2021-01-15 03:04:00+00:00"
        },
        {
            "timestamp": "2021-01-27 00:57:29+00:00",
            "latitude": 22.63794,
            "longitude": 113.6839,
            "imo": -1,
            "vesselName": "EDITH MAERSK 103W",
            "actualDeparturePort": "CNNGB",
            "actualArrivalPort": "DEHAM",
            "departTimeAtDeparturePort": "2021-01-20 12:15:00+00:00"
        },
        {
            "timestamp": "2021-01-19 04:57:57+00:00",
            "latitude": 32.81947,
            "longitude": 35.01287,
            "imo": -1,
            "vesselName": "MAERSK HAVANA 050W",
            "actualDeparturePort": "CNNGB",
            "actualArrivalPort": "ITTRS",
            "departTimeAtDeparturePort": "2020-12-22 05:00:00+00:00"
        },
        {
            "timestamp": "2021-01-20 11:55:45+00:00",
            "latitude": 31.34035,
            "longitude": 121.6522,
            "imo": -1,
            "vesselName": "KUO CHANG",
            "actualDeparturePort": "CNNGB",
            "actualArrivalPort": "TWKEL",
            "departTimeAtDeparturePort": "2021-01-18 14:00:00+00:00"
        },
        {
            "timestamp": "2021-01-12 03:57:49+00:00",
            "latitude": 1.333633,
            "longitude": 103.5558,
            "imo": -1,
            "vesselName": "MOSCOW MAERSK 053W",
            "actualDeparturePort": "CNNGB",
            "actualArrivalPort": "NLRTM",
            "departTimeAtDeparturePort": "2021-01-05 08:22:58+00:00"
        },
        {
            "timestamp": "2021-02-02 22:53:22+00:00",
            "latitude": 1.277382,
            "longitude": 103.7549,
            "imo": -1,
            "vesselName": "MSC SIXIN 101W",
            "actualDeparturePort": "CNZSN",
            "actualArrivalPort": "ESVLC",
            "departTimeAtDeparturePort": "2021-01-25 13:21:34+00:00"
        },
        {
            "timestamp": "2021-02-08 08:53:13+00:00",
            "latitude": 22.57246,
            "longitude": 114.2841,
            "imo": -1,
            "vesselName": "EVER GIFTED 0LA8BW1MA",
            "actualDeparturePort": "CNNGB",
            "actualArrivalPort": "NLRTM",
            "departTimeAtDeparturePort": "2021-02-01 13:26:00+00:00"
        },
        {
            "timestamp": "2021-02-14 06:55:28+00:00",
            "latitude": 51.95787,
            "longitude": 4.04065,
            "imo": -1,
            "vesselName": "MAERSK MC-KINNEY MOLLER 053W",
            "actualDeparturePort": "CNNGB",
            "actualArrivalPort": "NLRTM",
            "departTimeAtDeparturePort": "2021-01-15 12:00:00+00:00"
        },
        {
            "timestamp": "2021-02-05 07:55:33+00:00",
            "latitude": -32.12494,
            "longitude": -52.10221,
            "imo": -1,
            "vesselName": "ANTOFAGASTA EXPRESS",
            "actualDeparturePort": "BRSSZ",
            "actualArrivalPort": "CLSAI",
            "departTimeAtDeparturePort": "2021-02-02 02:18:00+00:00"
        },
        {
            "timestamp": "2021-02-01 00:56:08+00:00",
            "latitude": 1.26453,
            "longitude": 103.7813,
            "imo": -1,
            "vesselName": "COSCO SHIPPING TAURUS \/ 015W",
            "actualDeparturePort": "CNNGB",
            "actualArrivalPort": "DEHAM",
            "departTimeAtDeparturePort": "2021-01-27 09:27:00+00:00"
        },
        {
            "timestamp": "2021-02-04 03:57:35+00:00",
            "latitude": 36.88589,
            "longitude": -9.289742,
            "imo": -1,
            "vesselName": "COSCO SHIPPING ARIES \/ 015W",
            "actualDeparturePort": "CNNGB",
            "actualArrivalPort": "NLRTM",
            "departTimeAtDeparturePort": "2021-01-06 13:25:00+00:00"
        },
        {
            "timestamp": "2021-01-28 17:01:58+00:00",
            "latitude": 22.57326,
            "longitude": 113.4787,
            "imo": -1,
            "vesselName": "ZHONG HANG 936",
            "actualDeparturePort": "CNZSN",
            "actualArrivalPort": "KRPUS",
            "departTimeAtDeparturePort": "2021-01-11 23:59:00+00:00"
        },
        {
            "timestamp": "2021-01-12 13:55:39+00:00",
            "latitude": 1.333617,
            "longitude": 103.5559,
            "imo": -1,
            "vesselName": "MOSCOW MAERSK 053W",
            "actualDeparturePort": "CNNGB",
            "actualArrivalPort": "NLRTM",
            "departTimeAtDeparturePort": "2021-01-05 08:22:58+00:00"
        },
        {
            "timestamp": "2021-01-19 18:57:46+00:00",
            "latitude": 1.333655,
            "longitude": 103.5558,
            "imo": -1,
            "vesselName": "MSC BARI 101W",
            "actualDeparturePort": "CNSHG",
            "actualArrivalPort": "NLRTM",
            "departTimeAtDeparturePort": "2021-01-08 21:51:00+00:00"
        }
    ]
