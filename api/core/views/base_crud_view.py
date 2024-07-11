# .\api\core\views\base_crud_view.py
from typing import Optional

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from api.core.services.base_service import BaseService
from resources.utils.filter_util import FilterUtil


class BaseCRUDView(viewsets.ViewSet):
    """Base CRUD API View"""

    srv_class: Optional[BaseService] = None
    serial_class: Optional[ModelSerializer] = None

    def list(self, request, *args, **kwargs):
        """List all items"""
        data = request.GET.dict()
        filters = FilterUtil.get_list_filters(data=data)
        items = self.srv_class.get_all(**filters)
        serializer = self.serial_class(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """Create a new item"""
        serializer = self.serial_class(data=request.data)
        if serializer.is_valid():
            item = serializer.save()
            if hasattr(self.srv_class, "set_translation_keys"):
                self.srv_class.set_translation_keys(instance=item, keys=["translation_key"])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, id: int, *args, **kwargs):
        """Retrieve a specific item by ID"""
        if item := self.srv_class.get_one(id=id):
            serializer = self.serial_class(item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, id: int, *args, **kwargs):
        """Update a specific item by ID"""
        item = self.srv_class.get_one(id=id)
        if not item:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        serializer = self.serial_class(item, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, id: int, *args, **kwargs):
        """Delete a specific item by ID"""
        if self.srv_class.delete(id=id):
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def update_files(self, request, id: int, *args, **kwargs):
        """Update files for a specific item by ID"""
        if not hasattr(self.srv_class, "update_files"):
            return Response(
                {"detail": "update_files method not implemented in service"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        files = request.FILES
        if item := self.srv_class.update_files(files=files, id=id):
            serializer = self.serial_class(item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({}, status=status.HTTP_404_NOT_FOUND)
