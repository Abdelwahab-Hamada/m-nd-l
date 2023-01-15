class Query:
    @property
    def query(self):
        return self._query

    def set_contains(self,string=None):
        self._query=self._query.format(str=string)

class LostPosts(Query):
    def __init__(self):
        self._query=(
            '''
                query {{
                    lostPosts(orderBy:"-created_on",item_Label_Icontains:"{str}"){{
                        edges{{
                            node{{
                                id
                                uid
                                readableTime
                                description
                                imageId
                                item{{
                                    label
                                }}
                                color{{
                                    label
                                }}
                                place{{
                                    label
                                }}
                            }}
                        }}
                    }}
                }}
            '''
        )

class FoundPosts(Query):
    def __init__(self):
        self._query=(
            '''
                query {{
                    foundPosts(orderBy:"-created_on",item_Label_Icontains:"{str}"){{
                        edges{{
                            node{{
                                id
                                uid
                                readableTime
                                description
                                imageId
                                item{{
                                    label
                                }}
                                color{{
                                    label
                                }}
                                place{{
                                    label
                                }}
                            }}
                        }}
                    }}
                }}
            '''
        )

class Items(Query):
    def __init__(self):
        self._query=(
            '''
                query {{
                    items(orderBy:"label",label_Contains:"{str}"){{
                        edges{{
                            node{{
                                id
                                label
                            }}
                        }}
                    }}
                }}
            '''
        )

class Item(Query):
    def __init__(self):
        self._query=(
            '''
                query {{
                    item(id:"{str}"){{
                        label
                        lostSet(orderBy:"-created_on"){{
                            id
                            uid
                            readableTime
                            description
                            imageId
                        }}

                        foundSet(orderBy:"-created_on"){{
                            id
                            uid
                            readableTime
                            description
                            imageId
                        }}
                    }}
                }}
            '''
        )