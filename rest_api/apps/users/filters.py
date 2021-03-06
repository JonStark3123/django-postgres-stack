# -*- coding: utf-8 -*-
import django_filters
from django.db.models import Q

from machines.models import Machine
from records.models import TestRecord

class UserMachineListFilter(django_filters.rest_framework.FilterSet):
	"""
	UserMachineListFilter
	"""

	class Meta:
		model = Machine
		fields = ['owner_username', ]


class MachineRecordListFilter(django_filters.rest_framework.FilterSet):
	"""
	TestRecordListFilter
	"""
	branch__id = django_filters.NumberFilter()
	test_machine__machine_sn = django_filters.CharFilter()

	class Meta:
		model = TestRecord
		fields = ['branch__id', 'test_machine__sn']