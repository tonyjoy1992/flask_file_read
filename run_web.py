from flask import Flask, jsonify, request
from files.settings import *
app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def root():
#     """
#     main page
#     :return:
#     """
#     return_content = {}
#     if request.method == "GET":
#         with open(FILES_PATH + "file1.txt") as f:
#             content = f.readlines()
#             return_content["file_read"] = "file1.txt"
#             return_content["number_of_lines_read"] = len(content)
#             return_content["lines"] = content
#
#     return jsonify(return_content)


@app.route('/', methods=['GET'])
@app.route('/<file_name>', methods=['GET'])
def read_file_with_index(file_name=None):
    """
    http://127.0.0.1:5000/<file_name>?from=<from_line>&to=<to_line>
    :param file_name: Name of file to read
    :return:
    """
    from_line = 0
    to_line = 0
    return_content = {}

    if request.method == "GET":
        try:
            from_line = int(request.args.get('from'))
        except:
            pass

        try:
            to_line = int(request.args.get('to'))
        except:
            pass

        if file_name:
            full_file_name = FILES_PATH + "%s" % file_name
            with open(full_file_name) as f:
                content = f.readlines()

            if from_line and to_line:
                content = content[from_line - 1:to_line]
                return_content["file_read"] = file_name
                return_content["number_of_lines_read"] = len(content)
                return_content["lines"] = content
            else:
                return_content["file_read"] = file_name
                return_content["number_of_lines_read"] = len(content)
                return_content["lines"] = content
        else:
            with open(FILES_PATH + "file1.txt") as f:
                content = f.readlines()

            if from_line and to_line:
                content = content[from_line - 1:to_line]
                return_content["file_read"] = "file1.txt"
                return_content["number_of_lines_read"] = len(content)
                return_content["lines"] = content
            else:
                return_content["file_read"] = "file1.txt"
                return_content["number_of_lines_read"] = len(content)
                return_content["lines"] = content

    return jsonify(return_content)


if __name__ == "__main__":
    app.run()
