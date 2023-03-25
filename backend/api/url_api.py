from http import HTTPStatus

from flask import request, jsonify, Response, make_response
from flask_restful import Resource

from application.url_repo import UrlRepository
from application.url_service import UrlService
from infra.auth import requires_auth


url_repo = UrlRepository
url_service = UrlService

class Url(Resource):

    @requires_auth
    def post(self) -> Response:

        title = request.json.get("title")
        original_url = request.json.get("original_url")
        
        short_url = url_service.generate_short_url() # Generating a short link

        data = {
            "title": title,
            "original_url": original_url,
            "short_url": short_url
        }
        
        result = url_repo.insert_new_url(data)

        if not result:
            return make_response(jsonify("Failed to insert!"), HTTPStatus.INTERNAL_SERVER_ERROR)

        return make_response(jsonify("Short url created"), HTTPStatus.CREATED)

    @requires_auth
    def get(self, url_id: int) -> Response:
        return make_response(jsonify(url_repo.get_url_by_id(url_id)), HTTPStatus.OK)

    @requires_auth
    def delete(self, url_id: int) -> Response:
        try:
            deleted_url, is_success = url_repo.delete_url_by_id(
                url_id=url_id,
            )

            if not is_success:
                return make_response(
                    f"Failed to delete Url with ID {url_id}",
                    HTTPStatus.INTERNAL_SERVER_ERROR,
                )

            return make_response(
                f"Url {deleted_url.title} {deleted_url.original_url} deleted!",
                HTTPStatus.OK,
            )
        except ValueError as ex:
            print(ex)
            return make_response(f"Url not found", HTTPStatus.NOT_FOUND)
