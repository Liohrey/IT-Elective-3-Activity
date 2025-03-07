from django.http import JsonResponse, Http404, HttpResponseNotAllowed
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

# In-memory storage for items
items_list = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 699.99},
    {"id": 3, "name": "Headphones", "price": 149.99},
]

# Helper function to find an item by ID
def get_item_by_id(item_id):
    for item in items_list:
        if item["id"] == item_id:
            return item
    return None

# Class-based view for handling multiple items
@method_decorator(csrf_exempt, name='dispatch')
class ItemsListView(View):
    def get(self, request):
        # Handle search query parameter
        search_query = request.GET.get('search', '')
        if search_query:
            filtered_items = [item for item in items_list if search_query.lower() in item['name'].lower()]
            return JsonResponse({"items": filtered_items})
        
        # Return all items if no search parameter
        return JsonResponse({"items": items_list})
    
    def post(self, request):
        try:
            # Try to parse JSON data
            data = json.loads(request.body)
        except json.JSONDecodeError:
            # If not JSON, try form data
            data = request.POST.dict()
        
        # Validate required fields
        if 'name' not in data or 'price' not in data:
            return JsonResponse({"error": "Name and price are required"}, status=400)
        
        # Generate a new ID (simple approach)
        new_id = max([item["id"] for item in items_list], default=0) + 1
        
        # Create new item
        new_item = {
            "id": new_id,
            "name": data["name"],
            "price": float(data["price"])
        }
        
        # Add to list
        items_list.append(new_item)
        
        return JsonResponse({"message": "Item added successfully", "item": new_item}, status=201)

# Class-based view for handling a single item
@method_decorator(csrf_exempt, name='dispatch')
class ItemDetailView(View):
    def get(self, request, item_id):
        item = get_item_by_id(item_id)
        if not item:
            raise Http404("Item not found")
        
        return JsonResponse({"item": item})
    
    def put(self, request, item_id):
        item = get_item_by_id(item_id)
        if not item:
            raise Http404("Item not found")
        
        try:
            # Try to parse JSON data
            data = json.loads(request.body)
        except json.JSONDecodeError:
            # If not JSON, try form data
            data = request.POST.dict()
        
        # Update item fields if provided
        if 'name' in data:
            item['name'] = data['name']
        if 'price' in data:
            item['price'] = float(data['price'])
        
        return JsonResponse({"message": "Item updated successfully", "item": item})
    
    def delete(self, request, item_id):
        item = get_item_by_id(item_id)
        if not item:
            raise Http404("Item not found")
        
        # Remove item from list
        items_list.remove(item)
        
        return JsonResponse({"message": "Item deleted successfully"}) 