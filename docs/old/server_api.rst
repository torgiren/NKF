BASE
===============

:: 

    GET /

::
    
    200 OK
    {
    }

VAT
===============

::

    GET /vat

::
    
    200 OK 
    {
        "vats" : [
            {  
                "id": 1,
                "value": "0",
                "links": [
                    {
                        "href": "/vat/1",
                        "rel": "self",
                        "method": "GET"
                    },
                    {
                        "href": "/vat/1",
                        "rel": "edit",
                        "method": "PUT"
                    },
                    {
                        "href": "/vat/1",
                        "rel": "delete",
                        "method": "DELETE"
                    }
                ]
            },
            {  
                "id": 2,
                "value": "7",
                "links": [
                    {
                        "href": "/vat/2",
                        "rel": "self",
                        "method": "GET"
                    },
                    {
                        "href": "/vat/2",
                        "rel": "edit",
                        "method": "PUT"
                    },
                    {
                        "href": "/vat/2",
                        "rel": "delete",
                        "method": "DELETE"
                    }
                ]
            },

        "links": [
            {
                "href": "/vat",
                "rel": "create",
                "method": "POST"
            }
        ]
    }

:: 

    GET /vat/2

:: 

    200 OK
    {
        "vat": {
            "id": 2,
            "value": "7",
            "links": [
                {
                    "href": "/vat/2",
                    "rel": "self",
                    "method": "GET"
                },
                {
                    "href": "/vat/2",
                    "rel": "edit",
                    "method": "PUT"
                },
                {
                    "href": "/vat/2",
                    "rel": "delete",
                    "method": "DELETE"
                }
        },
        "links": {
            "href": "/vat",
            "rel": "list",
            "method": "GET"
        }
    }

::

    POST /vat
    {
        "value": "23"
    }

:: 

    201 Created
    {
        "vat": {
            "id": 3,
            "value": "23",
            "links": [
                {
                    "href": "/vat/3",
                    "rel": "self",
                    "method": "GET"
                },
                {
                    "href": "/vat/3",
                    "rel": "edit",
                    "method": "PUT"
                },
                {
                    "href": "/vat/3",
                    "rel": "delete",
                    "method": "DELETE"
                }
        },
        "links": {
            "href": "/vat",
            "rel": "list",
            "method": "GET"
        }
    }

:: 

    DELETE /vat/1

::
    
    204 No content
    {
        "links": {
            "href": "/vat",
            "rel": "list",
            "method": "GET"
        }
    }

TOWAR
========

:: 

    GET /towar

::

    200 OK
    {
        "items": [
            {
                "id": 1,
                "nazwa": "Mleko 1L 2%",
                "opis": "Mleko Laciate 2%, 1 litr"
                "jm" : {
                    "nazwa": "szt",
                    "href": "/jm/1"
                }
                "grupa": {
                    "nazwa": "Nabial",
                    "href": "/grupa/3"
                }
                "cena": {
                    "brutto": "3.20",
                    "netto": "2,80",
                    "href": "/cena/1"
                }
                "stan": "26",
                "ostatni_zakup": {
                    "data": "2014-10-12",
                    "temu": "20", #dni
                    "kontrahent" {
                        "nazwa": "Mleczarnia",
                        "href": "/kontrahent/4"
                    }
                    "href" : "/towar/1/zakupy"
                } 
