from django.shortcuts import render,redirect
from random import choice
import markdown2

from .util import get_entry,list_entries, save_entry


def index(request): 
    """
    Render a view for Index page, if no query exist.
    Redirect to an Entry page, if a query matches an existing entry.
    Render a Search page, if a query does not match any entry.
    """

    # Check if there is a query else open the index page.
    if len(request.GET) > 0 :
        query = request.GET["q"].strip()
        new_entries = set()
        if len(query) > 0:
            entries = list_entries()
            for entry in entries:
                if query.lower() in entry.lower():
                    # List of entries that have the query as a substring.
                    new_entries.add(entry)

                if query.lower() == entry.lower():
                    # Redirect to entry's page.
                    return redirect("wiki:TITLE",TITLE=query)
        return render(request, "encyclopedia/search.html", {
        "new_entries": new_entries
        })

    else:
        return render(request, "encyclopedia/index.html", {
            "entries": list_entries()
    })

def entry_page(request,TITLE):
    """
    Render an Entry page, if the 'TITLE' matches an encyclopedia entry.
    Else, render an Error page.
    """
    entry = get_entry(TITLE)
    if entry:
        entry_titles = list_entries()
        for entry_title in entry_titles:
            if entry_title.lower() == TITLE.lower():
                TITLE = entry_title
                break
        html_entry = markdown2.markdown(entry)
        return render(request, "encyclopedia/entrypage.html", {
            "html_entry": html_entry,
            "entry": entry, 
            "title": TITLE
        })
    else:
        # Error page
        return render(request, "encyclopedia/errorpage.html", {
            "error": 'Page Not Found'
        })


def new_page(request):
    """
    Render a page where a user can create a new encyclopedia entry.
    Error checking if an encyclopedia entry already exists with the provided title, and
    Error checking if the user submit an empty form.
    Otherwise, save the encyclopedia entry to disk, and redirect to the new entry's page.
    """
    if request.method == "POST":
        title = request.POST["title"].strip()
        content = request.POST["content"]
        entries = list_entries()
        for entry in entries:
            if entry.lower() == title.lower():
                error1 = f"Your  Title '{title}' already exist!"
                return render(request, "encyclopedia/newpage.html", {
                    "error1": error1
                })
        if len(title) > 0 and len(content) > 0:
            save_entry(title,content)
            return redirect("wiki:TITLE",TITLE=title)
        else:
            error2 = "Please enter both a Title and it's Markdown Content!"
            return render(request, "encyclopedia/newpage.html", {
                    "error2": error2
                })
    else:
        return render(request, "encyclopedia/newpage.html")


def edit(request):
    """
    Edit a Markdown content and redirect to the content's page after been saved.
    """
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        if len(request.POST) > 3:
            if len(content) > 0:
                save_entry(title,content)
                return redirect("wiki:TITLE",TITLE=title)
            else:
                error = "Markdown Content connot be empty!"
                return render(request, "encyclopedia/editpage.html", {
                        "error": error,
                        "title": title,
                        "content": content
                    })
        return render(request, "encyclopedia/editpage.html", {
            "title": title,
            "content": content
        })


def random(request):
    """
    Redirect to a random Entry Page.
    """
    ramdom = choice(list_entries())
    return redirect("wiki:TITLE",TITLE=ramdom) 