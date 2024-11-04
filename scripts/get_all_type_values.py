from collections import defaultdict

from app.services.swapi import SwApiService


def get_all_type_values(path):
    swapi_service = SwApiService()

    data = swapi_service.get(path)
    types = {k: set() for k, v in data[0].items()}
    not_typeable = defaultdict(list)

    for key in data[0].keys():
        for data_dto in data:
            if not isinstance(data_dto[key], list):
                types[key].add(data_dto[key])
            else:
                not_typeable[key] = data_dto[key]

    return types, not_typeable


if __name__ == '__main__':
    unic_values, err = get_all_type_values('/people')
    t = [item for item in unic_values.items()]
    print(t)
