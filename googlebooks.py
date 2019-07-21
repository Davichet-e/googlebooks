import json
from typing import Dict, Optional, Union

import requests


class GoogleBooksApi:
    """
    Google Books Api
    
    See: https://developers.google.com/books/
    """

    _BASEURL: str = "https://www.googleapis.com/books/v1"

    @classmethod
    def _get(cls, path: str, params: Optional[dict] = None) -> dict:
        if params is None:
            params = {}

        resp: requests.Response = requests.get(cls._BASEURL + path, params=params)

        resp.raise_for_status()

        return json.loads(resp.content)

    @classmethod
    def get(cls, volume_ID: str, **optional_parameters: str) -> dict:
        """
        Retrieve a Volume resource based on ID
        volumeId -- ID of volume to retrieve.
        Optional Parameters:
        partner --  Brand results for partner ID.
        
        projection -- Restrict information returned to a set of selected fields. 
                    Acceptable values are:
                    "full" - Includes all volume data.
                    "lite" - Includes a subset of fields in volumeInfo and accessInfo.
        
        source --   String to identify the originator of this request.
        See: https://developers.google.com/books/docs/v1/reference/volumes/get
        """
        path: str = "/volumes/" + volume_ID

        if optional_parameters:
            for optional_parameter in optional_parameters:
                if optional_parameter not in "partner projection source".split():
                    raise ValueError(f"Parameter '{optional_parameter}' not valid")

        return cls._get(path, params=optional_parameters)

    @classmethod
    def list_(cls, query: str, **optional_parameters: str) -> dict:
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

        download -- Restrict to volumes by download availability. 
                    Acceptable values are:
                    "epub" - All volumes with epub.
        filter --   Filter search results. 
                    Acceptable values are:
                    "ebooks" - All Google eBooks.
                    "free-ebooks" - Google eBook with full volume text viewability.
                    "full" - Public can view entire volume text.
                    "paid-ebooks" - Google eBook with a price.
                    "partial" - Public able to see parts of text.
        langRestrict -- Restrict results to books with this language code.
        libraryRestrict	-- Restrict search to this user's library. 
                    Acceptable values are:
                    "my-library" - Restrict to the user's library, any shelf.
                    "no-restrict" - Do not restrict based on user's library.
        maxResults -- Maximum number of results to return. Acceptable values are 0 to 40, inclusive.
        orderBy	 -- Sort search results. 
                    Acceptable values are:
                    "newest" - Most recently published.
                    "relevance" - Relevance to search terms.
        partner	--  Restrict and brand results for partner ID.
        printType -- Restrict to books or magazines. 
                    Acceptable values are:
                    "all" - All volume content types.
                    "books" - Just books.
                    "magazines" - Just magazines.
        projection -- Restrict information returned to a set of selected fields. 
                    Acceptable values are:
                    "full" - Includes all volume data.
                    "lite" - Includes a subset of fields in volumeInfo and accessInfo.
        
        showPreorders -- Set to true to show books available for preorder. Defaults to false.
        source --  String to identify the originator of this request.
        startIndex -- Index of the first result to return (starts at 0).

        See: https://developers.google.com/books/docs/v1/reference/volumes/list
        """
        path: str = "/volumes"

        params: Dict[str, str] = {"q": query}

        if optional_parameters:
            for optional_parameter in optional_parameters:
                if (
                    optional_parameter
                    not in (
                        "download filter langRestrict libraryRestrict maxResults "
                        "orderBy partner printType projection showPreorders source startIndex"
                    ).split()
                ):
                    raise ValueError(f"Parameter '{optional_parameter}' not valid")

            params.update(optional_parameters)

        return cls._get(path, params)

