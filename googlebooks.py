"""
Google Books Api

See: https://developers.google.com/books/
"""
from typing import Any, Dict, List, Optional, Union

import requests


_BASEURL = "https://www.googleapis.com/books/v1"

VolumeResponse = Dict[str, Any]
ListResponse = Dict[str, Union[str, List[VolumeResponse], int]]


def _get(path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    if params is None:
        params = {}

    resp: requests.Response = requests.get(_BASEURL + path, params=params)

    resp.raise_for_status()

    return resp.json(encoding="utf-8")


def get(volume_id: str, **kwargs: str) -> VolumeResponse:
    """
    Retrieve a Volume resource based on ID
    volumeId -- ID of volume to retrieve.

    Optional Parameters:
    partner: `str` --  Brand results for partner ID.

    projection: `str` -- Restrict information returned to a set of selected fields. 
                Acceptable values are:
                "full" - Includes all volume data.
                "lite" - Includes a subset of fields in volumeInfo and accessInfo.

    source: `str` -- String to identify the originator of this request.

    See: https://developers.google.com/books/docs/v1/reference/volumes/get
    """
    path = f"/volumes/{volume_id}"

    if kwargs:
        for optional_parameter in kwargs:
            if optional_parameter not in "partner projection source":
                raise ValueError(f"Parameter '{optional_parameter}' not valid")

    return _get(path, kwargs)


def list_books(query: str, **kwargs: Union[str, int, bool]) -> ListResponse:
    """
    Perform a book search.
    query -- Full-text search query string.

        There are special keywords you can specify in the search terms to
        search in particular fields, such as:

        intitle: Returns results where the text following this keyword is
                found in the title.

        inauthor: Returns results where the text following this keyword is
                found in the author.

        inpublisher: Returns results where the text following this keyword
                is found in the publisher.

        subject: Returns results where the text following this keyword is
                listed in the category list of the volume.

        isbn:   Returns results where the text following this keyword is the
                ISBN number.

        lccn:   Returns results where the text following this keyword is the
                Library of Congress Control Number.

        oclc:   Returns results where the text following this keyword is the
                Online Computer Library Center number.

    Optional Parameters:

    download: `str` -- Restrict to volumes by download availability. 
                Acceptable values are:
                "epub" - All volumes with epub.

    filter: `str` -- Filter search results. 
                Acceptable values are:
                "ebooks" - All Google eBooks.
                "free-ebooks" - Google eBook with full volume text viewability.
                "full" - Public can view entire volume text.
                "paid-ebooks" - Google eBook with a price.
                "partial" - Public able to see parts of text.

    langRestrict: `str` -- Restrict results to books with this language code.

    libraryRestrict: `str` -- Restrict search to this user's library. 
                Acceptable values are:
                "my-library" - Restrict to the user's library, any shelf.
                "no-restrict" - Do not restrict based on user's library.

    maxResults: `int` -- Maximum number of results to return. Acceptable values are 0 to 40, inclusive.

    orderBy: `str` -- Sort search results.
                Acceptable values are:
                "newest" - Most recently published.
                "relevance" - Relevance to search terms.

    partner: `str`	--  Restrict and brand results for partner ID.

    printType: `str` -- Restrict to books or magazines. 
                Acceptable values are:
                "all" - All volume content types.
                "books" - Just books.
                "magazines" - Just magazines.

    projection: `str` -- Restrict information returned to a set of selected fields. 
                Acceptable values are:
                "full" - Includes all volume data.
                "lite" - Includes a subset of fields in volumeInfo and accessInfo.

    showPreorders: `bool` -- Set to true to show books available for preorder. Defaults to false.

    source: `str` --  String to identify the originator of this request.

    startIndex: `int` -- Index of the first result to return (starts at 0).

    See: https://developers.google.com/books/docs/v1/reference/volumes/list
    """
    path = "/volumes"

    params: Dict[str, Union[str, int, bool]] = {"q": query}

    if kwargs:
        for optional_parameter in kwargs:
            if optional_parameter not in (
                "download filter langRestrict libraryRestrict maxResults "
                "orderBy partner printType projection showPreorders source startIndex"
            ):
                raise ValueError(f"Parameter '{optional_parameter}' not valid")

        params.update(kwargs)

    return _get(path, params)

