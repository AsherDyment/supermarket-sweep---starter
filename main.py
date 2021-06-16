@namespace
class SpriteKind:
    Grocery = SpriteKind.create()
    CartItem = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    if controller.A.is_pressed():
        addToCart(otherSprite)
sprites.on_overlap(SpriteKind.player, SpriteKind.Grocery, on_on_overlap)

def createTextSprite():
    global subTotalSprite
    subTotalSprite = textsprite.create("$0")
    subTotalSprite.left = 0
    subTotalSprite.top = 0
    subTotalSprite.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
def addToCart(grocery: Sprite):
    global item, cost, subtotal
    item = sprites.create(grocery.image, SpriteKind.CartItem)
    item.follow(player)
    item.x = player.x
    item.y = player.y
    cost = sprites.read_data_number(grocery, "cost")
    subtotal = subtotal + cost
def createProducts():
    global productImg, productCost, productWeight, productName
    i = 0
    while i <= len(groceryImages) - 1:
        productImg = groceryImages[i]
        productCost = groceryCosts[i]
        productWeight = groceryWeights[i]
        productName = groceryNames[i]
        createProduct(productImg, 0, 0, "")
        i += 1
def createProduct(productImg: Image, cost: number, weight: number, name: str):
    global product
    product = sprites.create(productImg, SpriteKind.Grocery)
    tiles.place_on_random_tile(product, assets.tile("""
        tile1
    """))
    sprites.set_data_number(product, "cost", cost)
    sprites.set_data_number(product, "weight", weight)
    sprites.set_data_string(product, "name", name)
product: Sprite = None
productName = ""
productWeight = 0
productCost = 0
productImg: Image = None
subtotal = 0
cost = 0
item: Sprite = None
subTotalSprite: TextSprite = None
player: Sprite = None
groceryCosts: List[number] = []
groceryWeights: List[number] = []
groceryNames: List[str] = []
groceryImages: List[Image] = []
groceryImages = [img("""
        . . . 2 2 2 . . . . . . . . . . 
            . . . c c c 6 6 8 8 . . . . . . 
            . . 6 1 1 1 1 1 9 6 8 . . . . . 
            . 6 1 1 1 1 1 1 8 9 6 8 . . . . 
            6 1 1 1 1 1 1 8 . 8 9 8 . . . . 
            6 1 1 1 1 1 1 8 . 8 9 8 . . . . 
            8 9 1 1 1 1 1 8 . 8 9 8 . . . . 
            8 9 1 1 1 1 1 8 8 9 9 8 . . . . 
            8 9 9 9 9 9 9 9 9 9 9 8 . . . . 
            8 6 9 9 9 9 9 9 9 9 9 8 . . . . 
            . 8 6 9 9 9 9 9 9 9 6 8 . . . . 
            . . 8 8 8 8 8 8 8 8 8 . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    img("""
        . . . . . . . 6 6 6 . . . . . . 
            . . . . . . . c b c . . . . . . 
            . . . . . c c c b c c c . . . . 
            . . . . c b b b b b b b c . . . 
            . . . . c 1 b b b b b 1 c . . . 
            . . . . c 1 1 7 1 7 1 1 c . . . 
            . . . . c 1 1 1 7 1 1 1 c . . . 
            . . . . c 1 1 a c a 1 1 c . . . 
            . . . . c 1 a c a c a 1 c . . . 
            . . . . c 1 c a c a c 1 c . . . 
            . . . . c 1 a c a c a 1 c . . . 
            . . . . c 1 c a c a 1 1 c . . . 
            . . . . c 1 a c a 1 1 1 c . . . 
            . . . . c b 1 a 1 1 1 b c . . . 
            . . . . c b b b b b b b c . . . 
            . . . . . c c c c c c c . . . .
    """),
    img("""
        . c c c c c c c c c c c c c . . 
            c b b b b b b b b b b b b b c . 
            c b b b b b b b b b b b b b c . 
            c c c c c c c c c c c c c c c . 
            c d d 1 1 1 1 1 1 1 1 1 d d c . 
            c d c c c 1 c c c 1 c c c d c . 
            c d c 1 c 1 c 1 c 1 1 c d d c . 
            c d c 1 c 1 c c c 1 1 c d d c . 
            c d c c c 1 c 1 c 1 1 c d d c . 
            c d d 1 1 1 1 1 1 1 1 1 d d c . 
            c d d 1 1 1 2 2 2 1 1 1 d d c . 
            c d d 1 1 2 8 8 8 2 1 1 d d c . 
            c d d 1 1 2 8 d 8 2 1 1 d d c . 
            c d d 1 1 2 8 6 8 2 1 1 d d c . 
            . c d 1 1 1 2 2 2 1 1 1 d c . . 
            . . c c c c c c c c c c c . . .
    """),
    img("""
        . . . c c c c . . . . . . . . . 
            . . c e e e e c c c . . . . . . 
            . c e e e e e e e e c . . . . . 
            . c e e e e e e e e e c . . . . 
            f e e e e c c c e e e c . b b . 
            f e e e c e e e c c c c c d d b 
            f c e e f e e e e e e e c d d b 
            f c c c f e e e f f f f c b b b 
            f c c c c f f f c c c f . c c . 
            . f c c c c c c c c c f . . . . 
            . f c c c c c c c c f . . . . . 
            . . f f f f f f f f . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    img("""
        . . . . . . . . . . . . . . . . 
            . . 6 6 9 9 9 9 . . . . . . . . 
            . 6 9 9 1 1 1 1 9 . . . . . . . 
            6 9 6 9 9 9 1 9 1 9 . . . . . . 
            6 9 9 6 6 6 6 1 1 9 . . . . . . 
            6 9 9 6 9 9 6 1 1 9 . . . . . . 
            . 6 9 6 9 9 6 1 9 . . . . . . . 
            . . 6 9 6 6 1 9 . . . . . . . . 
            . . . 6 9 9 9 . . . . . . . . . 
            . . . . 6 6 . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    img("""
        . . . . . . . . . . . . . . . . 
            . . . . c c c c c c c . . . . . 
            . . . c d d d d d d d c . . . . 
            . . c d d d d d b b d d c . . . 
            . . b c d d d d d d d c b . . . 
            . . b 2 c c c c c c c 2 b . . . 
            . . b 2 2 2 2 2 2 2 2 2 b . . . 
            . . b 2 2 2 2 2 2 2 2 2 b . . . 
            . . b 2 2 2 b b b 2 2 2 b . . . 
            . . b 2 2 b 2 2 2 b 2 2 b . . . 
            . . d 1 2 b 2 2 2 b 2 1 d . . . 
            . . d 1 1 b 2 2 2 b 1 1 d . . . 
            . . d 1 1 b 2 2 2 b 1 1 d . . . 
            . . d 1 1 1 b b b 1 1 1 d . . . 
            . . . d 1 1 1 1 1 1 1 d . . . . 
            . . . . d d d d d d d . . . . .
    """),
    img("""
        . . c c c c c c c c c c . . . . 
            . c d d d d d d d c b b c . . . 
            c d d d d d d d c b d b b c . . 
            c c d d d d d d d c b b c c . . 
            c b c c c c c c c c c c b c . . 
            c b 8 9 8 b 8 9 9 9 8 b b c . . 
            c b b 8 9 6 9 6 9 6 9 8 b c . . 
            c b b 8 9 6 9 6 9 6 9 8 b c . . 
            c b 8 9 8 b 8 9 9 9 8 b b c . . 
            . c c c c c c c c c c c c . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    img("""
        . . . . . . . . . . . . . . . . 
            . . . b 1 1 1 1 1 1 1 1 1 . . . 
            . . b 1 1 1 1 1 1 1 1 1 1 1 . . 
            . . b 1 1 1 1 1 1 1 1 1 8 8 . . 
            . . b 1 1 1 1 1 1 1 8 8 8 8 . . 
            . . b 1 1 1 5 5 5 5 8 8 8 8 . . 
            . . b 1 1 5 5 5 5 5 5 8 8 8 . . 
            . . b 1 8 5 5 5 5 5 5 8 8 8 . . 
            . . c 8 8 5 5 5 5 5 5 8 1 1 . . 
            . . c 8 8 5 5 5 5 5 5 1 1 1 . . 
            . . c 8 8 8 5 5 5 5 1 1 1 1 . . 
            . . c 8 8 8 1 1 1 1 1 1 1 1 . . 
            . . c 2 2 2 1 1 1 1 6 6 6 1 . . 
            . . b 1 2 1 1 1 1 1 1 1 1 1 . . 
            . . b 1 1 1 1 1 1 1 1 1 1 1 . . 
            . . . b b b b b b b b b b . . .
    """),
    img("""
        . . . . . . . 6 . . . . . . . . 
            . . . . 6 6 6 6 6 6 6 . . . . . 
            . . 6 6 6 6 7 6 7 6 6 6 6 . . . 
            . 6 6 7 6 6 7 6 7 6 6 7 7 6 . . 
            . 6 6 7 6 7 6 6 7 6 6 7 6 6 . . 
            6 7 6 7 6 7 6 6 7 7 6 7 6 7 6 . 
            6 7 6 7 6 7 6 6 7 7 6 7 6 7 6 . 
            6 7 6 7 6 7 6 6 7 7 6 7 6 7 6 . 
            6 7 6 7 6 7 6 6 7 7 6 7 6 7 6 . 
            6 7 6 7 6 7 6 6 7 7 6 7 6 7 6 . 
            6 7 6 7 6 7 6 6 7 6 6 7 6 7 6 . 
            6 6 6 7 6 7 6 6 7 6 6 7 6 6 6 . 
            . 6 6 7 6 7 6 6 7 6 6 7 6 6 . . 
            . 6 6 7 6 7 7 6 7 6 6 7 6 6 . . 
            . . 6 6 6 6 7 6 7 6 6 6 6 . . . 
            . . . . 6 6 6 6 6 6 6 . . . . .
    """)]
groceryNames = ["Milk",
    "Grape Soda",
    "Oatmeal",
    "Turkey",
    "dimond",
    "Chicken soup",
    "Sardines",
    "Flour",
    "Watermelon"]
groceryWeights = [8, 2, 1, 12, 0.5, 0.5, 0.5, 5, 10]
groceryCosts = [2, 3, 4, 20, 10, 2, 1, 5, 3]
scene.set_background_color(9)
tiles.set_tilemap(tilemap("""
    level
"""))
player = sprites.create(img("""
        fffffff......................
            f.fffcd......................
            ..ffddc......................
            ..fdddf......................
            ..fdddd......................
            ...55........................
            ..55dddbbbbbbbbbbbb..........
            ..555....b..b..b..b..........
            .5555....bbbbbbbbbb..........
            .5555....b..b..b..b..........
            .5555....bbbbbbbbbb..........
            .6666.....b.b..b.bb..........
            .6.66......bbbbbbb...........
            .d.d.......d.................
            .d..d......ddddddd...........
            .d..dd......c....c...........
    """),
    SpriteKind.player)
controller.move_sprite(player)
tiles.place_on_tile(player, tiles.get_tile_location(1, 3))
scene.camera_follow_sprite(player)
createProducts()
createTextSprite()