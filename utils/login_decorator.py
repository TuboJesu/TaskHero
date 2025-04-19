from functools import wraps

from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse

from task_manager.models import Task

def custom_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, "You need to log in to access this page.")
            return redirect('users:log_in') 
        return view_func(request, *args, **kwargs)
    return wrapper

# def user_is_review_owner(action):
#     """Decorator to check if the logged-in user is the owner of the review."""
#     def decorator(view_func):
#         @wraps(view_func)
#         def wrapper(request, review_id, *args, **kwargs):
#             review = get_object_or_404(Task, pk=review_id)
#             if request.user != review.added_by:
#                 messages.error(request, f"You cannot {action} this review.")
#                 return redirect(reverse('review:book_detail', kwargs={"book_id": review.book.id}))
#             return view_func(request,  review_id, *args, **kwargs)
#         return wrapper
#     return decorator