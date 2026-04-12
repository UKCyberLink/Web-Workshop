from flask import Flask, send_from_directory, Response, request
import os
import shutil
import requests

app = Flask(__name__, static_folder="static")

app.config["HTML_FILES"] = []
app.config["CSS_FILES"] = []
app.config["JAVASCRIPT_FILES"] = []
app.config["PHP_FILES"] = []
app.config["IS_DIRECTORIES"] = False
app.config["PHP_SERVER"] = "http://localhost:8000"

@app.route('/')
def index_checker():
    if "index.html" in app.config["HTML_FILES"]:
        html_path = "raw-files/"
        if app.config["IS_DIRECTORIES"]:
            html_path = f"{html_path}/{'html'}"

        return send_from_directory(html_path, "index.html")



def find_raw_files():
    html_files = []
    css_files = []
    javascript_files = []
    php_files = []
    path = "./raw-files"
    all_files_directories = os.listdir(path)
    isDirectory = check_if_in_directories(all_files_directories, path)
    if isDirectory:
        app.config["IS_DIRECTORIES"] = True
        os.makedirs("static/css", exist_ok=True)
        os.makedirs("static/javascript", exist_ok=True)
        for itm in all_files_directories:
            if itm.lower() == "html":
                html_files.extend(os.listdir(os.path.join(path, "html")))
            if itm.lower() == "php":
                php_files.extend(os.listdir(os.path.join(path, "php")))
            if itm.lower() == "css":
                css_path = "./raw-files/css"
                for file in os.listdir(css_path):
                    css_files.append(file)
                    shutil.copy2(os.path.join(css_path, file), "static/css")
            if itm.lower() == "javascript":
                javascript_path = "./raw-files/javascript"
                for file in os.listdir(javascript_path):
                    javascript_files.append(file)
                    shutil.copy2(os.path.join(javascript_path, file), "static/javascript")
    else:
        os.makedirs("static", exist_ok=True)
        for itm in all_files_directories:
            if itm.endswith(".html"):
                html_files.append(itm)
            if itm.endswith(".php"):
                php_files.append(itm)
            if itm.endswith(".css"):
                path = "./raw-files/"
                css_files.append(itm)
                shutil.copy2(os.path.join(path, itm), "static")
            if itm.endswith(".js"):
                path = "./raw-files/"
                javascript_files.append(itm)
                shutil.copy2(os.path.join(path, itm), "static")

    return html_files, css_files, javascript_files, php_files

@app.route("/<path:filename>", methods=["GET", "POST"])
def make_html_routes(filename):
    if filename == "image.png":
        return send_from_directory("static", "image.png")

    html_path = "raw-files/"
    css_path = "static/"
    javascript_path = "static/"
    php_path = "raw-files/"
    print(app.config["IS_DIRECTORIES"])
    print(filename)
    if app.config["IS_DIRECTORIES"]:
        html_path = f"{html_path}/{'html'}"
        css_path = f"{css_path}/{'css'}"
        javascript_path = f"{javascript_path}/{'javascript'}"
        php_path = f"{php_path}/{'php'}"
        filename = filename.split("/")[-1]
     
    if filename in app.config["CSS_FILES"]:
        print(css_path)
        return send_from_directory(css_path, filename)
    elif filename in app.config["JAVASCRIPT_FILES"]:
        return send_from_directory(javascript_path, filename)
    elif (filename + ".php") in app.config["PHP_FILES"]:
        filename = filename + '.php'
        php_url = f"{app.config['PHP_SERVER']}/{filename}"
        if app.config["IS_DIRECTORIES"]:
            php_url = f"{app.config['PHP_SERVER']}/php/{filename}"
        response = requests.request(
        method=request.method,
        url=php_url,
        data=request.form if request.method == "POST" else None,
        params=request.args if request.method == "GET" else None
    )


        return Response(
            response.content,
            status=response.status_code,
            content_type=response.headers.get("Content-Type")
        )
    elif (filename) in app.config["HTML_FILES"]:
        return send_from_directory(html_path, filename)
    # html must be last for nice url formatting
    elif (filename + ".html") in app.config["HTML_FILES"]:
        return send_from_directory(html_path, filename + ".html")
    else:
        return send_from_directory("raw-files", "404-error.html"), 404
                
def check_if_in_directories(all_files_directories, path):
    for itm in all_files_directories:
        if os.path.isdir(os.path.join(path, itm)) == True:
            return True
    return False

def clear_static():
    path = "./static"
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.remove(item_path)  # delete files
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)

if __name__ == '__main__':
    clear_static()
    html_files, css_files, javascript_files, php_files = find_raw_files()
    shutil.copy("image.png", "static/image.png")
    app.config["HTML_FILES"] = html_files
    app.config["CSS_FILES"] = css_files
    app.config["JAVASCRIPT_FILES"] = javascript_files
    app.config["PHP_FILES"] = php_files
    app.run(debug=True)