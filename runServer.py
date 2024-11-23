from flask import Flask, send_from_directory, jsonify

import json
import get_drink, get_recipe

app = Flask(__name__)

@app.route('/')  # '/' 경로 접속 시 start 실행 (라우팅 이라고 부름)
def start():  # 함수의 이름은 중복만 되지 않으면 됨
    return send_from_directory('static', 'api_rules.png')

# show all drink
@app.route('/drink/all')
def drinks():
    return app.response_class(
        response=json.dumps(get_drink.getalldrinks(), indent=4),
        mimetype='application/json'
    )
# show drink image
@app.route('/drink/image=<code>')
def drink_image(code=None):
    return send_from_directory('static', 'drinks/{}.png'.format(code))

# search drinks by <code>
@app.route('/drink/code=<code>')
def drink_code(code):
    info = get_drink.search_bycode(code)
    return app.response_class(
        response=json.dumps(info, indent=4),
        mimetype='application/json'
    )

# search drinks by <name>
@app.route('/drink/name=<name>')
def drink_name(name):
    info = get_drink.search_byname(name)
    return app.response_class(
        response=json.dumps(info, indent=4),
        mimetype='application/json'
    )

# search drinks by <type>
@app.route('/drink/type=<type>')
def drink_type(type):
    info = get_drink.search_bytype(type)
    return app.response_class(
        response=json.dumps(info, indent=4),
        mimetype='application/json'
    )


# show all recipe
@app.route('/recipe/all')
def all_recipes():
    return app.response_class(
        response=json.dumps(get_recipe.getallrecipes(), indent=4),
        mimetype='application/json'
    )
# show recipe image
@app.route('/recipe/image=<code>')
def recipe_image(code=None):
    return send_from_directory('static', 'recipes/{}.png'.format(code))

# search recipes by <name>
@app.route('/recipe/name=<name>')
def recipe_name(name):
    info = get_recipe.search_byname(name)
    return app.response_class(
        response=json.dumps(info, indent=4),
        mimetype='application/json'
    )

# search recipes by <code>
@app.route('/recipe/code=<code>')
def recipe_code(code):
    print(code)
    info = get_recipe.search_bycode(code)
    return app.response_class(
        response=json.dumps(info, indent=4),
        mimetype='application/json'
    )

# search available recipes
@app.route('/recipe/with=<codes>')
def recipe_with(codes):
    info = get_recipe.search_byings(codes)
    return app.response_class(
        response=json.dumps(info, indent=4),
        mimetype='application/json'
    )


# show ingredient image
@app.route('/ing/image=<name>')
def ing_image(name=None):
    return send_from_directory('static', 'ingredients/{}.png'.format(name))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2222)  # app 실행