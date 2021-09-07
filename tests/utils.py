#
# Copyright (C) 2021 Supercomputing Systems AG
# This file is part of smartmeter-datacollector.
#
# SPDX-License-Identifier: GPL-2.0-only
# See LICENSES/README.md for more information.
#
from typing import List

import pytest

from smartmeter_datacollector.smartmeter.cosem import CosemConfig, RegisterCosem
from smartmeter_datacollector.smartmeter.meter_data import MeterDataPointTypes


@pytest.fixture
def cosem_config_lg() -> CosemConfig:
    obis_registers = [
        RegisterCosem("1.0.1.7.0.255", MeterDataPointTypes.ACTIVE_POWER_P.value),
        RegisterCosem("1.0.2.7.0.255", MeterDataPointTypes.ACTIVE_POWER_N.value),
    ]
    return CosemConfig(
        id_obis="0.0.42.0.0.255",
        clock_obis="0.0.1.0.0.255",
        register_obis=obis_registers
    )


@pytest.fixture
def unencrypted_valid_data_lg() -> List[bytes]:
    data_str: List[str] = []
    data_str.append("7E A0 84 CE FF 03 13 12 8B E6 E7 00 E0 40 00 01 00 00 70 0F 00 00 CB C2 0C 07 E5 07 06 02 0E 3A 05 FF 80 00 00 02 10 01 10 02 04 12 00 28 09 06 00 08 19 09 00 FF 0F 02 12 00 00 02 04 12 00 28 09 06 00 08 19 09 00 FF 0F 01 12 00 00 02 04 12 00 01 09 06 00 00 2A 00 00 FF 0F 02 12 00 00 02 04 12 00 01 09 06 00 00 60 01 01 FF 0F 02 12 00 00 02 04 12 00 08 09 06 00 00 01 00 00 FF 0F 02 12 00 00 77 C8 7E")
    data_str.append("7E A0 7D CE FF 03 13 D0 45 E0 40 00 02 00 00 6C 02 04 12 00 03 09 06 01 00 01 07 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 00 02 07 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 00 03 07 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 00 04 07 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 01 01 08 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 01 02 08 00 FF 0F 02 12 00 00 B3 98 7E")
    data_str.append("7E A0 84 CE FF 03 13 12 8B E6 E7 00 E0 40 00 01 00 00 70 0F 00 00 CB C6 0C 07 E5 07 06 02 0E 3A 10 FF 80 00 00 02 10 01 10 02 04 12 00 28 09 06 00 08 19 09 00 FF 0F 02 12 00 00 02 04 12 00 28 09 06 00 08 19 09 00 FF 0F 01 12 00 00 02 04 12 00 01 09 06 00 00 2A 00 00 FF 0F 02 12 00 00 02 04 12 00 01 09 06 00 00 60 01 01 FF 0F 02 12 00 00 02 04 12 00 08 09 06 00 00 01 00 00 FF 0F 02 12 00 00 27 73 7E")
    data_str.append("7E A0 7D CE FF 03 13 D0 45 E0 40 00 02 00 00 6C 02 04 12 00 03 09 06 01 00 01 07 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 00 02 07 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 00 03 07 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 00 04 07 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 01 01 08 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 01 02 08 00 FF 0F 02 12 00 00 B3 98 7E")
    data_str.append("7E A0 8B CE FF 03 13 EE E1 E0 40 00 03 00 00 7A 02 04 12 00 03 09 06 01 01 05 08 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 01 06 08 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 01 07 08 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 01 08 08 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 00 0D 07 00 FF 0F 02 12 00 00 09 06 00 08 19 09 00 FF 09 10 4C 47 5A 31 30 33 30 36 35 35 39 33 33 35 31 32 09 07 31 39 33 35 3B 2A 7E")
    data_str.append("7E A0 57 CE FF 03 13 E9 69 E0 C0 00 04 00 00 46 39 31 32 09 0C 07 E5 07 06 02 0E 3A 12 FF 80 00 81 06 00 00 00 1C 06 00 00 00 00 06 00 00 00 00 06 00 00 00 0A 06 00 0D 88 C1 06 00 00 00 00 06 00 00 00 12 06 00 00 00 01 06 00 00 00 00 06 00 04 72 0D 12 03 AD C2 CE 7E")
    data = list(map(lambda frag: bytes.fromhex(frag.replace(" ", "")), data_str))
    return data


@pytest.fixture
def unencrypted_invalid_data_lg() -> List[bytes]:
    data_str: List[str] = []
    data_str.append("7E A0 84 CE FF 03 13 12 8B E6 E7 00 E0 40 00 01 00 00 70 0F 00 00 C9 60 0C 07 E5 07 06 02 0E 07 37 FF 80 00 00 02 10 01 10 02 04 12 00 28 09 06 00 08 19 09 00 FF 0F 02 12 00 00 02 04 12 00 28 09 06 00 08 19 09 00 FF 0F 01 12 00 00 02 04 12 00 01 09 06 00 00 2A 00 00 FF 0F 02 12 00 00 02 04 12 00 01 09 06 00 00 60 01 01 FF 0F 02 12 00 00 02 04 12 00 08 09 06 00 00 01 00 00 FF 0F 02 12 00 00 35 37 7E")
    data_str.append("7E A0 7D CE FF 03 13 D0 45 E0 40 00 02 00 00 6C 02 04 12 00 03 09 06 01 00 01 07 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 00 02 07 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 00 03 07 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 00 04 07 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 01 01 08 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 01 02 08 00 FF 0F 02 12 00 00 B3 98 7E")
    data_str.append("7E A0 7D CE FF 03 13 D0 45 E0 40 00 02 00 00 6C 02 04 12 00 03 09 06 01 00 01 07 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 00 02 07 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 00 03 07 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 00 04 07 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 01 01 08 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 01 02 08 00 FF 0F 02 12 00 00 B3 98 7E")
    data_str.append("7E A0 8B CE FF 03 13 EE E1 E0 40 00 03 00 00 7A 02 04 12 00 03 09 06 01 01 05 08 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 01 06 08 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 01 07 08 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 01 08 08 00 FF 0F 02 12 00 00 02 04 12 00 03 09 06 01 00 0D 07 00 FF 0F 02 12 00 00 09 06 00 08 19 09 00 FF 09 10 4C 47 5A 31 30 33 30 36 35 35 39 33 33 35 31 32 09 07 31 39 33 35 3B 2A 7E")
    data_str.append("7E A0 57 CE FF 03 13 E9 69 E0 C0 00 04 00 00 46 39 31 32 09 0C 07 E5 07 06 02 0E 08 13 FF 80 00 81 06 00 00 00 00 06 00 00 00 00 06 00 00 00 00 06 00 00 00 00 06 00 0D 88 C1 06 00 00 00 00 06 00 00 00 12 06 00 00 00 01 06 00 00 00 00 06 00 04 72 0D 12 03 E8 AD 29 7E")
    data = list(map(lambda frag: bytes.fromhex(frag.replace(" ", "")), data_str))
    return data
