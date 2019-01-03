from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
	message="Only the Owner can access this page"

	def has_object_permission(self, request, view, obj):
		if obj.owner == request.user:
			return True
		else: 
			return False
