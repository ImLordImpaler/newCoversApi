from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from basic.models import Question , SubQuestion , Cover
from rest_framework.status import HTTP_200_OK , HTTP_400_BAD_REQUEST
import json
class Index(ListAPIView):
    def list(self , request ):
        try:
            d = request.query_params.dict()
            kwargs = {}
            cover_type = d.get('cover_type', None)
            if cover_type is not None:
                kwargs['cover_type'] = cover_type

            vehicle_type = d.get('vehicle_type' , None)
            if vehicle_type is not None:
                kwargs['vehicle_type__name__in'] = [vehicle_type]

            policy_type = d.get('policy_type' , None)
            if policy_type is not None:
                kwargs['policy_type__name__in'] = [policy_type]

            fuel_type = d.get('fuel_type', None )
            if fuel_type is not None:
                kwargs['fuel_type__name__in'] = [fuel_type]

            owner_type = d.get('individual', None)
            if owner_type is not None:
                kwargs['owner_type__name__in'] = [owner_type]

            print("Kwargs: ", kwargs)
            queryset = Cover.objects.filter(**kwargs).values( 'description','name','code','value','value_type','plan_type')

            res = {
                'lb':[],
                'od':[],
                'addon':[],
                'dis':[]
            }
            print('\n')
            print(queryset)
            for i in queryset:
                if i.get('value_type') == 'text':
                    cover_data = i.get('value').split(',')
                    min_value = int(cover_data[0])
                    max_value = int(cover_data[1])
                    dropdown = None

                elif i.get('value_type') == 'dropdown':
                    min_value = None
                    max_value = None
                    cover_data = i.get('value').split(',')
                    cover_data.sort()
                    dropdown = {}
                    for cover in cover_data:
                        dropdown[int(cover)] = int(cover)
                elif i.get('value_type') == "radio":
                    cover_data = i.get('value').split(',')
                    cover_name = i.get('name')
                    cover_name = cover_name.split('/')
                    cover_data.sort()
                    min_value = int(cover_data[0])
                    max_value = int(cover_data[1])
                    radio_group_list = []
                    for cov_name in cover_name:
                        radio_group = {
                            "name": cov_name.split(" ")[0],
                            "min": min_value,
                            "max": max_value,
                            "code": i.get('code')
                        }
                        radio_group_list.append(radio_group)
                else:
                    min_value = None
                    max_value = None
                    dropdown = None

                if i.get('value_type') !='radio':
                    temp = {
                        'name': i.get('name'),
                        'code': i.get('code'),
                        'description': i.get('description'),
                        'cover_type': i.get('value_type'),
                        'min': min_value,
                        'max': max_value,
                        'dropdown': dropdown
                    }
                else:
                    temp = {
                        'name': i.get('name'),
                        'code': i.get('code'),
                        'description':i.get('description'),
                        'cover_type': i.get('value_type').lower(),
                        "radio_group": radio_group_list
                    }

                if i.get('plan_type') == 'Own_Damage':
                    res['od'].append(temp)
                elif i.get('plan_type') == 'Liability':
                    res['lb'].append(temp)
                elif i.get('plan_type') == 'Addon':
                    res['addon'].append(temp)
                elif i.get('plan_type') == 'Discounts':
                    res['dis'].append(temp)
                else:
                    pass

            return HTTP_200_OK, "Success", res
        except Exception as R:

            return HTTP_400_BAD_REQUEST, "Something went wrong", [str(R)]
