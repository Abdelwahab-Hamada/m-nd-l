class Mutation:
    @property
    def mutation(self):
        return self._mutation

class Lost(Mutation):
    def __init__(self):
        self._mutation=(
            f'''
                mutation (
                    $uid:String!,
                    $description:String!,
                    $imageId:String,
                    $itemId:String!,
                    $colorId:String!,
                    $placeId:String!
                ){{
                    lost(
                        input:{{
                            uid:$uid,
                            description:$description,
                            imageId:$imageId,
                            itemId:$itemId,
                            colorId:$colorId,
                            placeId:$placeId
                        }}
                    ){{
                        posted
                    }}
                }}
            '''
        )

class Found(Mutation):
    def __init__(self):
        self._mutation=(
            f'''
                mutation (
                    $uid:String!,
                    $description:String!,
                    $imageId:String,
                    $itemId:String!,
                    $colorId:String!,
                    $placeId:String!
                ){{
                    found(
                        input:{{
                            uid:$uid,
                            description:$description,
                            imageId:$imageId,
                            itemId:$itemId,
                            colorId:$colorId,
                            placeId:$placeId
                        }}
                    ){{
                        posted
                    }}
                }}
            '''
        )

class Item(Mutation):
    def __init__(self):
        self._mutation=(
            f'''
                mutation ($label:String!){{
                    item(label:$label){{
                        node{{
                            id
                            label
                        }}
                    }}
                }}
            '''
        )

class Color(Mutation):
    def __init__(self):
        self._mutation=(
            f'''
                mutation ($label:String!){{
                    color(label:$label){{
                        node{{
                            id
                            label
                        }}
                    }}
                }}
            '''
        )

class Place(Mutation):
    def __init__(self):
        self._mutation=(
            f'''
                mutation ($label:String!){{
                    place(label:$label){{
                        node{{
                            id
                            label
                        }}
                    }}
                }}
            '''
        )